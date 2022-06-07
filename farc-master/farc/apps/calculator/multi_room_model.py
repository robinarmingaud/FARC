from dataclasses import dataclass
from re import I
import numpy as np

from farc import models


@dataclass
class Building:
    name:str

@dataclass
class Ventilation:
    
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
    air_supply: float
    biov_amount: float
    biov_option: int

    def ventilation(self) -> models._VentilationBase:
        #FormData ventilation function
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
            inside_temp = models.PiecewiseConstant((0, 24), (293,))

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
class Action:
    expiration : models._ExpirationBase
    activity : models.Activity

@dataclass
class Mask:
    type: str
    ratio: float = 0

    def is_worn(self) : 
        return self.ratio > 0

@dataclass
class Event:
    start : int
    end : int
    location : RoomType
    mask : Mask
    activity : Action

@dataclass
class Schedule:
    events = np.ndarray = np.array([], dtype= Event)

    def add_event(self, event):
        self.events = np.append(self.events, event)
    
    def get_event_id(self, event):
        i=0
        for element in self.events :
            if element == event :
                return i
            i += 1

    def delete_event(self, event):
        self.events = np.delete(self.events, self.get_event_id(event))

    def get_boundaries(self):
        start = self.events[0].start
        end = 0
        for event in self.events :
            if event.start < start :
                start = event.start
            if event.end > end :
                end = event.end
        return start,end 


@dataclass
class Person(Role):
    id:int 
    infected: bool
    cumulative_dose: float = 0
    location: RoomType = None
    schedule = Schedule

    def __init__(self, name : str, id:int, infected: bool, cumulative_dose: float = 0, location: RoomType = None):
        self.id = id
        self.name = name
        self.infected = infected
        self.cumulative_dose = cumulative_dose
        self.location = location
        if self.location is not None:
            self.location.add_occupant(self)


    def set_location(self, room: RoomType) : 
        if self.location is not None:
            self.location.delete_occupant(self)
        room.add_occupant(self)
        self.location = room


@dataclass
class Room(RoomType):
    id:int
    humidity:float
    temperature : float
    occupants: np.ndarray = np.array([], dtype= Person)
    building: Building = None

    def get_occupant_id(self, person : Person):
        i=0
        for element in self.occupants :
            if element == person :
                return i
            i += 1

    def set_building(self, building : Building):
        self.building = building

    def add_occupant(self, occupant : Person):
        self.occupants = np.append(self.occupants, occupant)
        occupant.location = self

    def delete_occupant(self, occupant: Person):
        self.occupants = np.delete(self.occupants, self.get_occupant_id(occupant))
        occupant.location = None




#tests
room1 = Room(id = 1, humidity = 0.4, type_name = 'Office1', volume = 30, ventilation= models.PeriodicInterval(period=120, duration=120))

person_test = Person(id=1, infected = False, name = 'Office_worker')
