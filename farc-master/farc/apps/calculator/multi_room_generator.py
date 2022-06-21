from copy import deepcopy
from dataclasses import dataclass

import numpy as np

import farc.apps.calculator.multi_room_model as multi_room_model



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
                person.set_event(None)
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

