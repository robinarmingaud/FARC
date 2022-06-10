from farc.apps.calculator import multi_room_generator
from farc.apps.calculator import multi_room_model



Ventilation1 = multi_room_model.Ventilation('mechanical_ventilation',10,1,1,'window_sliding',1,1,'windows_open_permanently',1,'January',1,'mech_type_air_supply',100,1000.,0)
Room1 = multi_room_model.Room('Test',100, Ventilation1, 1, 0.3, 20.)
Room2 = multi_room_model.Room('Test2', 100, Ventilation1, 2 ,0.3 ,20.)
Event1 = multi_room_model.Event(8, 12, Room1, 0.7, 'Type_I', 'Musculation')
Event2 = multi_room_model.Event(12.01, 16, Room1, 0.7, 'Type_I', 'Concert_musician_rock')
Schedule1 = multi_room_model.Schedule()
Schedule1.add_event(Event1)
Schedule2 = multi_room_model.Schedule()
Schedule2.add_event(Event2)
Person1 = multi_room_model.Person('Musculation', 1, schedule = Schedule1)
Person2 = multi_room_model.Person('Concert musician rock', 2, schedule = Schedule2)


Simulation = multi_room_model.Simulation("SARS_CoV_2_OMICRON")
Simulation.add_person(Person1)
Simulation.add_person(Person2)
Simulation.add_room(Room1)
Simulation.add_room(Room2)

Report = multi_room_model.Report()

MultiReport = multi_room_generator.MultiGenerator(Simulation, Report)

MultiReport.calculate_simulation_data()

print(MultiReport.report.simulations[0].people[0].infection_probability)
print(MultiReport.report.simulations[0].people[1].infection_probability)
print(MultiReport.report.simulations[1].people[1].infection_probability)
print(MultiReport.report.simulations[1].people[0].infection_probability)