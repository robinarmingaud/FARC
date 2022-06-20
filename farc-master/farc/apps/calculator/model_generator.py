import dataclasses
import datetime
import html
import logging
import os
import typing

import numpy as np
import tornado

from farc import models
from farc import data
import farc.data.weather
import farc.monte_carlo as mc
from .. import calculator
from farc.monte_carlo.data import activity_distributions, virus_distributions, mask_distributions
from farc.monte_carlo.data import expiration_distribution, expiration_BLO_factors, expiration_distributions
from .DEFAULT_DATA import _NO_DEFAULT, _DEFAULT_MC_SAMPLE_SIZE, _DEFAULTS as d, ACTIVITY_TYPES, MECHANICAL_VENTILATION_TYPES, MASK_TYPES,MASK_WEARING_OPTIONS,VENTILATION_TYPES,VIRUS_TYPES,VOLUME_TYPES,WINDOWS_OPENING_REGIMES,WINDOWS_TYPES,COFFEE_OPTIONS_INT,MONTH_NAMES 

LOG = logging.getLogger(__name__)

minutes_since_midnight = typing.NewType('minutes_since_midnight', int)

@dataclasses.dataclass
class FormData:
    # activity_type: str
    humidity: str
    inside_temp: float
    exposed_activity_type: str
    exposed_activity_level : str
    exposed_breathing : float
    exposed_speaking : float
    exposed_shouting : float
    infected_breathing : float
    infected_speaking : float
    infected_shouting : float
    exposed_mask_wear_ratio: float
    infected_activity_type: str
    infected_activity_level : str
    infected_mask_wear_ratio: float
    air_changes: float
    air_supply: float
    ceiling_height: float
    exposed_coffee_break_option: str
    exposed_coffee_duration: int
    exposed_finish: minutes_since_midnight
    exposed_lunch_finish: minutes_since_midnight
    exposed_lunch_option: int
    exposed_lunch_start: minutes_since_midnight
    exposed_start: minutes_since_midnight
    floor_area: float
    biov_amount: float
    biov_option: int
    infected_coffee_break_option: str               #Used if infected_dont_have_breaks_with_exposed
    infected_coffee_duration: int                   #Used if infected_dont_have_breaks_with_exposed
    infected_dont_have_breaks_with_exposed: int
    infected_finish: minutes_since_midnight
    infected_lunch_finish: minutes_since_midnight   #Used if infected_dont_have_breaks_with_exposed
    infected_lunch_option: int                      #Used if infected_dont_have_breaks_with_exposed
    infected_lunch_start: minutes_since_midnight    #Used if infected_dont_have_breaks_with_exposed
    infected_people: int
    infected_start: minutes_since_midnight
    location_name: str
    location_latitude: float
    location_longitude: float
    mask_type: str
    mask_wearing_option: str
    mechanical_ventilation_type: str
    calculator_version: str
    opening_distance: float
    event_month: str
    room_heating_option: int
    room_number: str
    room_volume: float
    simulation_name: str
    total_people: int
    ventilation_type: str
    virus_type: str
    viruses: dict
    volume_type: str
    windows_duration: float
    windows_frequency: float
    window_height: float
    window_type: str
    window_width: float
    windows_number: int
    window_opening_regime: str
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'locale'))
    tornado.locale.load_gettext_translations(path , 'messages')
    locale = tornado.locale.get()
    _ = locale.translate
    _DEFAULTS = d
    MONTHS = list(MONTH_NAMES.keys())
    activities = { activity['Id'] for activity in ACTIVITY_TYPES}
    
    @classmethod
    def from_dict(cls, form_data: typing.Dict, locale) -> "FormData":
        # Take a copy of the form data so that we can mutate it.
        form_data = form_data.copy()
        form_data.pop('_xsrf', None)
        FormData.set_locale(cls, locale)

        # Don't let arbitrary unescaped HTML through the net.
        for key, value in form_data.items():
            if isinstance(value, str):
                form_data[key] = html.escape(value)

        for key, default_value in cls._DEFAULTS.items():
            if form_data.get(key, '') == '':
                if default_value is _NO_DEFAULT:
                    raise ValueError(f"{key} must be specified")
                form_data[key] = default_value

        for key, value in form_data.items():
            if key in _CAST_RULES_FORM_ARG_TO_NATIVE:
                form_data[key] = _CAST_RULES_FORM_ARG_TO_NATIVE[key](value)

            if key not in cls._DEFAULTS:
                raise ValueError(f'Invalid argument "{html.escape(key)}" given')

        instance = cls(**form_data)
        instance.validate()
        return instance

    @classmethod
    def to_dict(cls, form: "FormData", strip_defaults: bool = False) -> dict:
        form_dict = {
            field.name: getattr(form, field.name)
            for field in dataclasses.fields(form)
        }

        for attr, value in form_dict.items():
            if attr in _CAST_RULES_NATIVE_TO_FORM_ARG:
                form_dict[attr] = _CAST_RULES_NATIVE_TO_FORM_ARG[attr](value)

        if strip_defaults:
            del form_dict['calculator_version']

            for attr, value in list(form_dict.items()):
                default = cls._DEFAULTS.get(attr, _NO_DEFAULT)
                if default is not _NO_DEFAULT and value in [default, 'not-applicable']:
                    form_dict.pop(attr)
        return form_dict

    def validate(self):
        # Validate time intervals selected by user
        time_intervals = [
            ['exposed_start', 'exposed_finish'],
            ['infected_start', 'infected_finish'],
        ]
        if self.exposed_lunch_option == 1:
            time_intervals.append(['exposed_lunch_start', 'exposed_lunch_finish'])
        if self.infected_dont_have_breaks_with_exposed==1 and self.infected_lunch_option == 1:
            time_intervals.append(['infected_lunch_start', 'infected_lunch_finish'])

        for start_name, end_name in time_intervals:
            start = getattr(self, start_name)
            end = getattr(self, end_name)
            if start > end:
                raise ValueError(
                    f"{start_name} must be less than {end_name}. Got {start} and {end}.")

        validation_tuples = [
            # ('activity_type', ACTIVITY_TYPES),
            ('exposed_activity_type', self.activities),
            ('infected_activity_type', self.activities),
            ('exposed_coffee_break_option', COFFEE_OPTIONS_INT),
            ('infected_coffee_break_option', COFFEE_OPTIONS_INT),
            ('mechanical_ventilation_type', MECHANICAL_VENTILATION_TYPES),
            ('mask_type', MASK_TYPES),
            ('mask_wearing_option', MASK_WEARING_OPTIONS),
            ('ventilation_type', VENTILATION_TYPES),
            ('virus_type', VIRUS_TYPES),
            ('volume_type', VOLUME_TYPES),
            ('window_opening_regime', WINDOWS_OPENING_REGIMES),
            ('window_type', WINDOWS_TYPES),
            ('event_month', self.MONTHS)]
        for attr_name, valid_set in validation_tuples:
            if getattr(self, attr_name) not in valid_set:
                raise ValueError(f"{getattr(self, attr_name)} is not a valid value for {attr_name}")

        if self.ventilation_type == 'natural_ventilation':
            if self.window_type == 'not-applicable':
                raise ValueError(
                    "window_type cannot be 'not-applicable' if "
                    "ventilation_type is 'natural_ventilation'"
                )
            if self.window_opening_regime == 'not-applicable':
                raise ValueError(
                    "window_opening_regime cannot be 'not-applicable' if "
                    "ventilation_type is 'natural_ventilation'"
                )

        if (self.ventilation_type == 'mechanical_ventilation' 
                and self.mechanical_ventilation_type == 'not-applicable'):
            raise ValueError("mechanical_ventilation_type cannot be 'not-applicable' if "
                             "ventilation_type is 'mechanical_ventilation'")

    def build_mc_model(self) -> mc.ExposureModel:
        # Initializes room with volume either given directly or as product of area and height
        if self.volume_type == 'room_volume_explicit':
            volume = self.room_volume
        else:
            volume = self.floor_area * self.ceiling_height
        if self.humidity == '':
            if self.room_heating_option:
                humidity = 0.3
            else:
                humidity = 0.5
        else:
            humidity = float(self.humidity)
        room = models.Room(volume=volume, inside_temp=models.PiecewiseConstant((0, 24), (self.inside_temp+273,)), humidity=humidity)
        # Initializes and returns a model with the attributes defined above
        return mc.ExposureModel(
            concentration_model=mc.ConcentrationModel(
                room=room,
                ventilation=self.ventilation(),
                infected=self.infected_population(),
                evaporation_factor=0.3,
            ),
            exposed=self.exposed_population(),
        )
        

    def build_model(self, sample_size=_DEFAULT_MC_SAMPLE_SIZE) -> models.ExposureModel:
        return self.build_mc_model().build_model(size=sample_size)

    def tz_name_and_utc_offset(self) -> typing.Tuple[str, float]:
        """
        Return the timezone name (e.g. CET), and offset, in hours, that need to
        be *added* to UTC to convert to the form location's timezone.

        """
        month = self.MONTHS.index(self.event_month) + 1
        timezone = farc.data.weather.timezone_at(
            latitude=self.location_latitude, longitude=self.location_longitude,
        )
        # We choose the first of the month for the current year.
        date = datetime.datetime(datetime.datetime.now().year, month, 1)
        name = timezone.tzname(date)
        assert isinstance(name, str)
        utc_offset_td = timezone.utcoffset(date)
        assert isinstance(utc_offset_td, datetime.timedelta)
        utc_offset_hours = utc_offset_td.total_seconds() / 60 / 60
        return name, utc_offset_hours

    def outside_temp(self) -> models.PiecewiseConstant:
        """
        Return the outside temperature as a PiecewiseConstant in the destination
        timezone.
    
        """

        month = self.MONTHS.index(self.event_month) + 1

        wx_station = self.nearest_weather_station()
        temp_profile = farc.data.weather.mean_hourly_temperatures(wx_station[0], month)

        _, utc_offset = self.tz_name_and_utc_offset()

        # Offset the source times according to the difference from UTC (as a
        # result the first data value may no longer be a midnight, and the hours
        # no longer ordered modulo 24).
        source_times = np.arange(24) + utc_offset
        times, temp_profile = farc.data.weather.refine_hourly_data(
            source_times,
            temp_profile,
            npts=24*10,  # 10 steps per hour => 6 min steps
        )
        outside_temp = models.PiecewiseConstant(
            tuple(float(t) for t in times), tuple(float(t) for t in temp_profile),
        )
        return outside_temp

    def ventilation(self) -> models._VentilationBase:
        always_on = models.PeriodicInterval(period=120, duration=120)
        # Initializes a ventilation instance as a window if 'natural_ventilation' is selected, or as a BIOV-filter otherwise
        # If natural_ventilation and windows_open_periodically are selected, windows will be open during lunch and coffee breaks
        
        if self.ventilation_type == 'natural_ventilation':
            if self.window_opening_regime == 'windows_open_periodically':
                window_interval_boundaries = models.PeriodicInterval(self.windows_frequency, self.windows_duration, min(self.infected_start, self.exposed_start)/60).boundaries() 
                breaks_interval_boundaries = self.exposed_lunch_break_times()+self.infected_lunch_break_times()+self.exposed_coffee_break_times()
                for t1, t2 in breaks_interval_boundaries : 
                        window_interval_boundaries = window_interval_boundaries + ((t1/60, t2/60),)

                window_interval = models.SpecificInterval(window_interval_boundaries)

            else:
                window_interval = always_on

            outside_temp = self.outside_temp()
            inside_temp = models.PiecewiseConstant((0, 24), (self.inside_temp+273,))

            ventilation: models.Ventilation
            if self.window_type == 'window_sliding':
                ventilation = models.SlidingWindow(
                    active=window_interval,
                    inside_temp=inside_temp,
                    outside_temp=outside_temp,
                    window_height=self.window_height,
                    opening_length=self.opening_distance,
                    number_of_windows=self.windows_number,
                )
            elif self.window_type == 'window_hinged':
                ventilation = models.HingedWindow(
                    active=window_interval,
                    inside_temp=inside_temp,
                    outside_temp=outside_temp,
                    window_height=self.window_height,
                    window_width=self.window_width,
                    opening_length=self.opening_distance,
                    number_of_windows=self.windows_number,
                )

        elif self.ventilation_type == 'no_ventilation':
            ventilation = models.AirChange(active=always_on, air_exch=0.)
        else:
            if self.mechanical_ventilation_type == 'mech_type_air_changes':
                ventilation = models.AirChange(active=always_on, air_exch=self.air_changes)
            else:
                ventilation = models.HVACMechanical(
                    active=always_on, q_air_mech=self.air_supply)

        # this is a minimal, always present source of ventilation, due
        # to the air infiltration from the outside.
        # See CERN-OPEN-2021-004, p. 12.
        infiltration_ventilation = models.AirChange(active=always_on, air_exch=0.25)
        if self.biov_option == 1:
            biov = models.BIOVFilter(active=always_on, q_air_mech=self.biov_amount)
            return models.MultipleVentilation((ventilation, biov, infiltration_ventilation))
        else:
            return models.MultipleVentilation((ventilation, infiltration_ventilation))

    def nearest_weather_station(self) -> farc.data.weather.WxStationRecordType:
        """Return the nearest weather station (which has valid data) for this form"""
        return farc.data.weather.nearest_wx_station(
            longitude=self.location_longitude, latitude=self.location_latitude
        )

    def mask(self) -> models.Mask:
        # Initializes the mask type if mask wearing is "continuous", otherwise instantiates the mask attribute as
        # the "No mask"-mask
        if self.mask_wearing_option == 'mask_on':
            mask = mask_distributions[self.mask_type]
        else:
            mask = models.Mask.types['No mask']
        return mask

    def infected_population(self) -> mc.InfectedPopulation:
        # Initializes the virus
        virus = virus_distributions[self.virus_type]
        activity = activity_distributions[self.infected_activity_level]
        expiration = build_expiration({'Breathing' : self.infected_breathing, 'Speaking' : self.infected_speaking, 'Shouting' : self.infected_shouting})

        infected_occupants = self.infected_people

        infected = mc.InfectedPopulation(
            number=infected_occupants,
            virus=virus,
            presence=self.infected_present_interval(),
            mask=self.mask(),
            mask_wear_ratio=self.infected_mask_wear_ratio,
            activity=activity,
            expiration=expiration,
            host_immunity=0.,
        )
        return infected

    def exposed_population(self) -> mc.Population:
        
        activity = activity_distributions[self.exposed_activity_level]

        infected_occupants = self.infected_people
        # The number of exposed occupants is the total number of occupants
        # minus the number of infected occupants.
        exposed_occupants = self.total_people - infected_occupants

        exposed = mc.Population(
            number=exposed_occupants,
            presence=self.exposed_present_interval(),
            activity=activity,
            mask=self.mask(),
            mask_wear_ratio=self.exposed_mask_wear_ratio,
            host_immunity=0.,
        )
        return exposed

    def _compute_breaks_in_interval(self, start, finish, n_breaks, duration) -> models.BoundarySequence_t:
        break_delay = ((finish - start) - (n_breaks * duration)) // (n_breaks+1)
        break_times = []
        end = start
        for n in range(n_breaks):
            begin = end + break_delay
            end = begin + duration
            break_times.append((begin, end))
        return tuple(break_times)

    def exposed_lunch_break_times(self) -> models.BoundarySequence_t:
        result = []
        if self.exposed_lunch_option ==1:
            result.append((self.exposed_lunch_start, self.exposed_lunch_finish))
        return tuple(result)

    def infected_lunch_break_times(self) -> models.BoundarySequence_t:
        if self.infected_dont_have_breaks_with_exposed==1:
            result = []
            if self.infected_lunch_option == 1:
                result.append((self.infected_lunch_start, self.infected_lunch_finish))
            return tuple(result)
        else:
            return self.exposed_lunch_break_times()

    def exposed_number_of_coffee_breaks(self) -> int:
        return COFFEE_OPTIONS_INT[self.exposed_coffee_break_option]

    def infected_number_of_coffee_breaks(self) -> int:
        return COFFEE_OPTIONS_INT[self.infected_coffee_break_option]

    def _coffee_break_times(self, activity_start, activity_finish, coffee_breaks, coffee_duration, lunch_start, lunch_finish) -> models.BoundarySequence_t:
        time_before_lunch = lunch_start - activity_start
        time_after_lunch = activity_finish - lunch_finish
        before_lunch_frac = time_before_lunch / (time_before_lunch + time_after_lunch)
        n_morning_breaks = round(coffee_breaks * before_lunch_frac)
        breaks = (
            self._compute_breaks_in_interval(
                activity_start, lunch_start, n_morning_breaks, coffee_duration
            )
            + self._compute_breaks_in_interval(
                lunch_finish, activity_finish, coffee_breaks - n_morning_breaks, coffee_duration
            )
        )
        return breaks

    def exposed_coffee_break_times(self) -> models.BoundarySequence_t:
        exposed_coffee_breaks = self.exposed_number_of_coffee_breaks()
        if exposed_coffee_breaks == 0:
            return ()
        if self.exposed_lunch_option == 1:
            breaks = self._coffee_break_times(self.exposed_start, self.exposed_finish, exposed_coffee_breaks, self.exposed_coffee_duration, self.exposed_lunch_start, self.exposed_lunch_finish)
        else:
            breaks = self._compute_breaks_in_interval(self.exposed_start, self.exposed_finish, exposed_coffee_breaks, self.exposed_coffee_duration)
        return breaks

    def infected_coffee_break_times(self) -> models.BoundarySequence_t:
        if self.infected_dont_have_breaks_with_exposed==1:
            infected_coffee_breaks = self.infected_number_of_coffee_breaks()
            if infected_coffee_breaks == 0:
                return ()
            if self.infected_lunch_option == 1:
                breaks = self._coffee_break_times(self.infected_start, self.infected_finish, infected_coffee_breaks, self.infected_coffee_duration, self.infected_lunch_start, self.infected_lunch_finish)
            else:
                breaks = self._compute_breaks_in_interval(self.infected_start, self.infected_finish, infected_coffee_breaks, self.infected_coffee_duration)
            return breaks
        else:
            return self.exposed_coffee_break_times()

    def present_interval(
            self,
            start: int,
            finish: int,
            breaks: typing.Optional[models.BoundarySequence_t] = None,
    ) -> models.Interval:
        """
        Calculate the presence interval given the start and end times (in minutes), and
        a number of monotonic, non-overlapping, but potentially unsorted, breaks (also in minutes).

        """
        if not breaks:
            # If there are no breaks, the interval is the start and end.
            return models.SpecificInterval(((start/60, finish/60),))

        # Order the breaks by their start-time, and ensure that they are monotonic
        # and that the start of one break happens after the end of another.
        break_boundaries: models.BoundarySequence_t = tuple(sorted(breaks, key=lambda break_pair: break_pair[0]))

        for break_start, break_end in break_boundaries:
            if break_start >= break_end:
                raise ValueError("Break ends before it begins.")

        prev_break_end = break_boundaries[0][1]
        for break_start, break_end in break_boundaries[1:]:
            if prev_break_end >= break_start:
                raise ValueError(f"A break starts before another ends ({break_start}, {break_end}, {prev_break_end}).")
            prev_break_end = break_end

        present_intervals = []

        # def add_interval(start, end):

        current_time = start
        LOG.debug(f"starting time march at {_hours2timestring(current_time/60)} to {_hours2timestring(finish/60)}")

        # As we step through the breaks. For each break there are 6 important cases
        # we must cover. Let S=start; E=end; Bs=Break start; Be=Break end:
        #  1. The interval is entirely before the break. S < E <= Bs < Be
        #  2. The interval straddles the start of the break. S < Bs < E <= Be
        #  3. The break is entirely inside the interval. S < Bs < Be <= E
        #  4. The interval is entirely inside the break. Bs <= S < E <= Be
        #  5. The interval straddles the end of the break. Bs <= S < Be <= E
        #  6. The interval is entirely after the break. Bs < Be <= S < E

        for current_break in break_boundaries:
            if current_time >= finish:
                break

            LOG.debug(f"handling break {_hours2timestring(current_break[0]/60)}-{_hours2timestring(current_break[1]/60)} "
                      f" (current time: {_hours2timestring(current_time/60)})")

            break_s, break_e = current_break
            case1 = finish <= break_s
            case2 = current_time < break_s < finish < break_e
            case3 = current_time < break_s < break_e <= finish
            case4 = break_s <= current_time < finish <= break_e
            case5 = break_s <= current_time < break_e < finish
            case6 = break_e <= current_time

            if case1:
                LOG.debug(f"case 1: interval entirely before break")
                present_intervals.append((current_time / 60, finish / 60))
                LOG.debug(f" + added interval {_hours2timestring(present_intervals[-1][0])} "
                          f"- {_hours2timestring(present_intervals[-1][1])}")
                current_time = finish
            elif case2:
                LOG.debug(f"case 2: interval straddles start of break")
                present_intervals.append((current_time / 60, break_s / 60))
                LOG.debug(f" + added interval {_hours2timestring(present_intervals[-1][0])} "
                          f"- {_hours2timestring(present_intervals[-1][1])}")
                current_time = break_e
            elif case3:
                LOG.debug(f"case 3: break entirely inside interval")
                # We add the bit before the break, but not the bit afterwards,
                # as it may hit another break.
                present_intervals.append((current_time / 60, break_s / 60))
                LOG.debug(f" + added interval {_hours2timestring(present_intervals[-1][0])} "
                          f"- {_hours2timestring(present_intervals[-1][1])}")
                current_time = break_e
            elif case4:
                LOG.debug(f"case 4: interval entirely inside break")
                current_time = finish
            elif case5:
                LOG.debug(f"case 5: interval straddles end of break")
                current_time = break_e
            elif case6:
                LOG.debug(f"case 6: interval entirely after the break")

        if current_time < finish:
            LOG.debug("trailing interval")
            present_intervals.append((current_time / 60, finish / 60))
        return models.SpecificInterval(tuple(present_intervals))

    def infected_present_interval(self) -> models.Interval:
        return self.present_interval(
            self.infected_start, self.infected_finish,
            breaks=self.infected_lunch_break_times() + self.infected_coffee_break_times(),
        )

    def exposed_present_interval(self) -> models.Interval:
        return self.present_interval(
            self.exposed_start, self.exposed_finish,
            breaks=self.exposed_lunch_break_times() + self.exposed_coffee_break_times(),
        )


def build_expiration(expiration_definition) -> models._ExpirationBase:
    if isinstance(expiration_definition, str):
        return expiration_distributions[expiration_definition]
    elif isinstance(expiration_definition, dict):
        total_weight = sum(expiration_definition.values())
        BLO_factors = np.sum([
            np.array(expiration_BLO_factors[exp_type]) * weight/total_weight
            for exp_type, weight in expiration_definition.items()
            ], axis=0)
        return expiration_distribution(tuple(BLO_factors))


def baseline_raw_form_data():
    # Note: This isn't a special "baseline". It can be updated as required.
    return d


def _hours2timestring(hours: float):
    # Convert times like 14.5 to strings, like "14:30"
    return f"{int(np.floor(hours)):02d}:{int(np.round((hours % 1) * 60)):02d}"


def time_string_to_minutes(time: str) -> minutes_since_midnight:
    """
    Converts time from string-format to an integer number of minutes after 00:00
    :param time: A string of the form "HH:MM" representing a time of day
    :return: The number of minutes between 'time' and 00:00
    """
    return minutes_since_midnight(60 * int(time[:2]) + int(time[3:]))


def time_minutes_to_string(time: int) -> str:
    """
    Converts time from an integer number of minutes after 00:00 to string-format
    :param time: The number of minutes between 'time' and 00:00
    :return: A string of the form "HH:MM" representing a time of day
    """
    return "{0:0=2d}".format(int(time/60)) + ":" + "{0:0=2d}".format(time%60)


def _safe_int_cast(value) -> int:
    if isinstance(value, int):
        return value
    elif isinstance(value, float) and int(value) == value:
        return int(value)
    elif isinstance(value, str) and value.isdecimal():
        return int(value)
    else:
        raise TypeError(f"Unable to safely cast {value} ({type(value)} type) to int")


#: Mapping of field name to a callable which can convert values from form
#: input (URL encoded arguments / string) into the correct type.
_CAST_RULES_FORM_ARG_TO_NATIVE: typing.Dict[str, typing.Callable] = {}

#: Mapping of field name to callable which can convert native type to values
#: that can be encoded to URL arguments.
_CAST_RULES_NATIVE_TO_FORM_ARG: typing.Dict[str, typing.Callable] = {}


for _field in dataclasses.fields(FormData):
    if _field.type is minutes_since_midnight:
        _CAST_RULES_FORM_ARG_TO_NATIVE[_field.name] = time_string_to_minutes
        _CAST_RULES_NATIVE_TO_FORM_ARG[_field.name] = time_minutes_to_string
    elif _field.type is int:
        _CAST_RULES_FORM_ARG_TO_NATIVE[_field.name] = _safe_int_cast
    elif _field.type is float:
        _CAST_RULES_FORM_ARG_TO_NATIVE[_field.name] = float
    elif _field.type is bool:
        _CAST_RULES_FORM_ARG_TO_NATIVE[_field.name] = lambda v: v == '1'
        _CAST_RULES_NATIVE_TO_FORM_ARG[_field.name] = int
