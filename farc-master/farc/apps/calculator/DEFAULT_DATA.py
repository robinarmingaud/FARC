import os
import tornado


# ------------------ Translation ----------------------

path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "locale"))

tornado.locale.load_gettext_translations(path , "messages")
locale = tornado.locale.get()
_ = locale.translate


# ------------------ Default form values ----------------------

_NO_DEFAULT = object()
_DEFAULT_MC_SAMPLE_SIZE = 60000
# The calculator version is based on a combination of the model version and the
# semantic version of the calculator itself. The version uses the terms
# "{MAJOR}.{MINOR}.{PATCH}" to describe the 3 distinct numbers constituting a version.
# Effectively, if the model increases its MAJOR version then so too should this
# calculator version. If the calculator needs to make breaking changes (e.g. change
# form attributes) then it can also increase its MAJOR version without needing to
# increase the overall CARA version (found at ``farc.__version__``).
__version__ = "2.0.0"

_MULTI_DEFAULTS = {  
    "air_supply": 100,
    "humidity": 0.3,
    "event_month": _("January"),
    "biov_amount": 1000,
    "biov_option": 0,
    "location_latitude": 47.21725,
    "location_longitude": -1.55336,
    "location_name": "Nantes, Loire-Atlantique, Pays de la Loire, FRA",
    "mechanical_ventilation_type": "mech_type_air_supply",
    "opening_distance": 0.5,
    "room_heating_option": 1, # 1: True, 0 : False
    "room_number": _("My room"),
    "volume": 100,
    "air_changes": 1.,
    "simulation_name": _("My simulation"),
    "person_id": 0,
    "room_id": 0,
    "people_number" : 1,
    "ventilation_type": "mechanical_ventilation",
    "virus_type": "SARS_CoV_2_OMICRON",
    "viruses" : {"SARS_CoV_2" : _("SARS-CoV-2 (nominal strain)"), "SARS_CoV_2_ALPHA" : _("SARS-CoV-2 (Alpha VOC)"), "SARS_CoV_2_BETA" : _("SARS-CoV-2 (Beta VOC)"), "SARS_CoV_2_GAMMA": _("SARS-CoV-2 (Gamma VOC)"), "SARS_CoV_2_DELTA" : _("SARS-CoV-2 (Delta VOC)"), "SARS_CoV_2_OMICRON" :_("SARS-CoV-2 (Omicron VOC)")},
    "window_type": "window_sliding",
    "window_height": 1.,
    "window_width": 1.,
    "windows_duration": 15,
    "windows_frequency": 60,
    "windows_number": 1,
    "window_opening_regime": "windows_open_permanently",
    "inside_temp" : 20.,
    "type_name" : _("Room"),
    "name" : _("Person"),
    "event_mask_wearing_option" : "mask_off",
    "event_activity_level" : "Seated",
    "event_activity_breathing" : 8,
    "event_activity_speaking" : 2,
    "event_activity_shouting" : 0,
    "start" : "08:30",
    "end" : "17:30",
    "mask_ratio" : 0.7,
    "mask_type" : "Type_I",
    "activity" : "Office_worker" 
}

_DEFAULTS = {
        "exposed_activity_type": "Office_worker",
        "exposed_activity_level" : "Seated",
        "exposed_breathing" : 8,
        "exposed_speaking" : 2,
        "exposed_shouting" : 0,
        "exposed_mask_wear_ratio": 0.7,
        "infected_activity_type": "Office_worker",
        "infected_activity_level" : "Seated",
        "infected_breathing" : 8,
        "infected_speaking" : 2,
        "infected_shouting" : 0,
        "infected_mask_wear_ratio": 0.7,
        "air_changes": 1.,
        "air_supply": 100,
        "calculator_version": __version__,
        "ceiling_height": 2.5,
        "humidity": 0.3,
        "inside_temp": 20,
        "exposed_coffee_break_option": "coffee_break_0",
        "exposed_coffee_duration": 5,
        "exposed_finish": "17:30",
        "exposed_lunch_finish": "13:30",
        "exposed_lunch_option": 1,
        "exposed_lunch_start": "12:30",
        "exposed_start": "08:30",
        "event_month": _("January"),
        "floor_area": 40,
        "biov_amount": 1000,
        "biov_option": 0,
        "infected_coffee_break_option": "coffee_break_0",
        "infected_coffee_duration": 5,
        "infected_dont_have_breaks_with_exposed": 0,
        "infected_finish": "17:30",
        "infected_lunch_finish": "13:30",
        "infected_lunch_option": 1,
        "infected_lunch_start": "12:30",
        "infected_people": 1,
        "infected_start": "08:30",
        "location_latitude": 47.21725,
        "location_longitude": -1.55336,
        "location_name": "Nantes, Loire-Atlantique, Pays de la Loire, FRA",
        "mask_type": "Type_I",
        "mask_wearing_option": "mask_off",
        "mechanical_ventilation_type": "mech_type_air_supply",
        "opening_distance": 0.5,
        "room_heating_option": 1, # 1: True, 0 : False
        "room_number": _("My room"),
        "room_volume": 100,
        "simulation_name": _("My simulation"),
        "total_people": 10,
        "ventilation_type": "mechanical_ventilation",
        "virus_type": "SARS_CoV_2_OMICRON",
        "viruses" : {"SARS_CoV_2" : _("SARS-CoV-2 (nominal strain)"), "SARS_CoV_2_ALPHA" : _("SARS-CoV-2 (Alpha VOC)"), "SARS_CoV_2_BETA" : _("SARS-CoV-2 (Beta VOC)"), "SARS_CoV_2_GAMMA": _("SARS-CoV-2 (Gamma VOC)"), "SARS_CoV_2_DELTA" : _("SARS-CoV-2 (Delta VOC)"), "SARS_CoV_2_OMICRON" :_("SARS-CoV-2 (Omicron VOC)")},
        "volume_type": "room_volume_explicit",
        "window_type": "window_sliding",
        "window_height": 1.,
        "window_width": 1.,
        "windows_duration": 15,
        "windows_frequency": 60,
        "windows_number": 1,
        "window_opening_regime": "windows_open_permanently",
    }

# ------------------ Activities ----------------------

ACTIVITY_TYPES = [{"Group":_("Business"),"Id":"Office_worker", "Name" : _("Office worker"), "Activity" : "Seated", "Expiration" : {_("Speaking"): 2, _("Breathing"): 8}},
                {"Group":_("Business"),"Id":"Workshop_worker", "Name" : _("Workshop worker"), "Activity" :"Moderate activity", "Expiration" : {_("Speaking"):7, _("Breathing"):1.5, _("Shouting"):1.5}},
                {"Group":_("Business"),"Id":"Meeting_participant", "Name" : _("Meeting participant"), "Activity" : "Seated", "Expiration" : {_("Speaking"):1.5, _("Breathing"):8, _("Shouting"): 0.5 }},
                {"Group":_("Business"),"Id":"Meeting_leader", "Name" : _("Meeting leader"), "Activity" : "Standing", "Expiration" : {_("Breathing"):6,_("Speaking"):3,_("Shouting"):1}},
                {"Group":_("Hospital"),"Id":"Hospital_patient", "Name" : _("Hospital patient"), "Activity" : "Seated", "Expiration" : {_("Speaking"): 0.5, _("Breathing"): 9.5}},
                {"Group":_("Hospital"),"Id":"Nurse_working", "Name" : _("Nurse working"), "Activity" :"Light activity", "Expiration" : {_("Speaking"): 2, _("Breathing"): 8}},
                {"Group":_("Hospital"),"Id":"Physician_working", "Name" : _("Physician working"), "Activity" : "Standing", "Expiration" : {_("Speaking"): 5, _("Breathing"): 5}},
                {"Group":_("Education"),"Id":"Student_sitting", "Name" : _("Student sitting"), "Activity" : "Seated", "Expiration" : {_("Speaking"):0.5 , _("Breathing"): 9.5}},
                {"Group":_("Education"),"Id":"Professor_teaching", "Name" : _("Professor teaching"), "Activity" : "Standing", "Expiration" : {_("Speaking"): 6, _("Breathing"): 2, _("Shouting"):2}},
                {"Group":_("Education"),"Id":"Professor_conferencing", "Name" : _("Professor conferencing"), "Activity" :"Light activity", "Expiration" : {_("Speaking"):2,_("Breathing"):2, _("Shouting"):6}},
                {"Group":_("Events"),"Id":"Concert_musician_soft_music", "Name" : _("Concert musician (soft music)"), "Activity" : "Standing", "Expiration" : {_("Speaking"):0.5,_("Breathing"):9.5}},
                {"Group":_("Events"),"Id":"Concert_musician_rock", "Name" : _("Concert musician (rock)"), "Activity" :"Moderate activity", "Expiration" : {_("Speaking"):1,_("Breathing"):8, _("Shouting"):1}},
                {"Group":_("Events"),"Id":"Concert_singer_rock", "Name" : _("Concert singer (rock)"), "Activity" :"Moderate activity", "Expiration" : {_("Speaking"):1,_("Breathing"):2, _("Shouting"):7}},
                {"Group":_("Events"),"Id":"Concert_spectator_standing", "Name" : _("Concert spectator (standing)"), "Activity" :"Light activity", "Expiration" : {_("Speaking"):1,_("Breathing"):8, _("Shouting"):1}},
                {"Group":_("Events"),"Id":"Concert_spectator_sitting", "Name" : _("Concert spectator (sitting)"), "Activity" : "Seated", "Expiration" : {_("Speaking"):0.5,_("Breathing"):9, _("Shouting"):0.5}},
                {"Group":_("Events"),"Id":"Museum_visitor", "Name" : _("Museum visitor"), "Activity" : "Standing", "Expiration" : {_("Speaking"):1,_("Breathing"):9}},
                {"Group":_("Events"),"Id":"Theater_spectator", "Name" : _("Theater spectator"), "Activity" : "Seated", "Expiration" : {_("Speaking"):0.5,_("Breathing"):9, _("Shouting"):0.5}},
                {"Group":_("Events"),"Id":"Theater_actor", "Name" : _("Theater actor"), "Activity" :"Moderate activity", "Expiration" : {_("Breathing"):7, _("Shouting"):3}},
                {"Group":_("Events"),"Id":"Conferencer", "Name" : _("Conferencer"), "Activity" :"Light activity", "Expiration" : {_("Speaking"):2, _("Breathing"):2, _("Shouting"):6}},
                {"Group":_("Events"),"Id":"Conference_attendee", "Name" : _("Conference attendee"), "Activity" : "Seated", "Expiration" : {_("Speaking"):0.5, _("Breathing"):9.5}},
                {"Group":_("Restaurant and Bar"),"Id":"Guest_standing", "Name" : _("Guest standing"), "Activity" : "Standing", "Expiration" : {_("Speaking"):2, _("Breathing"):6, _("Shouting"):2}},
                {"Group":_("Restaurant and Bar"),"Id":"Guest_sitting", "Name" : _("Guest sitting"), "Activity" : "Seated", "Expiration" : {_("Speaking"):4, _("Breathing"):6}},
                {"Group":_("Restaurant and Bar"),"Id":"Server", "Name" : _("Server"), "Activity" :"Light activity", "Expiration" : {_("Speaking"):2, _("Breathing"):8}},
                {"Group":_("Restaurant and Bar"),"Id":"Barrista", "Name" : _("Barrista"), "Activity" : "Standing", "Expiration" : {_("Speaking"):2, _("Breathing"):6, _("Shouting"):2}}, 
                {"Group":_("Restaurant and Bar"),"Id":"Nightclub_dancing", "Name" : _("Nightclub dancing"), "Activity" :"Moderate activity", "Expiration" : {_("Breathing"):9, _("Shouting"):1}},
                {"Group":_("Restaurant and Bar"),"Id":"Nightclub_sitting", "Name" : _("Nightclub sitting"), "Activity" : "Seated", "Expiration" : {_("Breathing"):8, _("Shouting"):2}},
                {"Group":_("Store and Retail"),"Id":"Customer_standing", "Name" : _("Customer standing"), "Activity" : "Standing", "Expiration" : {_("Speaking"):1,_("Breathing"):9}},
                {"Group":_("Store and Retail"),"Id":"Cashier_sitting", "Name" : _("Cashier sitting"), "Activity" : "Seated", "Expiration" : {_("Speaking"):5,_("Breathing"):5}},
                {"Group":_("Store and Retail"),"Id":"Vendor_standing", "Name" : _("Vendor standing"), "Activity" : "Standing", "Expiration" : {_("Speaking"):5,_("Breathing"):5}},
                {"Group":_("Sport"),"Id":"Musculation", "Name" : _("Musculation"), "Activity" :"Heavy exercise", "Expiration" : {_("Speaking"):1,_("Breathing"):9}},
                {"Group":_("Sport"),"Id":"Floor_gymnastics", "Name" : _("Floor gymnastics"), "Activity" :"Moderate activity", "Expiration" : {_("Speaking"):1,_("Breathing"):8, _("Shouting"):1}},
                {"Group":_("Sport"),"Id":"Team_competition", "Name" : _("Team competition"), "Activity" :"Heavy exercise", "Expiration" : {_("Speaking"):0.5,_("Breathing"):8, _("Shouting"):1.5}},
                {"Group":_("Miscellaneous"),"Id":"Trip_in_elevator", "Name" : _("Trip in elevator"), "Activity" : "Standing", "Expiration" : {_("Speaking"):1,_("Breathing"):9}},
                {"Group":_("Navy"),"Id":"Watch_seated", "Name" : _("Watch seated"), "Activity" : "Seated", "Expiration" : {_("Shouting"): 10, _("Speaking"): 30, _("Breathing"): 60}}, # Manning a console seating in front of it
                {"Group":_("Navy"),"Id":"Watch_standing", "Name" : _("Watch standing"), "Activity" :"Light activity", "Expiration" : {_("Shouting"): 20, _("Speaking"): 30, _("Breathing"): 50}}] # Pacing and moving from station to station, giving orders and looking at data at stations

# ------------------ Validation ----------------------

MECHANICAL_VENTILATION_TYPES = {"mech_type_air_changes", "mech_type_air_supply", "not-applicable"}
MASK_TYPES = {"Type_I", "FFP2"}
MASK_WEARING_OPTIONS = {"mask_on", "mask_off"}
VENTILATION_TYPES = {"natural_ventilation", "mechanical_ventilation", "no_ventilation"}
VIRUS_TYPES = {"SARS_CoV_2", "SARS_CoV_2_ALPHA", "SARS_CoV_2_BETA","SARS_CoV_2_GAMMA", "SARS_CoV_2_DELTA", "SARS_CoV_2_OMICRON"}
VOLUME_TYPES = {"room_volume_explicit", "room_volume_from_dimensions"}
WINDOWS_OPENING_REGIMES = {"windows_open_permanently", "windows_open_periodically", "not-applicable"}
WINDOWS_TYPES = {"window_sliding", "window_hinged", "not-applicable"}

COFFEE_OPTIONS_INT = {"coffee_break_0": 0, "coffee_break_1": 1, "coffee_break_2": 2, "coffee_break_4": 4}

MONTH_NAMES = {
    "January" : _("January"), "February" : _("February"), "March" : _("March"), "April" : _("April"), "May" : _("May"), "June" :_("June"), "July" : _("July"),
    "August" : _("August"), "September" : _("September"), "October": _("October"), "November" : _("November"), "December" : _("December"),
}

# ------------------ Text ----------------------

TOOLTIPS = {"virus_data" : _("Choose the SARS-CoV-2 Variant of Concern (VOC)."),
"room_data":_("The area you wish to study (choose one of the 2 options). Indicate if a heating/air conditionning system is in use."),
"ventilation_data":_("The available means of venting / bioventilation of indoor spaces."),
"window_open" : _("If 'Periodically' is selected, windows will be open during lunch and coffee breaks"),
"bio_ventilation" : _("This value can be modified for alternative scenarios even if 'No' is checked"),
"face_mask" : _("Masks worn or removed when a 2m physical distance is respected and proper venting is ensured."),
"event_data" : _("The total no. of occupants in the room and how many of them you assume are infected."),
"activity_breaks" : _("Input breaks that, by default, are the same for infected/exposed person(s) unless specified otherwise."),
"activity_level" : _("Percentage of time spent breathing, talking or shouting")
}
PLACEHOLDERS = {"room_volume":_("Room volume (m³)"),
"room_floor_area":_("Room floor area (m²)"),
"ceiling_height" : _("Room ceiling height (m)"),
"flow_rate" : _("Flow rate (m³ / hour)"),
"air_exchange" : _("Air exchange (h⁻¹)"),
"number" : _("Number (#)"),
"height" : _("Height (m)"),
"width" : _("Width (m)"),
"opening_distance" : _("Opening distance (m)"),
"duration" : _("Duration (min)"),
"frequency" : _("Frequency (min)"),
"default" : _("Default"),
}
