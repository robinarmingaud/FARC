from dataclasses import dataclass, field
import numpy as np

import numpy as np

from farc.apps.calculator import model_generator
from farc import models
import farc.monte_carlo as mc
from farc.monte_carlo.data import activity_distributions, virus_distributions, mask_distributions
from farc.monte_carlo.data import expiration_distribution, expiration_BLO_factors, expiration_distributions
from .DEFAULT_DATA import ACTIVITY_TYPES

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
    mechanical_ventilation_type: str
    air_supply: float
    biov_amount: float
    biov_option: int

    def ventilation(self) -> models._VentilationBase:
        """FormData ventilation function from CARA model"""
        always_on = models.PeriodicInterval(period=120, duration=120)
        # Initializes a ventilation instance as a window if 'natural_ventilation' is selected, or as a BIOV-filter otherwise
        # If natural_ventilation and windows_open_periodically are selected, windows will be open during lunch and coffee breaks
        
        if self.ventilation_type == 'natural_ventilation':
            if self.window_opening_regime == 'windows_open_periodically':
                window_interval_boundaries = models.PeriodicInterval(self.windows_frequency, self.windows_duration, min(self.infected_start, self.exposed_start)/60).boundaries() 
                breaks_interval_boundaries = self.exposed_lunch_break_times()+self.infected_lunch_break_times()+self.exposed_coffee_break_times()
                for t1, t2 in breaks_interval_boundaries : 
                        window_interval_boundaries = window_interval_boundaries + ((t1, t2),)

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
class Event:
    start : int
    end : int
    location : RoomType
    mask_ratio : float
    mask_type : str
    activity : str

@dataclass
class Schedule:
    events : list = field(default_factory=lambda: [])
    def add_event(self, event):
        self.events.append(event)
    
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
    name : str
    id:int 
    schedule : Schedule = Schedule()
    exposure_model : list = field(default_factory=lambda: [])
    infected: bool = False
    cumulative_dose:  models._VectorisedFloat = 0.
    current_event: Event = None
    infection_probability : float = 0



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
        if self.current_event.mask_ratio > 0:
            mask = mask_distributions[self.current_event.mask_type]
        else:
            mask = models.Mask.types['No mask']
        return mask

    def infected_population(self, simulation, time1, time2):
        """Adaptation of infected population from model_generator"""
        virus = virus_distributions[simulation.virus_type]
        scenario_activity_and_expiration = {}
        for activity in ACTIVITY_TYPES :
            scenario_activity_and_expiration[activity['Id']] = (activity['Activity'], activity['Expiration'])
        [activity_defn, expiration_defn] = scenario_activity_and_expiration[self.current_event.activity]
        activity = activity_distributions[activity_defn]
        expiration = model_generator.build_expiration(expiration_defn)
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
        scenario_activity = {}
        for activity in ACTIVITY_TYPES : 
            scenario_activity[activity['Id']] = activity['Activity']

        exposed_activity_defn = scenario_activity[self.current_event.activity]
        activity = activity_distributions[exposed_activity_defn]

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
            return total_dose
        else :
            return 0.

    def calculate_infection_probability(self):
        if not self.infected and self.exposure_model :
            self.infection_probability = np.mean(self.exposure_model[0]._dose_infection_probability(self.cumulative_dose))
        else :
            return 0.

    def add_model(self, model : models.ExposureModel):
        self.exposure_model.append(model)


@dataclass
class Room(RoomType):
    id:int
    humidity:float
    temperature : float
    concentrationModels: list = field(default_factory=lambda: [])
    building: Building = None
    virus_concentration: models._VectorisedFloat = 0.
    cumulative_exposure: models._VectorisedFloat = 0.
    #All concentrations models from infected people who went to this room and left virus particles

    def set_building(self, building : Building):
        self.building = building

    def get_occupants(self, simulation):
        occupants = []
        for person in simulation.people :
            if person.get_location() == self :
                occupants.append(person)

        return occupants

    def build_model(self, infected : Person, simulation, time1 : int, time2: int):
        room = models.Room(volume = self.volume,humidity = self.humidity)
        ventilation = self.ventilation.ventilation()
        if infected.get_location() and infected.get_location().id == self.id:
            infected_population = infected.infected_population(simulation, time1, time2)
            self.concentrationModels.append(mc.ConcentrationModel(
                room=room,
                ventilation=ventilation,
                infected=infected_population,
                evaporation_factor=0.3,
            ))
        for person in self.get_occupants(simulation) :
            exposed_population = person.exposed_population(time1, time2)
            for model in self.concentrationModels :
                person.add_model(mc.ExposureModel(model, exposed_population).build_model(size=60000))
 


    def calculate_cumulative_dose(self):
        self.cumulative_exposure = np.mean(self.cumulative_exposure)

    
@dataclass
class Simulation:
    virus_type : str
    rooms: list = field(default_factory=lambda: [])
    people: list = field(default_factory=lambda: [])

    def get_room_id(self, room : Room):
        i=0
        for element in self.rooms :
            if element == room :
                return i
            i += 1

    def add_room(self, room : Room): 
        self.rooms.append(room)

    def delete_room(self, room : Room):
        self.rooms.pop(self.get_room_id(room))

    def get_person_id(self, person : Person):
        i=0
        for element in self.people :
            if element == person :
                return i
            i += 1

    def add_person(self, person : Person):
        self.people.append(person)

    def delete_person(self, person: Person):
        self.people.pop(self.get_person_id(person))

    def get_infected(self):
        for person in self.people:
            if person.infected:
                return person
        

@dataclass
class Report:
    simulations: list = field(default_factory=lambda: [])

