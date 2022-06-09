from copy import deepcopy
from dataclasses import dataclass

import numpy as np

import multi_room_model

import report_generator


@dataclass 
class MultiGenerator:
    simulation : multi_room_model.Simulation
    report : multi_room_model.Report
    n = simulation.people.size

    def interesting_times(self):
        """Return every moment someone change room"""
        times = []
        for person in self.simulation.people:
            for event in person.schedule.events:
                times += event.start
                times += event.end
        unique_times = np.unique(np.array(times))
        return np.sort(unique_times)

    def calculate_simulation_data(self):
        for person in self.simulation.people:
            person.infected = True
            simulation_copy = deepcopy(self.simulation)
            times = self.interesting_times()
            for time1, time2 in zip(times[:-1], times[1:]):
                self.calculate_event(time1,time2,simulation_copy, infected = person)


            person.infected = False

    def calculate_event(self, time1, time2, simulation : multi_room_model.Simulation, infected: multi_room_model.Person):
        for person in simulation.people:
            try :
                current_event = person.schedule.get_event_by_time(time1)
                person.set_location(current_event.location)
                person.set_event(current_event)
            except ValueError :
                if person.location != None :
                    person.location.delete_occupant(person)

        
        # Low resolution to try to improve performances            
        times = report_generator.interesting_times(infected.exposure_model, 5)

        for room in simulation.rooms:
            room.build_model(infected, simulation, time1, time2)
            for person in room.occupants:
                # Could be optimized, room concentration calculated size(room.occupants) times
                person.calculate_data(times)
