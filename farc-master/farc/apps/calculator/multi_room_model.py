import os
import tornado


from dataclasses import dataclass, field
import datetime
import typing
import numpy as np

import numpy as np

import farc.data.weather
from farc.apps.calculator import model_generator
from farc import models
import farc.monte_carlo as mc
from farc.monte_carlo.data import activity_distributions, virus_distributions, mask_distributions
from farc.monte_carlo.data import expiration_distribution, expiration_BLO_factors, expiration_distributions
from .DEFAULT_DATA import ACTIVITY_TYPES, MONTH_NAMES
from farc import data
from farc.apps.calculator.model_generator import time_string_to_minutes

from .DEFAULT_DATA import _DEFAULTS as default, _MULTI_DEFAULTS as multi_default


path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'locale'))

tornado.locale.load_gettext_translations(path , 'messages')
locale = tornado.locale.get()
_ = locale.translate

@dataclass
class Building:
    name:str

@dataclass
class Ventilation:
    inside_temp: float = multi_default['inside_temp']
    ventilation_type : str = multi_default['ventilation_type']
    windows_duration: float = multi_default['windows_duration']
    windows_frequency: float = multi_default['windows_frequency']
    window_height: float = multi_default['window_height']
    window_type: str = multi_default['window_type']
    window_width: float = multi_default['window_width']
    windows_number: int = multi_default['windows_number']
    window_opening_regime: str = multi_default['window_opening_regime']
    opening_distance: float = multi_default['opening_distance']
    room_heating_option: int = multi_default['room_heating_option']
    mechanical_ventilation_type: str = multi_default['mechanical_ventilation_type']
    air_supply: float = multi_default['air_supply']
    air_changes: float = multi_default['air_changes'],
    biov_amount: float = multi_default['biov_amount']
    biov_option: int = multi_default['biov_option']

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
        month = list(MONTH_NAMES.keys()).index(simulation.event_month) + 1
        timezone = farc.data.weather.timezone_at(latitude=simulation.location_latitude, longitude=simulation.location_longitude)
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

        

        month = list(MONTH_NAMES.keys()).index(simulation.event_month) + 1

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
                window_interval = models.PeriodicInterval(self.windows_frequency, self.windows_duration)
                
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
    type_name:str = multi_default['type_name']
    room_volume:int = multi_default['volume']
    ventilation: Ventilation = Ventilation()

@dataclass
class Role:
    name: str = multi_default['name']

@dataclass
class Event:
    event_mask_wearing_option : str = multi_default['event_mask_wearing_option']
    event_activity_level : str = multi_default['event_activity_level']
    event_activity_breathing : float = multi_default['event_activity_breathing']
    event_activity_speaking : float = multi_default['event_activity_speaking']
    event_activity_shouting : float = multi_default['event_activity_shouting']
    start : float = time_string_to_minutes(multi_default['start'])/60
    end : float = time_string_to_minutes(multi_default['end'])/60
    location : RoomType = RoomType()
    mask_ratio : float = multi_default['mask_ratio']
    mask_type : str = multi_default['mask_type']
    activity : str = multi_default['activity']
    description : str = ""

    def get_event_duration(self):
        return self.end-self.start

@dataclass
class Schedule:
    events : np.ndarray = np.array([])
    def add_event(self, event):
        if self.events.size == 0 :
            self.events = np.append(self.events, event)
        else :
            i = 0
            for element in self.events :
                if element.start > event.start :
                    self.events = np.insert(self.events, i, event)
                    return
                else :
                    i+=1
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
    person_number: int = multi_default['people_number']
    person_name : str = multi_default['name']
    id:int = multi_default['person_id']
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

    def exposed_population(self, time1, time2, number):
        activity = activity_distributions[self.current_event.event_activity_level]

        exposed = mc.Population(
            number=number,
            presence= models.SpecificInterval(((time1, time2),)),
            activity= activity,
            mask=self.mask(),
            mask_wear_ratio=self.current_event.mask_ratio,
            host_immunity=0.,
        )
        return exposed

    def calculate_data(self):
        if (not self.infected or self.person_number>1) and len(self.exposure_model)>0 :
            total_dose : models._VectorisedFloat = 0
            for model in self.exposure_model :
                deposited_exposure = model.deposited_exposure()
                if np.mean(deposited_exposure)*self.person_number < 0.1 and len(self.exposure_model) > 1 :
                    # Delete neglectable models
                    self.get_location().concentration_models = np.delete(self.get_location().concentration_models, np.where(self.get_location().concentration_models==model.concentration_model))
                    self.exposure_model = np.delete(self.exposure_model, np.where(self.exposure_model == model))
                else :
                    virus_dose = np.sort(deposited_exposure)
                    self.cumulative_dose = self.cumulative_dose + virus_dose
                    total_dose = total_dose + virus_dose
            self.virus_dose = total_dose
        else :
            self.virus_dose = 0

    def calculate_infection_probability(self, virus):
            if not self.infected :
                self.infection_probability = np.mean(infection_probability(self.cumulative_dose, virus))*self.person_number
                self.cumulative_dose = np.mean(self.cumulative_dose)
            elif self.person_number>1 :
                self.infection_probability = np.mean(infection_probability(self.cumulative_dose, virus))*(self.person_number-1)
                self.cumulative_dose = np.mean(self.cumulative_dose)
            else : 
                return 0.



    def add_model(self, model : models.ExposureModel):
        self.exposure_model = np.append(self.exposure_model, model)

    def clear_data(self):
        self.exposure_model = []
        self.virus_dose = 0




@dataclass
class Room(RoomType):
    id:int = multi_default['room_id']
    humidity:float = multi_default['humidity']
    number: str = multi_default['room_number']
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
        room = models.Room(volume = self.room_volume,humidity = self.humidity)
        ventilation = self.ventilation.ventilation(simulation)
        if infected.get_location() and infected.get_location().id == self.id:
            infected_population = infected.infected_population(simulation, time1, time2)
            self.concentration_models = np.append(self.concentration_models, mc.ConcentrationModel(
                room=room,
                ventilation=ventilation,
                infected=infected_population,
                evaporation_factor=0.3,
            ).build_model(size=60000))
        for person in self.get_occupants(simulation) :
            person.clear_data()
            if person.infected and person.person_number>1 : 
                exposed_population = person.exposed_population(time1, time2, person.person_number-1)
                for model in self.concentration_models :
                    person.add_model(mc.ExposureModel(model, exposed_population).build_model(size=60000))
            elif not person.infected :
                exposed_population = person.exposed_population(time1, time2, person.person_number)
                for model in self.concentration_models :
                    person.add_model(mc.ExposureModel(model, exposed_population).build_model(size=60000))

    def calculate_cumulative_dose(self):
        self.cumulative_exposure = np.mean(self.cumulative_exposure)
        self.virus_concentration = np.mean(self.virus_concentration)

    def clear_data(self):
        self.concentration_models=[]

    
@dataclass
class Simulation:
    simulation_name : str = ""
    event_month: str = multi_default['event_month']
    virus_type : str = multi_default['virus_type']
    location_name: str = multi_default['location_name']
    location_latitude: float = multi_default['location_latitude']
    location_longitude: float = multi_default['location_longitude']
    rooms: np.ndarray = np.array([])
    people: np.ndarray = np.array([])

    def get_room_by_id(self, id: int):
        for room in self.rooms :
            if room.id == id :
                return room

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

def infection_probability(viral_dose, virus):
    oneoverln2 = 1 / np.log(2)
    infectious_dose = oneoverln2 * virus.infectious_dose

        # Probability of infection.
    return (1 - np.exp(-(viral_dose / (infectious_dose *virus.transmissibility_factor)))) 