from dataclasses import dataclass, field
import datetime
import typing
import numpy as np

import numpy as np

from farc.apps.calculator import model_generator
from farc import models
import farc.monte_carlo as mc
from farc.monte_carlo.data import activity_distributions, virus_distributions, mask_distributions
from farc.monte_carlo.data import expiration_distribution, expiration_BLO_factors, expiration_distributions
from .DEFAULT_DATA import ACTIVITY_TYPES, MONTH_NAMES
from farc import data

@dataclass
class Building:
    name:str

@dataclass
class Ventilation:
    inside_temp: float
    ventilation_type : str
    windows_duration: float
    windows_frequency: float
    window_height: float
    window_type: str
    window_width: float
    windows_number: int
    window_opening_regime: str
    opening_distance: float
    event_month: str
    room_heating_option: int
    mechanical_ventilation_type: str
    air_supply: float
    biov_amount: float
    biov_option: int

    def nearest_weather_station(self, simulation) -> data.weather.WxStationRecordType:
        """Return the nearest weather station (which has valid data) for this form"""
        return data.weather.nearest_wx_station(
            longitude=simulation.location_longitude, latitude=simulation.location_latitude
        )

    def tz_name_and_utc_offset(self, simulation) -> typing.Tuple[str, float]:
        """
        Return the timezone name (e.g. CET), and offset, in hours, that need to
        be *added* to UTC to convert to the form location's timezone.

        """
        month = list(MONTH_NAMES.keys()).index(self.event_month) + 1
        timezone = data.weather.timezone_at(
            latitude=simulation.location_latitude, longitude=simulation.location_longitude,
        )
        # We choose the first of the month for the current year.
        date = datetime.datetime(datetime.datetime.now().year, month, 1)
        name = timezone.tzname(date)
        assert isinstance(name, str)
        utc_offset_td = timezone.utcoffset(date)
        assert isinstance(utc_offset_td, datetime.timedelta)
        utc_offset_hours = utc_offset_td.total_seconds() / 60 / 60
        return name, utc_offset_hours


    def outside_temp(self, simulation) -> models.PiecewiseConstant:
        """
        Return the outside temperature as a PiecewiseConstant in the destination
        timezone.
    
        """

        month = list(MONTH_NAMES.keys()).index(self.event_month) + 1

        wx_station = self.nearest_weather_station(simulation)
        temp_profile = data.weather.mean_hourly_temperatures(wx_station[0], month)

        _, utc_offset = self.tz_name_and_utc_offset(simulation)

        # Offset the source times according to the difference from UTC (as a
        # result the first data value may no longer be a midnight, and the hours
        # no longer ordered modulo 24).
        source_times = np.arange(24) + utc_offset
        times, temp_profile = data.weather.refine_hourly_data(
            source_times,
            temp_profile,
            npts=24*10,  # 10 steps per hour => 6 min steps
        )
        outside_temp = models.PiecewiseConstant(
            tuple(float(t) for t in times), tuple(float(t) for t in temp_profile),
        )
        return outside_temp


    def ventilation(self, simulation) -> models._VentilationBase:
        """FormData ventilation function from CARA model"""
        always_on = models.PeriodicInterval(period=120, duration=120)
        # Initializes a ventilation instance as a window if 'natural_ventilation' is selected, or as a BIOV-filter otherwise
        # If natural_ventilation and windows_open_periodically are selected, windows will be open during lunch and coffee breaks
        
        if self.ventilation_type == 'natural_ventilation':
            if self.window_opening_regime == 'windows_open_periodically':
                window_interval_boundaries = models.PeriodicInterval(self.windows_frequency, self.windows_duration, min(self.infected_start, self.exposed_start)/60).boundaries() 
                window_interval = models.SpecificInterval(window_interval_boundaries)

            else:
                window_interval = always_on

            outside_temp = self.outside_temp(simulation)
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


@dataclass
class RoomType:
    type_name:str
    volume:int
    ventilation: Ventilation

@dataclass
class Role:
    name: str

@dataclass
class Event:
    event_mask_wearing_option : str
    event_activity_level : str
    event_activity_breathing : float
    event_activity_speaking : float
    event_activity_shouting : float
    start : int
    end : int
    location : RoomType
    mask_ratio : float
    mask_type : str
    activity : str

@dataclass
class Schedule:
    events : np.ndarray = np.array([])
    def add_event(self, event):
        self.events = np.append(self.events, event)
    
    def get_event_id(self, event):
        i=0
        for element in self.events :
            if element == event :
                return i
            i += 1

    def delete_event(self, event):
        self.events.pop(self.get_event_id(event))

    def get_boundaries(self):
        start = self.events[0].start
        end = 0
        for event in self.events :
            if event.start < start :
                start = event.start
            if event.end > end :
                end = event.end
        return start,end 

    def get_event_by_time(self, time):
        for event in self.events:
            if event.start <= time and event.end > time :
                return event
        raise ValueError


@dataclass
class Person(Role):
    number: int
    name : str
    id:int 
    schedule : Schedule = Schedule()
    exposure_model : np.ndarray = np.array([])
    infected: bool = False
    cumulative_dose:  models._VectorisedFloat = 0.
    current_event: Event = None
    infection_probability : float = 0
    virus_dose : models._VectorisedFloat = 0.



    def get_location(self) : 
        if self.current_event : 
            return self.current_event.location
        else :
            return None

    def set_event(self, event: Event):
        self.current_event = event

    def mask(self) -> models.Mask:
    # Initializes the mask type if mask wearing is "continuous", otherwise instantiates the mask attribute as
    # the "No mask"-mask
    # Adaptation from FormData mask method
        if self.current_event.event_mask_wearing_option == 'mask_on' :
            mask = mask_distributions[self.current_event.mask_type]
        else:
            mask = models.Mask.types['No mask']
        return mask

    def infected_population(self, simulation, time1, time2):
        """Adaptation of infected population from model_generator"""
        virus = virus_distributions[simulation.virus_type]
        activity = activity_distributions[self.current_event.event_activity_level]
        expiration = build_expiration({'Breathing' : self.current_event.event_activity_breathing, 'Speaking' : self.current_event.event_activity_speaking, 'Shouting' : self.current_event.event_activity_shouting})
        return mc.InfectedPopulation(
            number=1,
            virus=virus,
            presence= models.SpecificInterval(((time1, time2),)),
            mask=self.mask(),
            mask_wear_ratio=self.current_event.mask_ratio,
            activity=activity,
            expiration=expiration,
            host_immunity=0.,)

    def exposed_population(self, time1, time2):
        activity = activity_distributions[self.current_event.event_activity_level]

        exposed = mc.Population(
            number=1,
            presence= models.SpecificInterval(((time1, time2),)),
            activity= activity,
            mask=self.mask(),
            mask_wear_ratio=self.current_event.mask_ratio,
            host_immunity=0.,
        )
        return exposed

    def calculate_data(self):
        if not self.infected and self.exposure_model :
            total_dose : models._VectorisedFloat = 0
            for model in self.exposure_model :
                virus_dose = np.sort(model.deposited_exposure())
                self.cumulative_dose = self.cumulative_dose + virus_dose
                total_dose = total_dose + virus_dose
            self.virus_dose = total_dose
        else :
            self.virus_dose = 0

    def calculate_infection_probability(self):
        if not self.infected and self.exposure_model :
            self.infection_probability = np.round(np.mean(self.exposure_model[0]._dose_infection_probability(self.cumulative_dose))/100, 4)
            self.cumulative_dose = np.round(np.mean(self.cumulative_dose), 2)
        else :
            return 0.

    def add_model(self, model : models.ExposureModel):
        self.exposure_model = np.append(self.exposure_model, model)

    def clear_data(self):
        self.exposure_model = []
        self.virus_dose = 0




@dataclass
class Room(RoomType):
    id:int
    humidity:float
    number : int = 1
    #All concentration models from infected people who went to this room and left virus particles
    concentration_models: np.ndarray = np.array([])
    virus_concentration: models._VectorisedFloat = 0.
    cumulative_exposure: models._VectorisedFloat = 0.
    

    def set_building(self, building : Building):
        self.building = building

    def get_occupants(self, simulation):
        occupants = np.array([])
        for person in simulation.people :
            if person.get_location() == self :
                occupants = np.append(occupants , person)

        return occupants

    def build_model(self, infected : Person, simulation, time1 : int, time2: int):
        room = models.Room(volume = self.volume,humidity = self.humidity)
        ventilation = self.ventilation.ventilation(simulation)
        if infected.get_location() and infected.get_location().id == self.id:
            infected_population = infected.infected_population(simulation, time1, time2)
            self.concentration_models = np.append(self.concentration_models, mc.ConcentrationModel(
                room=room,
                ventilation=ventilation,
                infected=infected_population,
                evaporation_factor=0.3,
            ))
        for person in self.get_occupants(simulation) :
            person.clear_data()
            exposed_population = person.exposed_population(time1, time2)
            for model in self.concentration_models :
                person.add_model(mc.ExposureModel(model, exposed_population).build_model(size=60000))

    def calculate_cumulative_dose(self):
        self.cumulative_exposure = np.round(np.mean(self.cumulative_exposure), 2)
        self.virus_concentration = np.round(np.mean(self.virus_concentration), 2)

    def clear_data(self):
        self.concentration_models=[]

    
@dataclass
class Simulation:
    virus_type : str
    location_name: str = "Nantes, Loire-Atlantique, Pays de la Loire, FRA"
    location_latitude: float = 47.21725
    location_longitude: float = -1.55336
    rooms: np.ndarray = np.array([])
    people: np.ndarray = np.array([])

    def get_room_id(self, room : Room):
        i=0
        for element in self.rooms :
            if element == room :
                return i
            i += 1

    def add_room(self, room : Room): 
        self.rooms = np.append(self.rooms, room)

    def delete_room(self, room : Room):
        self.rooms.pop(self.get_room_id(room))


    def get_person_id(self, person : Person):
        i=0
        for element in self.people :
            if element == person :
                return i
            i += 1

    def add_person(self, person : Person):
        self.people = np.append(self.people, person)

    def delete_person(self, person: Person):
        self.people.pop(self.get_person_id(person))

    def get_infected(self):
        for person in self.people:
            if person.infected:
                return person
        

@dataclass
class Report:
    simulations: np.ndarray = np.array([])

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