var js_default = JSON.parse('{"exposed_activity_type": "Office_worker", "exposed_activity_level": "Seated", "exposed_breathing": 8, "exposed_speaking": 2, "exposed_shouting": 0, "exposed_mask_wear_ratio": 0.7, "infected_activity_type": "Office_worker", "infected_activity_level": "Seated", "infected_breathing": 8, "infected_speaking": 2, "infected_shouting": 0, "infected_mask_wear_ratio": 0.7, "air_changes": 1.0, "air_supply": 100, "calculator_version": "1.0.3", "ceiling_height": 2.5, "humidity": "", "inside_temp": 20, "exposed_coffee_break_option": "coffee_break_0", "exposed_coffee_duration": 5, "exposed_finish": "17:30", "exposed_lunch_finish": "13:30", "exposed_lunch_option": 1, "exposed_lunch_start": "12:30", "exposed_start": "08:30", "event_month": "January", "floor_area": 40, "biov_amount": 1000, "biov_option": 0, "infected_coffee_break_option": "coffee_break_0", "infected_coffee_duration": 5, "infected_dont_have_breaks_with_exposed": 0, "infected_finish": "17:30", "infected_lunch_finish": "13:30", "infected_lunch_option": 1, "infected_lunch_start": "12:30", "infected_people": 1, "infected_start": "08:30", "location_latitude": 47.21725, "location_longitude": -1.55336, "location_name": "Nantes, Loire-Atlantique, Pays de la Loire, FRA", "mask_type": "Type_I", "mask_wearing_option": "mask_off", "mechanical_ventilation_type": "mech_type_air_supply", "opening_distance": 0.5, "room_heating_option": 1, "room_number": "1", "room_volume": 100, "simulation_name": "My simulation", "total_people": 10, "ventilation_type": "mechanical_ventilation", "virus_type": "SARS_CoV_2_OMICRON", "viruses": {"SARS_CoV_2": "SARS-CoV-2 (nominal strain)", "SARS_CoV_2_ALPHA": "SARS-CoV-2 (Alpha VOC)", "SARS_CoV_2_BETA": "SARS-CoV-2 (Beta VOC)", "SARS_CoV_2_GAMMA": "SARS-CoV-2 (Gamma VOC)", "SARS_CoV_2_DELTA": "SARS-CoV-2 (Delta VOC)", "SARS_CoV_2_OMICRON": "SARS-CoV-2 (Omicron VOC)"}, "volume_type": "room_volume_explicit", "window_type": "window_sliding", "window_height": 1.0, "window_width": 1.0, "windows_duration": 15, "windows_frequency": 60, "windows_number": 1, "window_opening_regime": "windows_open_permanently"}');
var js_expiration = JSON.parse('{"Office_worker_breathing": 8, "Office_worker_speaking": 2, "Office_worker_activity_level": "Seated", "Workshop_worker_breathing": 1.5, "Workshop_worker_shouting": 1.5, "Workshop_worker_speaking": 7, "Workshop_worker_activity_level": "Moderate activity", "Meeting_participant_breathing": 8, "Meeting_participant_shouting": 0.5, "Meeting_participant_speaking": 1.5, "Meeting_participant_activity_level": "Seated", "Meeting_leader_breathing": 6, "Meeting_leader_shouting": 1, "Meeting_leader_speaking": 3, "Meeting_leader_activity_level": "Standing", "Hospital_patient_breathing": 9.5, "Hospital_patient_speaking": 0.5, "Hospital_patient_activity_level": "Seated", "Nurse_working_breathing": 8, "Nurse_working_speaking": 2, "Nurse_working_activity_level": "Light activity", "Physician_working_breathing": 5, "Physician_working_speaking": 5, "Physician_working_activity_level": "Standing", "Student_sitting_breathing": 9.5, "Student_sitting_speaking": 0.5, "Student_sitting_activity_level": "Seated", "Professor_teaching_breathing": 2, "Professor_teaching_shouting": 2, "Professor_teaching_speaking": 6, "Professor_teaching_activity_level": "Standing", "Professor_conferencing_breathing": 2, "Professor_conferencing_shouting": 6, "Professor_conferencing_speaking": 2, "Professor_conferencing_activity_level": "Light activity", "Concert_musician_soft_music_breathing": 9.5, "Concert_musician_soft_music_speaking": 0.5, "Concert_musician_soft_music_activity_level": "Standing", "Concert_musician_rock_breathing": 8, "Concert_musician_rock_shouting": 1, "Concert_musician_rock_speaking": 1, "Concert_musician_rock_activity_level": "Moderate activity", "Concert_singer_rock_breathing": 2, "Concert_singer_rock_shouting": 7, "Concert_singer_rock_speaking": 1, "Concert_singer_rock_activity_level": "Moderate activity", "Concert_spectator_standing_breathing": 8, "Concert_spectator_standing_shouting": 1, "Concert_spectator_standing_speaking": 1, "Concert_spectator_standing_activity_level": "Light activity", "Concert_spectator_sitting_breathing": 9, "Concert_spectator_sitting_shouting": 0.5, "Concert_spectator_sitting_speaking": 0.5, "Concert_spectator_sitting_activity_level": "Seated", "Museum_visitor_breathing": 9, "Museum_visitor_speaking": 1, "Museum_visitor_activity_level": "Standing", "Theater_spectator_breathing": 9, "Theater_spectator_shouting": 0.5, "Theater_spectator_speaking": 0.5, "Theater_spectator_activity_level": "Seated", "Theater_actor_breathing": 7, "Theater_actor_shouting": 3, "Theater_actor_activity_level": "Moderate activity", "Conferencer_breathing": 2, "Conferencer_shouting": 6, "Conferencer_speaking": 2, "Conferencer_activity_level": "Light activity", "Conference_attendee_breathing": 9.5, "Conference_attendee_speaking": 0.5, "Conference_attendee_activity_level": "Seated", "Guest_standing_breathing": 6, "Guest_standing_shouting": 2, "Guest_standing_speaking": 2, "Guest_standing_activity_level": "Standing", "Guest_sitting_breathing": 6, "Guest_sitting_speaking": 4, "Guest_sitting_activity_level": "Seated", "Server_breathing": 8, "Server_speaking": 2, "Server_activity_level": "Light activity", "Barrista_breathing": 6, "Barrista_shouting": 2, "Barrista_speaking": 2, "Barrista_activity_level": "Standing", "Nightclub_dancing_breathing": 9, "Nightclub_dancing_shouting": 1, "Nightclub_dancing_activity_level": "Moderate activity", "Nightclub_sitting_breathing": 8, "Nightclub_sitting_shouting": 2, "Nightclub_sitting_activity_level": "Seated", "Customer_standing_breathing": 9, "Customer_standing_speaking": 1, "Customer_standing_activity_level": "Standing", "Cashier_sitting_breathing": 5, "Cashier_sitting_speaking": 5, "Cashier_sitting_activity_level": "Seated", "Vendor_standing_breathing": 5, "Vendor_standing_speaking": 5, "Vendor_standing_activity_level": "Standing", "Musculation_breathing": 9, "Musculation_speaking": 1, "Musculation_activity_level": "Heavy exercise", "Floor_gymnastics_breathing": 8, "Floor_gymnastics_shouting": 1, "Floor_gymnastics_speaking": 1, "Floor_gymnastics_activity_level": "Moderate activity", "Team_competition_breathing": 8, "Team_competition_shouting": 1.5, "Team_competition_speaking": 0.5, "Team_competition_activity_level": "Heavy exercise", "Trip_in_elevator_breathing": 9, "Trip_in_elevator_speaking": 1, "Trip_in_elevator_activity_level": "Standing", "Watch_seated_breathing": 60, "Watch_seated_shouting": 10, "Watch_seated_speaking": 30, "Watch_seated_activity_level": "Seated", "Watch_standing_breathing": 50, "Watch_standing_shouting": 20, "Watch_standing_speaking": 30, "Watch_standing_activity_level": "Light activity"}');


/* -------HTML structure------- */
function getChildElement(elem) {
  // Get the element named in the given element's data-enables attribute.
  return $(elem.data("enables"));
}

function insertErrorFor(referenceNode, text) {
  var element = document.createElement("span");
  element.setAttribute("class", "error_text");
  element.classList.add("red_text");
  element.innerHTML = "&nbsp;&nbsp;" + text;
  referenceNode.parentNode.insertBefore(element, referenceNode.nextSibling);
}

function removeErrorFor(referenceNode) {
  $(referenceNode).next('span.error_text').remove();
}

/* -------Required fields------- */
function require_fields(obj) {
  switch ($(obj).attr('id')) {
    case "room_data_volume":
      require_room_volume(true);
      require_room_dimensions(false);
      break;
    case "room_data_dimensions":
      require_room_volume(false);
      require_room_dimensions(true);
      break;
    case "mechanical_ventilation":
      require_mechanical_ventilation(true);
      require_natural_ventilation(false);
      break;
    case "natural_ventilation":
      require_mechanical_ventilation(false);
      require_natural_ventilation(true);
      break;
    case "window_sliding":
      require_window_width(false);
      break;
    case "window_hinged":
      require_window_width(true);
      break;
    case "mech_type_air_changes":
      require_air_changes(true);
      require_air_supply(false);
      break;
    case "mech_type_air_supply":
      require_air_changes(false);
      require_air_supply(true);
      break;
    case "windows_open_periodically":
      require_venting(true);
      break;
    case "windows_open_permanently":
      require_venting(false);
      break;
    case "biov_yes":
      require_biov(true);
      break;
    case "biov_no":
      require_biov(false);
      break;
    case "mask_on":
      require_mask(true);
      break;
    case "mask_off":
      require_mask(false);
      break;
    case "exposed_lunch_option_no":
    case "infected_lunch_option_no":
      require_lunch($(obj).attr('id'), false);
      break;
    case "exposed_lunch_option_yes":
    case "infected_lunch_option_yes":
      require_lunch($(obj).attr('id'), true);
      break;
    default:
      break;
  }
}

function unrequire_fields(obj) {
  switch (obj.id) {
    case "mechanical_ventilation":
      require_mechanical_ventilation(false);
      break;
    case "natural_ventilation":
      require_natural_ventilation(false);
      break;
    default:
      break;
  }
}

function require_room_volume(option) {
  require_input_field("#room_volume", option);
  set_disabled_status("#room_volume", !option);
}

function require_room_dimensions(option) {
  require_input_field("#floor_area", option);
  require_input_field("#ceiling_height", option);
  set_disabled_status("#floor_area", !option);
  set_disabled_status("#ceiling_height", !option);
}

function require_mechanical_ventilation(option) {
  $("#mech_type_air_changes").prop('required', option);
  $("#mech_type_air_supply").prop('required', option);
  if (!option) {
    require_input_field("#air_changes", option);
    require_input_field("#air_supply", option);
  }
}

function require_natural_ventilation(option) {
  require_input_field("#windows_number", option);
  require_input_field("#window_height", option);
  require_input_field("#opening_distance", option);
  $("#window_sliding").prop('required', option);
  $("#window_hinged").prop('required', option);
  $("#windows_open_permanently").prop('required', option);
  $("#windows_open_periodically").prop('required', option);
  if (!option) {
    require_input_field("#window_width", option);
    require_input_field("#windows_duration", option);
    require_input_field("#windows_frequency", option);
  }
}

function require_window_width(option) {
  require_input_field("#window_width", option);
  set_disabled_status("#window_width", !option);
}

function require_air_changes(option) {
  require_input_field("#air_changes", option);
  set_disabled_status("#air_changes", !option);
}

function require_air_supply(option) {
  require_input_field("#air_supply", option);
  set_disabled_status("#air_supply", !option);
}

function require_venting(option) {
  require_input_field("#windows_duration", option);
  require_input_field("#windows_frequency", option);
  set_disabled_status("#windows_duration", !option);
  set_disabled_status("#windows_frequency", !option);
}

function require_lunch(id, option) {
  var activity = $(document.getElementById(id)).data('lunch-select');
  var startObj = $(".start_time[data-lunch-for='"+activity+"']")[0];
  var startID = '#'+$(startObj).attr('id');
  var finishObj = $(".finish_time[data-lunch-for='"+activity+"']")[0];
  var finishID = '#'+$(finishObj).attr('id');

  require_input_field(startID, option);
  require_input_field(finishID, option);
  set_disabled_status(startID, !option);
  set_disabled_status(finishID, !option);

  if (!option) {
    $(finishID).removeClass("red_border finish_time_error lunch_break_error");
    removeErrorFor(finishObj);
  }
  else {
    if (startObj.value === "" && finishObj.value === "") {
      startObj.value = "12:30";
      finishObj.value = "13:30";
    }
    validateLunchBreak($(startObj).data('time-group'));
  }
}

function require_mask(option) {
  $("#mask_type_1").prop('required', option);
  $("#mask_type_ffp2").prop('required', option);
}

function require_biov(option) {
  require_input_field("#biov_amount", option);
}

function require_input_field(id, option) {
  $(id).prop('required', option);
  if (!option) {
    removeInvalid(id);
  }
}

function set_disabled_status(id, option) {
  if (option)
    $(id).addClass("disabled");
  else
    $(id).removeClass("disabled");
}

function setMaxInfectedPeople() {
  $("#training_limit_error").hide();
  var max = $("#total_people").val()

  if ($("#activity_type").val() === "training") {
    max = 1;
    $("#training_limit_error").show();
  }

  $("#infected_people").attr("max", max);
}

function removeInvalid(id) {
  if ($(id).hasClass("red_border")) {
    $(id).val("");
    $(id).removeClass("red_border");
    removeErrorFor(id);
  }
}

function on_ventilation_type_change() {
  ventilation_types = $('input[type=radio][name=ventilation_type]');
  ventilation_types.each(function (index) {
    if (this.checked) {
      getChildElement($(this)).show();
      require_fields(this);
    } else {
      getChildElement($(this)).hide();
      unrequire_fields(this);

      //Clear invalid inputs for this newly hidden child element
      removeInvalid("#"+getChildElement($(this)).find('input').not('input[type=radio]').attr('id'));
    }
  });
}

/* -------UI------- */

function show_disclaimer() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}

$("[data-has-radio]").on('click', function(event){
  $($(this).data("has-radio")).click();
});

$("[data-has-radio]").on('change', function(event){
  $($(this).data("has-radio")).click();
});

function toggle_split_breaks() {
  $("#DIVinfected_breaks").toggle(this.checked);
  $("#exposed_break_title").toggle(this.checked);
  require_lunch("infected_lunch_option_yes", document.getElementById("infected_dont_have_breaks_with_exposed").checked);
}

/* -------Form validation------- */
function validate_form(form) {
  var submit = true;

  // Activity times and lunch break times are co-dependent
  // -> So if 1 fails it doesn't make sense to check the rest

  //Validate all finish times
  $("input[required].finish_time").each(function() {
    var activity = $(this).data('lunch-for');
    if (document.getElementById("infected_dont_have_breaks_with_exposed").checked || activity!="infected") {
      if (!validateFinishTime(this)) {
        submit = false;
      }
    }
  });

  //Validate all lunch breaks
  if (submit) {
    $("input[required].start_time[data-lunch-for]").each(function() {
      var activity = $(this).data('lunch-for');
      if (document.getElementById("infected_dont_have_breaks_with_exposed").checked || activity!="infected") {
        if (!validateLunchBreak($(this).data('time-group'))) {
          submit = false;
        }
      }
    });
  }

  //Validate expiration

  if (submit) {
    if (!validateExpiration("exposed")) {
      submit = false;
    }
    if (!validateExpiration("infected")) {
      submit = false;
    }
  }

  //Check if breaks length >= activity length
  if (submit) {
    $("[data-lunch-for]").each(function() {
      var activity = $(this).data('lunch-for');
      if (document.getElementById("infected_dont_have_breaks_with_exposed").checked || activity!="infected") {
        var activityBreaksObj= document.getElementById("activity_breaks");
        removeErrorFor(activityBreaksObj);

        var lunch_mins = 0;
        if (document.getElementById(activity+"_lunch_option_yes").checked) {
          var lunch_start = document.getElementById(activity+"_lunch_start");
          var lunch_finish = document.getElementById(activity+"_lunch_finish");
          lunch_mins = parseTimeToMins(lunch_finish.value) - parseTimeToMins(lunch_start.value);
        }

        var coffee_breaks = parseInt(document.querySelector('input[name="'+activity+'_coffee_break_option"]:checked').value);
        var coffee_duration = parseInt(document.getElementById(activity+"_coffee_duration").value);
        var coffee_mins = coffee_breaks * coffee_duration;
        
        var activity_start = document.getElementById(activity+"_start");
        var activity_finish = document.getElementById(activity+"_finish");
        var activity_mins = parseTimeToMins(activity_finish.value) - parseTimeToMins(activity_start.value);

        if ((lunch_mins + coffee_mins) >= activity_mins) {
          insertErrorFor(activityBreaksObj, "Length of breaks >= Length of "+activity+" presence");
          submit = false;
        }
      }
    });
  }

  // Validate location input.
  if (submit) {
      // We make the non-visible location inputs mandatory, without marking them as "required" inputs.
      // See https://stackoverflow.com/q/22148080/741316 for motivation.
      var locationSelectObj= document.getElementById("location_select");
      removeErrorFor(locationSelectObj);
      $("input[name*='location']").each(function() {
        el = $(this);
        if ($.trim(el.val()) == ''){
          submit = false;
        }
      });

      if (!submit) {
        insertErrorFor(locationSelectObj, "Please select a location");
      }
  }

  //Validate all non zero values
  $("input[required].non_zero").each(function() {
    if (!validateValue(this)) {
      submit = false;
    }
  });

  //Validate window venting duration < venting frequency
  if (!$("#windows_duration").hasClass("disabled")) {
    var windowsDurationObj = document.getElementById("windows_duration");
    var windowsFrequencyObj = document.getElementById("windows_frequency");
    removeErrorFor(windowsFrequencyObj);

    if (parseInt(windowsDurationObj.value) >= parseInt(windowsFrequencyObj.value)) {
      insertErrorFor(windowsFrequencyObj, "Duration >= Frequency");
      submit = false;
    }
  }

  if (submit) {
    $("#generate_report").prop("disabled", true);
    //Add spinner to button
    $("#generate_report").html(
      `<span id="loading_spinner" class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...`
    );
  }


  return submit;
}

function validateValue(obj) {
  $(obj).removeClass("red_border");
  removeErrorFor(obj);

  if (!isLessThanZeroOrEmpty($(obj).val())) {
    $(obj).addClass("red_border");
    insertErrorFor(obj, "Value must be > 0");
    return false;
  }
  return true;
}

function isLessThanZeroOrEmpty(value) {
  if (value === "") return true;
  if (value <= 0)
    return false;
  return true;
}

function validateDate(obj) {
  $(obj).removeClass("red_border");
  removeErrorFor(obj);

  if (!isValidDateOrEmpty($(obj).val())) {
    $(obj).addClass("red_border");
    insertErrorFor(obj, "Incorrect date format");
    return false;
  }
  return true;
}

function isValidDateOrEmpty(date) {
  if (date === "") return true;
  var matches = /^(\d+)[-\/](\d+)[-\/](\d+)$/.exec(date);
  if (matches == null) return false;
  var d = matches[1];
  var m = matches[2];
  var y = matches[3];
  if (y > 2100 || y < 1900) return false;
  var composedDate = new Date(y + '/' + m + '/' + d);
  return composedDate.getDate() == d && composedDate.getMonth() + 1 == m && composedDate.getFullYear() == y;
}

function validateFinishTime(obj) {
  var groupID = $(obj).data('time-group');
  var startObj = $(".start_time[data-time-group='"+groupID+"']")[0];
  var finishObj = $(".finish_time[data-time-group='"+groupID+"']")[0];

  if ($(finishObj).hasClass("finish_time_error")) {
    $(finishObj).removeClass("red_border finish_time_error");
    removeErrorFor(finishObj);
  }

  //Check if finish time error (takes precedence over lunch break error)
  var startTime = parseValToNumber(startObj.value);
  var finishTime = parseValToNumber(finishObj.value);
  if (startTime >= finishTime) {
    $(finishObj).addClass("red_border finish_time_error");
    removeErrorFor(finishObj);
    insertErrorFor(finishObj, "Finish time must be after start");
    return false;
  }
  return true;
}

function validateLunchBreak(lunchGroup) {
  //Valid if lunch break not selected
  if(document.getElementById(lunchGroup+"_option_no").checked)
    return true;

  var lunchStartObj = $(".start_time[data-time-group='"+lunchGroup+"']")[0];
  var lunchFinishObj = $(".finish_time[data-time-group='"+lunchGroup+"']")[0];

  //Skip if finish time error present (it takes precedence over lunch break error)
  if ($(lunchStartObj).hasClass("finish_time_error") || $(lunchFinishObj).hasClass("finish_time_error"))
    return false;

  removeErrorFor(lunchFinishObj);
  var valid = validateLunchTime(lunchStartObj) & validateLunchTime(lunchFinishObj);
  if (!valid) {
    insertErrorFor(lunchFinishObj, "Lunch break must be within presence times");
  }

  return valid;
}

function validateExpiration(infected_state) {
  removeErrorFor(document.getElementById(infected_state + 'Expiration'));
  if (document.getElementById(infected_state + '_activity_breathing').value + document.getElementById(infected_state + '_activity_speaking').value +  document.getElementById(infected_state + '_activity_shouting').value == 0){
    insertErrorFor(document.getElementById(infected_state + 'Expiration'),"Expiration sum must be > 0")
    return false
  } 

  return true

}

//Check if exposed/infected lunch time within exposed/infected presence times
function validateLunchTime(obj) {
  var activityGroup = $(obj).data('lunch-for');
  var activityStart = parseValToNumber($(".start_time[data-time-group='"+activityGroup+"']")[0].value);
  var activityFinish = parseValToNumber($(".finish_time[data-time-group='"+activityGroup+"']")[0].value);

  var time = parseValToNumber(obj.value);
  $(obj).removeClass("red_border lunch_break_error");
  if ((time < activityStart) || (time > activityFinish)) {
    $(obj).addClass("red_border lunch_break_error");
    return false;
  }

  return true;
}

function parseValToNumber(val) {
  return parseInt(val.replace(':',''), 10);
}

function parseTimeToMins(cTime) {
  var time = cTime.match(/(\d+):(\d+)/);
  return parseInt(time[1]*60) + parseInt(time[2]);
}

// Prevent spinner when clicking on back button
window.onpagehide = function(){
  $('loading_spinner').remove();
  $("#generate_report").prop("disabled", false).html(`Generate report`);
};

/* -------On Load------- */
$(document).ready(function () {

  // Check default values
  var volume_type = js_default["volume_type"]
  $('.room_volume[value='+volume_type+']').attr('checked', 'checked');
  var heating_system = js_default['room_heating_option']
  $('.heating_option[value='+heating_system+']').attr('checked', 'checked');
  var ventilation_type = js_default['ventilation_type']
  $('.ventilation_option[value='+ventilation_type+']').attr('checked', 'checked');
  var mechanical_ventilation_type = js_default['mechanical_ventilation_type']
  $('.mech_type_option[value='+mechanical_ventilation_type+']').attr('checked', 'checked');
  var window_type = js_default['window_type']
  $('.window_type_option[value='+window_type+']').attr('checked', 'checked');
  var window_opening_regime = js_default['window_opening_regime']
  $('.window_open_option[value='+window_opening_regime+']').attr('checked', 'checked');
  var biov_option = js_default['biov_option']
  $('.biov_option[value='+biov_option+']').attr('checked', 'checked');
  var mask_wearing_option = js_default['mask_wearing_option']
  $('.mask_wearing_option[value='+mask_wearing_option+']').attr('checked', 'checked');
  var mask_type = js_default['mask_type']
  $('.mask_type_option[value='+mask_type+']').attr('checked', 'checked');
  var infected_dont_have_breaks_with_exposed = js_default['infected_dont_have_breaks_with_exposed']
  $('.infected_dont_have_breaks_with_exposed_option[value='+infected_dont_have_breaks_with_exposed+']').attr('checked', 'checked');
  var exposed_coffee_break_option = js_default['exposed_coffee_break_option']
  $('.exposed_coffee_break_option[value='+exposed_coffee_break_option+']').attr('checked', 'checked');
  var exposed_lunch_option = js_default['exposed_lunch_option']
  $('.exposed_lunch_option[value='+exposed_lunch_option+']').attr('checked', 'checked');
  var infected_lunch_option = js_default['infected_lunch_option']
  $('.infected_lunch_option[value='+infected_lunch_option+']').attr('checked', 'checked');
  var infected_coffee_break_option = js_default['infected_coffee_break_option']
  $('.infected_coffee_break_option[value='+infected_coffee_break_option+']').attr('checked', 'checked');

    //Set humidity value according to heating option

  if($("#heating_no").is(':checked')){
      $("#humidity").val(0.5)
    }
  if($("#heating_yes").is(':checked')){
      $("#humidity").val(0.3)
    }
  
  $("#heating_no").change(function() {
      if(this.checked) {
          $("#humidity").val(0.5)
      }
    });
  
  $("#heating_yes").change(function() {
      if(this.checked) {
          $("#humidity").val(0.3)
      }
    });

        // Update expiration on change
    $("#exposed_activity_type").change(function() {
      document.getElementById('exposed_activity_breathing').value = js_expiration[this.value+"_breathing"] || 0 
    })
    $("#exposed_activity_type").change(function() {
      document.getElementById('exposed_activity_speaking').value = js_expiration[this.value+"_speaking"] || 0 
    })
    $("#exposed_activity_type").change(function() {
      document.getElementById('exposed_activity_shouting').value = js_expiration[this.value+"_shouting"]  || 0
    })
    $("#infected_activity_type").change(function() {
      document.getElementById('infected_activity_breathing').value = js_expiration[this.value+"_breathing"] || 0 
    })
    $("#infected_activity_type").change(function() {
      document.getElementById('infected_activity_speaking').value = js_expiration[this.value+"_speaking"] || 0 
    })
    $("#infected_activity_type").change(function() {
      document.getElementById('infected_activity_shouting').value = js_expiration[this.value+"_shouting"]  || 0
    })
    $("#exposed_activity_type").change(function() {
      document.getElementById('exposed_activity_level').value = js_expiration[this.value+"_activity_level"]
    })
    $("#infected_activity_type").change(function() {
      document.getElementById('infected_activity_level').value = js_expiration[this.value+"_activity_level"]
    })

  var url = new URL(decodeURIComponent(window.location.href));
  //Pre-fill form with known values
  url.searchParams.forEach((value, name) => {
    //If element exists
    if(document.getElementsByName(name).length > 0) {
      var elemObj = document.getElementsByName(name)[0];

      //Pre-select checked radios
      if (elemObj.type === 'radio') {
        // Calculator <= 1.5.0 used to send not-applicable in the URL for radios that
        // weren't set. Now those are not sent at all, but we keep the behaviour for compatibility.
        if (value !== 'not-applicable') {
          $('[name="'+name+'"][value="'+value+'"]').prop('checked',true);
        }
      }
      //Pre-select checkboxes
      else if (elemObj.type === 'checkbox') {
        elemObj.checked = (value==1);
      }

      //Ignore 0 (default) values from server side
      else if (!(elemObj.classList.contains("non_zero") || elemObj.classList.contains("remove_zero")) || (value != "0.0" && value != "0")) {
        elemObj.value = value;
        validateValue(elemObj);
      }
    }
  });

  // Handle default URL values if they are not explicitly defined.
  if (Array.from(url.searchParams).length > 0) {
    if (!url.searchParams.has('location_name')) {
      $('[name="location_name"]').val('Geneva')
      $('[name="location_select"]').val('Geneva')
    }
    if (!url.searchParams.has('location_latitude')) {
      $('[name="location_latitude"]').val('46.20833')
    }
    if (!url.searchParams.has('location_longitude')) {
      $('[name="location_longitude"]').val('6.14275')
    }
  }


  // When the document is ready, deal with the fact that we may be here
  // as a result of a forward/back browser action. If that is the case, update
  // the visibility of some of our inputs.

  // Chrome fix - on back button infected break DIV not shown
  if (document.getElementById("infected_dont_have_breaks_with_exposed").checked) {
    $("#DIVinfected_breaks").show();
    $("#exposed_break_title").show();
    require_lunch("infected_lunch_option_yes", true);
  }

  //Check all radio buttons previously selected
  $("input[type=radio]:checked").each(function() {require_fields(this)});

  // When the ventilation_type changes we want to make its respective
  // children show/hide.
  $("input[type=radio][name=ventilation_type]").change(on_ventilation_type_change);
  // Call the function now to handle forward/back button presses in the browser.
  on_ventilation_type_change();

  // Setup the maximum number of people at page load (to handle back/forward),
  // and update it when total people is changed.
  setMaxInfectedPeople();
  $("#total_people").change(setMaxInfectedPeople);
  $("#activity_type").change(setMaxInfectedPeople);

  //Validate all non zero values
  $("input[required].non_zero").each(function() {validateValue(this)});
  $(".non_zero").change(function() {validateValue(this)});

  //Validate all finish times
  $("input[required].finish_time").each(function() {validateFinishTime(this)});
  $(".finish_time").change(function() {validateFinishTime(this)});
  $(".start_time").change(function() {validateFinishTime(this)});

  //Validate expiration
  $("#exposed_activity_breathing").change(function(){validateExpiration("exposed")});
  $("#exposed_activity_speaking").change(function(){validateExpiration("exposed")});
  $("#exposed_activity_shouting").change(function(){validateExpiration("exposed")});
  $("#infected_activity_breathing").change(function(){validateExpiration("infected")});
  $("#infected_activity_speaking").change(function(){validateExpiration("infected")});
  $("#infected_activity_shouting").change(function(){validateExpiration("infected")});

  //Validate lunch times
  $(".start_time[data-lunch-for]").each(function() {validateLunchBreak($(this).data('time-group'))});
  $("[data-lunch-for]").change(function() {validateLunchBreak($(this).data('time-group'))});
  $("[data-lunch-break]").change(function() {validateLunchBreak($(this).data('lunch-break'))});

  $("#location_select").select2({
    ajax: {
      // Docs for the geocoding service at:
      // https://developers.arcgis.com/rest/geocode/api-reference/geocoding-service-output.htm
      url: "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/suggest",
      dataType: 'json',
      delay: 250,
      data: function(params) {
        return {
          text: params.term, // search term
          f: 'json',
          page: params.page,
          maxSuggestions: 20,
        };
      },
      processResults: function(data, params) {
        // Enable infinite scrolling
        params.page = params.page || 1;
        return {
          results: data.suggestions.map(function(suggestion) {
            return {
                id: suggestion.magicKey,  // The unique reference to this result.
                text: suggestion.text,
                magicKey: suggestion.magicKey
            }
          }),
          pagination: {
            more: (params.page * 10) < data.suggestions.length
          }
        };
      },
      cache: true
    },
    placeholder: 'Geneva, CHE',
    minimumInputLength: 1,
    templateResult: formatlocation,
    templateSelection: formatLocationSelection
  });

  function formatlocation(suggestedLocation) {
    // Function is called for each location from the geocoding API.

    if (suggestedLocation.loading) {
      // Update the first message in the search results to show the
      // "Searching..." message.
      return suggestedLocation.text;
    }

    // Create a container for this location (to be added to the DOM by the select2
    // library when returned).
    // This will become one of many search results in the dropdown.
    var $container = $(
      "<div class='select2-result-location clearfix'>" +
      "<div class='select2-result-location__meta'>" +
      "<div class='select2-result-location__title'>" + suggestedLocation.text + "</div>" +
      "</div>" +
      "</div>"
    );
    return $container;
  }

  function formatLocationSelection(selectedSuggestion) {
    // Function is called when a selection is made in the search result dropdown.

    // ID may be empty, for example when the page is refreshed or back button pressed.
    if (selectedSuggestion.id != "") {

        // Turn the suggestion into a proper location (so that we can get its latitude & longitude).
        $.ajax({
          dataType: "json",
          url: 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates',
          data: {
            magicKey: selectedSuggestion.magicKey,
            outFields: 'country, location',
            f: "json"
          },
          success: function (locations) {
            // If there isn't precisely one result something is very wrong.
            geocoded_loc = locations.candidates[0];
            $('input[name="location_name"]').val(selectedSuggestion.text);
            $('input[name="location_latitude"]').val(geocoded_loc.location.y.toPrecision(7));
            $('input[name="location_longitude"]').val(geocoded_loc.location.x.toPrecision(7));
          }
        });

    } else if ($('input[name="location_name"]').val() != "") {
        // If we have no selection AND the location_name is available, use that in the search bar.
        // This means that we preserve the location through refresh/back button.
        return $('input[name="location_name"]').val();
    }
    return selectedSuggestion.text;
  }
});



/* -------Debugging------- */
function debug_submit(form) {

  //Prevent default posting of form - put here to work in case of errors
  event.preventDefault();

  //Serialize the data in the form
  var serializedData = objectifyForm($(form).serializeArray());

  console.log(serializedData);

  return false; //don't submit
}

function objectifyForm(formArray) {
  var returnArray = {};
  for (var i = 0; i < formArray.length; i++)
    returnArray[formArray[i]['name']] = formArray[i]['value'];
  return returnArray;
}
