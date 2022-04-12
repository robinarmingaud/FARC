
# ------------------ Default form values ----------------------

_NO_DEFAULT = object()
_DEFAULT_MC_SAMPLE_SIZE = 250000
# The calculator version is based on a combination of the model version and the
# semantic version of the calculator itself. The version uses the terms
# "{MAJOR}.{MINOR}.{PATCH}" to describe the 3 distinct numbers constituting a version.
# Effectively, if the model increases its MAJOR version then so too should this
# calculator version. If the calculator needs to make breaking changes (e.g. change
# form attributes) then it can also increase its MAJOR version without needing to
# increase the overall CARA version (found at ``farc.__version__``).
__version__ = "1.0.1"
_DEFAULTS = {
        # 'activity_type': 'office',
        'exposed_activity_type': 'Office_worker',
        'exposed_mask_wear_ratio': 0.7,
        'infected_activity_type': 'Office_worker',
        'infected_mask_wear_ratio': 0.7,
        'air_changes': 1.,
        'air_supply': 100,
        'calculator_version': __version__,
        'ceiling_height': 2.5,
        'exposed_coffee_break_option': 'coffee_break_0',
        'exposed_coffee_duration': 5,
        'exposed_finish': '17:30',
        'exposed_lunch_finish': '13:30',
        'exposed_lunch_option': True,
        'exposed_lunch_start': '12:30',
        'exposed_start': '08:30',
        'event_month': 'January',
        'floor_area': 40,
        'biov_amount': 1000,
        'biov_option': 0,
        'infected_coffee_break_option': 'coffee_break_0',
        'infected_coffee_duration': 5,
        'infected_dont_have_breaks_with_exposed': False,
        'infected_finish': '17:30',
        'infected_lunch_finish': '13:30',
        'infected_lunch_option': True,
        'infected_lunch_start': '12:30',
        'infected_people': 1,
        'infected_start': '08:30',
        'location_latitude': 47.21725,
        'location_longitude': -1.55336,
        'location_name': "Nantes, FRA",
        'mask_type': 'Type_I',
        'mask_wearing_option': 'mask_off',
        'mechanical_ventilation_type': 'mech_type_air_supply',
        'opening_distance': 0.5,
        'room_heating_option': 1, # 1: True, 0 : False
        'room_number': "Boardroom",
        'room_volume': 100,
        'simulation_name': "Workshop without masks",
        'total_people': 10,
        'ventilation_type': 'mechanical_ventilation',
        'virus_type': "SARS_CoV_2_OMICRON",
        'viruses' : {"SARS_CoV_2" : "SARS-CoV-2 (nominal strain)", "SARS_CoV_2_ALPHA" : "SARS-CoV-2 (Alpha VOC)", "SARS_CoV_2_BETA" : "SARS-CoV-2 (Beta VOC)", "SARS_CoV_2_GAMMA":"SARS-CoV-2 (Gamma VOC)", "SARS_CoV_2_DELTA" : "SARS-CoV-2 (Delta VOC)", "SARS_CoV_2_OMICRON" :"SARS-CoV-2 (Omicron VOC)"},
        'volume_type': 'room_volume_explicit',
        'window_type': 'window_sliding',
        'window_height': 1.,
        'window_width': 1.,
        'windows_duration': 15,
        'windows_frequency': 60,
        'windows_number': 1,
        'window_opening_regime': 'windows_open_permanently',
    }

# ------------------ Activities ----------------------

ACTIVITY_TYPES = [{'Group':'Business','Id':'Office_worker', 'Name' : 'Office worker', 'Activity' : 'Seated', 'Expiration' : {'Speaking': 2, 'Breathing': 8}},
                {'Group':'Business','Id':'Workshop_worker', 'Name' : 'Workshop worker', 'Activity' : 'Moderate activity', 'Expiration' : {'Speaking':7, 'Breathing':1.5, 'Shouting':1.5}},
                {'Group':'Business','Id':'Meeting_participant', 'Name' : 'Meeting participant', 'Activity' : 'Seated', 'Expiration' : {'Speaking':1.5, 'Breathing':8, 'Shouting': 0.5 }},
                {'Group':'Business','Id':'Meeting_leader', 'Name' : 'Meeting leader', 'Activity' : 'Standing', 'Expiration' : {'Breathing':6,'Speaking':3,'Shouting':1}},
                {'Group':'Hospital','Id':'Hospital_patient', 'Name' : 'Hospital patient', 'Activity' : 'Seated', 'Expiration' : {'Speaking': 0.5, 'Breathing': 9.5}},
                {'Group':'Hospital','Id':'Nurse_working', 'Name' : 'Nurse working', 'Activity' : 'Light activity', 'Expiration' : {'Speaking': 2, 'Breathing': 8}},
                {'Group':'Hospital','Id':'Physician_working', 'Name' : 'Physician working', 'Activity' : 'Standing', 'Expiration' : {'Speaking': 5, 'Breathing': 5}},
                {'Group':'Education','Id':'Student_sitting', 'Name' : 'Student sitting', 'Activity' : 'Seated', 'Expiration' : {'Speaking':0.5 , 'Breathing': 9.5}},
                {'Group':'Education','Id':'Professor_teaching', 'Name' : 'Professor teaching', 'Activity' : 'Standing', 'Expiration' : {'Speaking': 6, 'Breathing': 2, 'Shouting':2}},
                {'Group':'Education','Id':'Professor_conferencing', 'Name' : 'Professor conferencing', 'Activity' : 'Light activity', 'Expiration' : {'Speaking':2,'Breathing':2, 'Shouting':6}},
                {'Group':'Events','Id':'Concert_musician_soft_music', 'Name' : 'Concert musician (soft music)', 'Activity' : 'Standing', 'Expiration' : {'Speaking':0.5,'Breathing':9.5}},
                {'Group':'Events','Id':'Concert_musician_rock', 'Name' : 'Concert musician (rock)', 'Activity' : 'Moderate activity', 'Expiration' : {'Speaking':1,'Breathing':8, 'Shouting':1}},
                {'Group':'Events','Id':'Concert_singer_rock', 'Name' : 'Concert singer (rock)', 'Activity' : 'Moderate activity', 'Expiration' : {'Speaking':1,'Breathing':2, 'Shouting':7}},
                {'Group':'Events','Id':'Concert_spectator_standing', 'Name' : 'Concert spectator (standing)', 'Activity' : 'Light activity', 'Expiration' : {'Speaking':1,'Breathing':8, 'Shouting':1}},
                {'Group':'Events','Id':'Concert_spectator_sitting', 'Name' : 'Concert spectator (sitting)', 'Activity' : 'Seated', 'Expiration' : {'Speaking':0.5,'Breathing':9, 'Shouting':0.5}},
                {'Group':'Events','Id':'Museum_visitor', 'Name' : 'Museum visitor', 'Activity' : 'Standing', 'Expiration' : {'Speaking':1,'Breathing':9}},
                {'Group':'Events','Id':'Theater_spectator', 'Name' : 'Theater spectator', 'Activity' : 'Seated', 'Expiration' : {'Speaking':0.5,'Breathing':9, 'Shouting':0.5}},
                {'Group':'Events','Id':'Theater_actor', 'Name' : 'Theater actor', 'Activity' : 'Moderate activity', 'Expiration' : {'Breathing':7, 'Shouting':3}},
                {'Group':'Events','Id':'Conferencer', 'Name' : 'Conferencer', 'Activity' : 'Light activity', 'Expiration' : {'Speaking':2, 'Breathing':2, 'Shouting':6}},
                {'Group':'Events','Id':'Conference_attendee', 'Name' : 'Conference attendee', 'Activity' : 'Seated', 'Expiration' : {'Speaking':0.5, 'Breathing':9.5}},
                {'Group':'Restaurant and Bar','Id':'Guest_standing', 'Name' : 'Guest standing', 'Activity' : 'Standing', 'Expiration' : {'Speaking':2, 'Breathing':6, 'Shouting':2}},
                {'Group':'Restaurant and Bar','Id':'Guest_sitting', 'Name' : 'Guest sitting', 'Activity' : 'Sitting', 'Expiration' : {'Speaking':4, 'Breathing':6}},
                {'Group':'Restaurant and Bar','Id':'Server', 'Name' : 'Server', 'Activity' : 'Light activity', 'Expiration' : {'Speaking':2, 'Breathing':8}},
                {'Group':'Restaurant and Bar','Id':'Barrista', 'Name' : 'Barrista', 'Activity' : 'Standing', 'Expiration' : {'Speaking':2, 'Breathing':6, 'Shouting':2}}, 
                {'Group':'Restaurant and Bar','Id':'Nightclub_dancing', 'Name' : 'Nightclub dancing', 'Activity' : 'Moderate activity', 'Expiration' : {'Breathing':9, 'Shouting':1}},
                {'Group':'Restaurant and Bar','Id':'Nightclub_sitting', 'Name' : 'Nightclub sitting', 'Activity' : 'Seated', 'Expiration' : {'Breathing':8, 'Shouting':2}},
                {'Group':'Store and Retail','Id':'Customer_standing', 'Name' : 'Customer standing', 'Activity' : 'Standing', 'Expiration' : {'Speaking':1,'Breathing':9}},
                {'Group':'Store and Retail','Id':'Cashier_sitting', 'Name' : 'Cashier sitting', 'Activity' : 'Seated', 'Expiration' : {'Speaking':5,'Breathing':5}},
                {'Group':'Store and Retail','Id':'Vendor_standing', 'Name' : 'Vendor standing', 'Activity' : 'Standing', 'Expiration' : {'Speaking':5,'Breathing':5}},
                {'Group':'Sport','Id':'Musculation', 'Name' : 'Musculation', 'Activity' : 'Heavy exercise', 'Expiration' : {'Speaking':1,'Breathing':9}},
                {'Group':'Sport','Id':'Floor_gymnastics', 'Name' : 'Floor gymnastics', 'Activity' : 'Moderate exercise', 'Expiration' : {'Speaking':1,'Breathing':8, "Shouting":1}},
                {'Group':'Sport','Id':'Team_competition', 'Name' : 'Team competition', 'Activity' : 'Heavy exercise', 'Expiration' : {'Speaking':0.5,'Breathing':8, "Shouting":1.5}},
                {'Group':'Miscellaneous','Id':'Trip_in_elevator', 'Name' : 'Trip in elevator', 'Activity' : 'Standing', 'Expiration' : {'Speaking':1,'Breathing':9}},
                {'Group':'Navy','Id':'Watch_seated', 'Name' : 'Watch seated', 'Activity' : 'Seated', 'Expiration' : {'Shouting': 10, 'Speaking': 30, 'Breathing': 60}}, # Manning a console seating in front of it
                {'Group':'Navy','Id':'Watch_standing', 'Name' : 'Watch standing', 'Activity' : 'Light activity', 'Expiration' : {'Shouting': 20, 'Speaking': 30, 'Breathing': 50}}] # Pacing and moving from station to station, giving orders and looking at data at stations

# ------------------ Validation ----------------------

MECHANICAL_VENTILATION_TYPES = {'mech_type_air_changes', 'mech_type_air_supply', 'not-applicable'}
MASK_TYPES = {'Type_I', 'FFP2'}
MASK_WEARING_OPTIONS = {'mask_on', 'mask_off'}
VENTILATION_TYPES = {'natural_ventilation', 'mechanical_ventilation', 'no_ventilation'}
VIRUS_TYPES = {'SARS_CoV_2', 'SARS_CoV_2_ALPHA', 'SARS_CoV_2_BETA','SARS_CoV_2_GAMMA', 'SARS_CoV_2_DELTA', 'SARS_CoV_2_OMICRON'}
VOLUME_TYPES = {'room_volume_explicit', 'room_volume_from_dimensions'}
WINDOWS_OPENING_REGIMES = {'windows_open_permanently', 'windows_open_periodically', 'not-applicable'}
WINDOWS_TYPES = {'window_sliding', 'window_hinged', 'not-applicable'}

COFFEE_OPTIONS_INT = {'coffee_break_0': 0, 'coffee_break_1': 1, 'coffee_break_2': 2, 'coffee_break_4': 4}

MONTH_NAMES = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December',
]