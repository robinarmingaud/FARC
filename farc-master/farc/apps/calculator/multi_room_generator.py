from copy import deepcopy
from dataclasses import dataclass
import dataclasses
import html
import typing

import numpy as np

import farc.apps.calculator.multi_room_model as multi_room_model

minutes_since_midnight = typing.NewType('minutes_since_midnight', int)

@dataclass 
class MultiGenerator:
    simulation : multi_room_model.Simulation
    report : multi_room_model.Report

    def interesting_times(self):
        """Return every moment someone change room"""
        times = []
        for person in self.simulation.people:
            for event in person.schedule.events:
                times.append(event.start)
                times.append(event.end)
        unique_times = np.unique(np.array(times))
        return np.sort(unique_times)
    
    def calculate_event(self, time1, time2, simulation : multi_room_model.Simulation, infected: multi_room_model.Person):
        for person in simulation.people:
            try :
                current_event = person.schedule.get_event_by_time(time1)
                person.set_location(current_event.location)
                person.set_event(current_event)
            except ValueError :
                if person.location != None :
                    person.location.delete_occupant(person)
        for room in simulation.rooms:
                room.build_model(infected, simulation, time1, time2)
                for person in room.occupants:
                    # Could be optimized, room concentration calculated size(room.occupants) times
                        virus_dose = person.calculate_data()
                        room.cumulative_exposure += virus_dose
                        

    def calculate_means(self, simulation : multi_room_model.Simulation):
        """TODO : Add concentration/time and cumulative dose/time ?"""
        for person in simulation.people :
            person.calculate_infection_probability()
        for room in simulation.rooms :
            room.calculate_cumulative_dose()

    def calculate_simulation_data(self):
        times = self.interesting_times()
        for person in self.simulation.people:
            person.infected = True
            simulation_copy = deepcopy(self.simulation)
            infected = simulation_copy.get_infected()
            for time1, time2 in zip(times[:-1], times[1:]):
                self.calculate_event(time1,time2,simulation_copy, infected = infected)
            person.infected = False
            self.calculate_means(simulation_copy)
            self.report.simulations = np.append(self.report.simulations, simulation_copy)



@dataclasses.dataclass
class FormData:
    simulation = multi_room_model.Simulation(virus_type='SARS_CoV_2_OMICRON')
    
    
    @classmethod
    def from_dict(cls, form_data: typing.Dict) -> "FormData":
        form_data.pop('_xsrf', None)
        instance = FormData()

        # Don't let arbitrary unescaped HTML through the net.
        for key, value in form_data.items():
            if isinstance(value, str):
                form_data[key] = html.escape(value)

        for key, value in form_data.items():
            if key in _CAST_RULES_FORM_ARG_TO_NATIVE:
                form_data[key] = _CAST_RULES_FORM_ARG_TO_NATIVE[key](value)


            if key.startswith('room_name'):
                room_id = get_element_id(key)
                instance.simulation.add_room(build_room_from_form(form_data, room_id))

            if key.startswith('person_name'):
                person_id = get_element_id(key)
                instance.simulation.add_person(build_person_from_form(form_data, person_id))

            if key.startswith('event_start'):
                event_id = get_element_id(key)
                room_id = get_form_data_value(form_data, 'event_location', event_id)
                person_id = get_form_data_value(form_data, 'event_person', event_id)
                instance.get_person_by_id(person_id).schedule.add_event(build_event_from_form(form_data, event_id, instance.get_room_by_id(room_id)))

        return instance.simulation

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

        return form_dict

    def get_person_by_id(self, id):
        for person in self.simulation.people :
            if person.id == int(id) :
                return person

    def get_room_by_id(self, id):
        for room in self.simulation.rooms :
            if room.id == int(id) :
                return room

#: Mapping of field name to a callable which can convert values from form
#: input (URL encoded arguments / string) into the correct type.
_CAST_RULES_FORM_ARG_TO_NATIVE: typing.Dict[str, typing.Callable] = {}

#: Mapping of field name to callable which can convert native type to values
#: that can be encoded to URL arguments.
_CAST_RULES_NATIVE_TO_FORM_ARG: typing.Dict[str, typing.Callable] = {}

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


def build_ventilation_from_form(form_data, index):
    return multi_room_model.Ventilation(get_form_data_value(form_data, 'ventilation', index),
                                        float(get_form_data_value(form_data, 'duration', index)),
                                        float(get_form_data_value(form_data, 'frequency', index)),
                                        float(get_form_data_value(form_data, 'height', index)),
                                        get_form_data_value(form_data, 'window_type', index),
                                        float(get_form_data_value(form_data, 'width', index)),
                                        int(get_form_data_value(form_data, 'number', index)),
                                        get_form_data_value(form_data, 'opening_regime', index),
                                        float(get_form_data_value(form_data, 'opening_distance', index)),
                                        get_form_data_value(form_data, 'month', index),
                                        int(get_form_data_value(form_data, 'room_heating_option', index)),
                                        'mech_type_air_supply',
                                        float(get_form_data_value(form_data, 'air_supply', index)),
                                        float(get_form_data_value(form_data, 'biov_amount', index)),
                                        int(get_form_data_value(form_data, 'biov_option', index))
                                        )


def build_room_from_form(form_data, index):
    return multi_room_model.Room(get_form_data_value(form_data, 'room_name', index), 
                                int(get_form_data_value(form_data, 'volume', index)),
                                build_ventilation_from_form(form_data,index),
                                index, #TODO : humidity and temperature in form or using room heating option
                                0.3,
                                20
                                )

def build_person_from_form(form_data, index):
    return multi_room_model.Person(get_form_data_value(form_data, 'person_name', index),
                                index
                                )


def build_event_from_form(form_data, index, room):
    return multi_room_model.Event(time_string_to_minutes(get_form_data_value(form_data, 'event_start', index))/60,
                                 time_string_to_minutes(get_form_data_value(form_data, 'event_finish', index))/60,
                                 room,
                                 float(get_form_data_value(form_data, 'event_mask_ratio', index)),
                                 get_form_data_value(form_data, 'event_mask_type', index),
                                 get_form_data_value(form_data, 'event_activity', index)
                                 )

def get_element_id(key: str):
    return int(key.split('[')[1][:-1])

def get_form_data_value(form_data, key: str, index: int):
    return form_data[key+'['+str(index)+']']

def _safe_int_cast(value) -> int:
    if isinstance(value, int):
        return value
    elif isinstance(value, float) and int(value) == value:
        return int(value)
    elif isinstance(value, str) and value.isdecimal():
        return int(value)
    else:
        raise TypeError(f"Unable to safely cast {value} ({type(value)} type) to int")
 
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