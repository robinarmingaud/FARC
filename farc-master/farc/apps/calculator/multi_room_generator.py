import base64
from copy import deepcopy
from dataclasses import dataclass
import dataclasses
import html
import typing
import urllib
import numpy as np
import zlib

import farc.apps.calculator.multi_room_model as multi_room_model
from farc.apps.calculator.model_generator import time_minutes_to_string, time_string_to_minutes, _safe_int_cast, _CAST_RULES_FORM_ARG_TO_NATIVE, _CAST_RULES_NATIVE_TO_FORM_ARG

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
                person.set_event(current_event)
            except ValueError :
                person.set_event(None)
        for room in simulation.rooms:
                room.build_model(infected, simulation, time1, time2)
                occupants = room.get_occupants(simulation)
                for person in occupants:
                    person.calculate_data()
                    if person.infected :
                        room.cumulative_exposure = room.cumulative_exposure + person.virus_dose*(person.number-1)
                    else : 
                        room.cumulative_exposure = room.cumulative_exposure + person.virus_dose*person.number
                        
    def calculate_means(self, simulation : multi_room_model.Simulation):
        for person in simulation.people :
            person.calculate_infection_probability()
            person.clear_data()
        for room in simulation.rooms :
            room.calculate_cumulative_dose()
            room.clear_data()



    def calculate_simulation_data(self, executor_factory):
        times = self.interesting_times()
        for person in self.simulation.people:
            person.infected = True
            simulation_copy = deepcopy(self.simulation)
            infected = simulation_copy.get_infected()
            with executor_factory() as executor :
                for time1, time2 in zip(times[:-1], times[1:]):
                    executor.submit(self.calculate_event, time1, time2, simulation_copy, infected)
            person.infected = False
            self.calculate_means(simulation_copy)
            self.report.simulations = np.append(self.report.simulations, simulation_copy)
        return self


@dataclass
class FormData:
    simulation : multi_room_model.Simulation = multi_room_model.Simulation(virus_type='SARS_CoV_2_OMICRON')
    
    
    @classmethod
    def from_dict(cls, form_data: typing.Dict):
        form_data = form_data.copy()
        form_data.pop('_xsrf', None)


        # Don't let arbitrary unescaped HTML through the net.
        for key, value in form_data.items():
            if isinstance(value, str):
                form_data[key] = html.escape(value)

        instance = FormData(multi_room_model.Simulation(virus_type=form_data['virus_type'], location_name= form_data['location_name'],
                                                        location_latitude=float(form_data['location_latitude']),location_longitude=float(form_data['location_longitude'])))

        for key, value in form_data.items():
            if key in _CAST_RULES_FORM_ARG_TO_NATIVE:
                form_data[key] = _CAST_RULES_FORM_ARG_TO_NATIVE[key](value)

            if key.startswith('room_volume'): 
                if isinstance(get_element_id(key), int) :
                    room_id = get_element_id(key)
                    instance.simulation.add_room(build_room_from_form(form_data, room_id))

            if key.startswith('person_name'):
                if isinstance(get_element_id(key), int) :
                    person_id = get_element_id(key)
                    instance.simulation.add_person(build_person_from_form(form_data, person_id))

            if key.startswith('event_start'):
                if isinstance(get_element_id(key), int) :
                    event_id = get_element_id(key)
                    room_id = get_form_data_value(form_data, 'event_location', event_id)
                    person_id = get_form_data_value(form_data, 'event_person', event_id)
                    instance.get_person_by_id(person_id).schedule.add_event(build_event_from_form(form_data, event_id, instance.get_room_by_id(room_id)))
        return instance

    @classmethod
    def to_dict(cls, form: "FormData", strip_defaults: bool = False) -> dict:
        form_dict = {}
        room_list = []
        people_list = []
        event_list = []

        for room in form.simulation.rooms :
            room_dict = {}
            for field in dataclasses.fields(room):
                if field.name == 'ventilation' :
                    ventilation = getattr(room, field.name)
                    for element in dataclasses.fields(ventilation):
                        if getattr(ventilation, element.name) != element.default :
                            room_dict[element.name] = getattr(ventilation, element.name)
                else :   
                    if getattr(room, field.name) != field.default :
                        room_dict[field.name] = getattr(room, field.name)

            for attr, value in room_dict.items():
                if attr in _CAST_RULES_NATIVE_TO_FORM_ARG:
                    room_dict[attr] = _CAST_RULES_NATIVE_TO_FORM_ARG[attr](value)
            room_list.append(room_dict)

        for person in form.simulation.people :
            person_dict = {}
            for field in dataclasses.fields(person):
                if getattr(person, field.name) != field.default :
                    person_dict[field.name] = getattr(person, field.name)

            

            for attr, value in person_dict.items():
                if attr in _CAST_RULES_NATIVE_TO_FORM_ARG:
                    person_dict[attr] = _CAST_RULES_NATIVE_TO_FORM_ARG[attr](value)
            try :
                del(person_dict['schedule'])
            except :
                pass
            
            people_list.append(person_dict)

            for event in person.schedule.events :
                event_dict = {}
                event_dict['Person'] = person.id
                for field in dataclasses.fields(event):
                    if field.name == 'location' :
                        location = getattr(event, field.name)
                        event_dict[field.name] = getattr(location, 'id')
                    else :    
                        if getattr(event, field.name) != field.default :
                            event_dict[field.name] = getattr(event, field.name)
                try :
                    event_dict['start'] = time_minutes_to_string(int(event_dict['start']*60))
                except :
                    pass
                try : 
                    event_dict['end'] = time_minutes_to_string(int(event_dict['end']*60))
                except :
                    pass

                for attr, value in event_dict.items():
                    if attr in _CAST_RULES_NATIVE_TO_FORM_ARG:
                        event_dict[attr] = _CAST_RULES_NATIVE_TO_FORM_ARG[attr](value)
                event_list.append(event_dict)

        form_dict['Room_list'] = room_list
        form_dict['People_list'] = people_list
        form_dict['Event_list'] = event_list

        return form_dict

    def get_person_by_id(self, id):
        for person in self.simulation.people :
            if person.id == int(id) :
                return person

    def get_room_by_id(self, id):
        for room in self.simulation.rooms :
            if room.id == int(id) :
                return room


def build_ventilation_from_form(form_data, index):
    return multi_room_model.Ventilation(inside_temp = float(get_form_data_value(form_data, 'inside_temp', index)),
                                        ventilation_type = get_form_data_value(form_data, 'ventilation_type', index),
                                        windows_duration = float(get_form_data_value(form_data, 'windows_duration', index)),
                                        windows_frequency = float(get_form_data_value(form_data, 'windows_frequency', index)),
                                        window_height = float(get_form_data_value(form_data, 'window_height', index)),
                                        window_type = get_form_data_value(form_data, 'window_type', index),
                                        window_width = float(get_form_data_value(form_data, 'window_width', index)),
                                        windows_number = int(get_form_data_value(form_data, 'windows_number', index)),
                                        window_opening_regime = get_form_data_value(form_data, 'window_opening_regime', index),
                                        opening_distance = float(get_form_data_value(form_data, 'opening_distance', index)),
                                        event_month = form_data['event_month'],
                                        room_heating_option = int(get_form_data_value(form_data, 'room_heating_option', index)),
                                        mechanical_ventilation_type= get_form_data_value(form_data, 'mechanical_ventilation_type', index),
                                        air_supply= float(get_form_data_value(form_data,'air_supply', index)),
                                        biov_amount=float(get_form_data_value(form_data, 'biov_amount', index)),
                                        biov_option=int(get_form_data_value(form_data,'biov_option',index))
                                        )


def build_room_from_form(form_data, index):
    return multi_room_model.Room(id = index,
                                 type_name = get_form_data_value(form_data, 'room_name', index),
                                 volume= float(get_form_data_value(form_data, 'room_volume', index)),
                                 ventilation= build_ventilation_from_form(form_data, index),
                                 humidity = float(get_form_data_value(form_data, 'humidity', index)),
                                )

def build_person_from_form(form_data, index):
    return multi_room_model.Person(name = get_form_data_value(form_data, 'person_name', index),
                                number= float(get_form_data_value(form_data, 'person_number', index)),
                                id = index,
                                schedule=multi_room_model.Schedule())
            


def build_event_from_form(form_data, index, room):
    return multi_room_model.Event( event_mask_wearing_option= get_form_data_value(form_data, 'event_mask_wearing_option', index),
                                event_activity_level= get_form_data_value(form_data, "event_activity_level", index ),
                                event_activity_breathing= float(get_form_data_value(form_data, "event_activity_breathing", index )),
                                event_activity_speaking= float(get_form_data_value(form_data, "event_activity_speaking", index )),
                                event_activity_shouting= float(get_form_data_value(form_data, "event_activity_shouting", index )),
                                start = time_string_to_minutes(get_form_data_value(form_data, 'event_start', index))/60,
                                end = time_string_to_minutes(get_form_data_value(form_data, 'event_finish', index))/60,
                                location = room,
                                mask_type= get_form_data_value(form_data, 'event_mask_type', index),
                                mask_ratio = float(get_form_data_value(form_data, 'event_mask_ratio', index)),
                                activity= get_form_data_value(form_data, 'event_activity', index)
                                )

def get_element_id(key: str):
    try :
        return int(key.split('[')[1][:-1])
    except :
        return None

def get_form_data_value(form_data, key: str, index: int):
    return form_data[key+'['+str(index)+']']


def generate_permalink(base_url, calculator_prefix, form: FormData):
    form_dict = FormData.to_dict(form, strip_defaults=True)

    # Generate the calculator URL arguments that would be needed to re-create this
    # form.
    args = urllib.parse.urlencode(form_dict)
    print(args)

    # Then zlib compress + base64 encode the string. To be inverted by the
    # /_c/ endpoint.
    compressed_args = base64.b64encode(zlib.compress(args.encode())).decode()
    qr_url = f"{base_url}/_m/{compressed_args}"
    url = f"{base_url}{calculator_prefix}?{args}"

    return {
        'link': url,
        'shortened': qr_url,
    }