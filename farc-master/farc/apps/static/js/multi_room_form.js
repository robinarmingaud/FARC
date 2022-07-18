var js_default = JSON.parse('{"exposed_activity_type": "Office_worker", "exposed_activity_level": "Seated", "exposed_breathing": 8, "exposed_speaking": 2, "exposed_shouting": 0, "exposed_mask_wear_ratio": 0.7, "infected_activity_type": "Office_worker", "infected_activity_level": "Seated", "infected_breathing": 8, "infected_speaking": 2, "infected_shouting": 0, "infected_mask_wear_ratio": 0.7, "air_changes": 1.0, "air_supply": 100, "calculator_version": "1.0.3", "ceiling_height": 2.5, "humidity": 0.3, "inside_temp": 20, "exposed_coffee_break_option": "coffee_break_0", "exposed_coffee_duration": 5, "exposed_finish": "17:30", "exposed_lunch_finish": "13:30", "exposed_lunch_option": 1, "exposed_lunch_start": "12:30", "exposed_start": "08:30", "event_month": "January", "floor_area": 40, "biov_amount": 1000, "biov_option": 0, "infected_coffee_break_option": "coffee_break_0", "infected_coffee_duration": 5, "infected_dont_have_breaks_with_exposed": 0, "infected_finish": "17:30", "infected_lunch_finish": "13:30", "infected_lunch_option": 1, "infected_lunch_start": "12:30", "infected_people": 1, "infected_start": "08:30", "location_latitude": 47.21725, "location_longitude": -1.55336, "location_name": "Nantes, Loire-Atlantique, Pays de la Loire, FRA", "mask_type": "Type_I", "mask_wearing_option": "mask_off", "mechanical_ventilation_type": "mech_type_air_supply", "opening_distance": 0.5, "room_heating_option": 1, "room_number": "My room", "room_volume": 100, "simulation_name": "My simulation", "total_people": 10, "ventilation_type": "mechanical_ventilation", "virus_type": "SARS_CoV_2_OMICRON", "viruses": {"SARS_CoV_2": "SARS-CoV-2 (nominal strain)", "SARS_CoV_2_ALPHA": "SARS-CoV-2 (Alpha VOC)", "SARS_CoV_2_BETA": "SARS-CoV-2 (Beta VOC)", "SARS_CoV_2_GAMMA": "SARS-CoV-2 (Gamma VOC)", "SARS_CoV_2_DELTA": "SARS-CoV-2 (Delta VOC)", "SARS_CoV_2_OMICRON": "SARS-CoV-2 (Omicron VOC)"}, "volume_type": "room_volume_explicit", "window_type": "window_sliding", "window_height": 1.0, "window_width": 1.0, "windows_duration": 15, "windows_frequency": 60, "windows_number": 1, "window_opening_regime": "windows_open_permanently"}');
var js_expiration = JSON.parse('{"Office_worker_breathing": 8, "Office_worker_speaking": 2, "Office_worker_activity_level": "Seated", "Workshop_worker_breathing": 1.5, "Workshop_worker_shouting": 1.5, "Workshop_worker_speaking": 7, "Workshop_worker_activity_level": "Moderate activity", "Meeting_participant_breathing": 8, "Meeting_participant_shouting": 0.5, "Meeting_participant_speaking": 1.5, "Meeting_participant_activity_level": "Seated", "Meeting_leader_breathing": 6, "Meeting_leader_shouting": 1, "Meeting_leader_speaking": 3, "Meeting_leader_activity_level": "Standing", "Hospital_patient_breathing": 9.5, "Hospital_patient_speaking": 0.5, "Hospital_patient_activity_level": "Seated", "Nurse_working_breathing": 8, "Nurse_working_speaking": 2, "Nurse_working_activity_level": "Light activity", "Physician_working_breathing": 5, "Physician_working_speaking": 5, "Physician_working_activity_level": "Standing", "Student_sitting_breathing": 9.5, "Student_sitting_speaking": 0.5, "Student_sitting_activity_level": "Seated", "Professor_teaching_breathing": 2, "Professor_teaching_shouting": 2, "Professor_teaching_speaking": 6, "Professor_teaching_activity_level": "Standing", "Professor_conferencing_breathing": 2, "Professor_conferencing_shouting": 6, "Professor_conferencing_speaking": 2, "Professor_conferencing_activity_level": "Light activity", "Concert_musician_soft_music_breathing": 9.5, "Concert_musician_soft_music_speaking": 0.5, "Concert_musician_soft_music_activity_level": "Standing", "Concert_musician_rock_breathing": 8, "Concert_musician_rock_shouting": 1, "Concert_musician_rock_speaking": 1, "Concert_musician_rock_activity_level": "Moderate activity", "Concert_singer_rock_breathing": 2, "Concert_singer_rock_shouting": 7, "Concert_singer_rock_speaking": 1, "Concert_singer_rock_activity_level": "Moderate activity", "Concert_spectator_standing_breathing": 8, "Concert_spectator_standing_shouting": 1, "Concert_spectator_standing_speaking": 1, "Concert_spectator_standing_activity_level": "Light activity", "Concert_spectator_sitting_breathing": 9, "Concert_spectator_sitting_shouting": 0.5, "Concert_spectator_sitting_speaking": 0.5, "Concert_spectator_sitting_activity_level": "Seated", "Museum_visitor_breathing": 9, "Museum_visitor_speaking": 1, "Museum_visitor_activity_level": "Standing", "Theater_spectator_breathing": 9, "Theater_spectator_shouting": 0.5, "Theater_spectator_speaking": 0.5, "Theater_spectator_activity_level": "Seated", "Theater_actor_breathing": 7, "Theater_actor_shouting": 3, "Theater_actor_activity_level": "Moderate activity", "Conferencer_breathing": 2, "Conferencer_shouting": 6, "Conferencer_speaking": 2, "Conferencer_activity_level": "Light activity", "Conference_attendee_breathing": 9.5, "Conference_attendee_speaking": 0.5, "Conference_attendee_activity_level": "Seated", "Guest_standing_breathing": 6, "Guest_standing_shouting": 2, "Guest_standing_speaking": 2, "Guest_standing_activity_level": "Standing", "Guest_sitting_breathing": 6, "Guest_sitting_speaking": 4, "Guest_sitting_activity_level": "Seated", "Server_breathing": 8, "Server_speaking": 2, "Server_activity_level": "Light activity", "Barrista_breathing": 6, "Barrista_shouting": 2, "Barrista_speaking": 2, "Barrista_activity_level": "Standing", "Nightclub_dancing_breathing": 9, "Nightclub_dancing_shouting": 1, "Nightclub_dancing_activity_level": "Moderate activity", "Nightclub_sitting_breathing": 8, "Nightclub_sitting_shouting": 2, "Nightclub_sitting_activity_level": "Seated", "Customer_standing_breathing": 9, "Customer_standing_speaking": 1, "Customer_standing_activity_level": "Standing", "Cashier_sitting_breathing": 5, "Cashier_sitting_speaking": 5, "Cashier_sitting_activity_level": "Seated", "Vendor_standing_breathing": 5, "Vendor_standing_speaking": 5, "Vendor_standing_activity_level": "Standing", "Musculation_breathing": 9, "Musculation_speaking": 1, "Musculation_activity_level": "Heavy exercise", "Floor_gymnastics_breathing": 8, "Floor_gymnastics_shouting": 1, "Floor_gymnastics_speaking": 1, "Floor_gymnastics_activity_level": "Moderate activity", "Team_competition_breathing": 8, "Team_competition_shouting": 1.5, "Team_competition_speaking": 0.5, "Team_competition_activity_level": "Heavy exercise", "Trip_in_elevator_breathing": 9, "Trip_in_elevator_speaking": 1, "Trip_in_elevator_activity_level": "Standing", "Watch_seated_breathing": 60, "Watch_seated_shouting": 10, "Watch_seated_speaking": 30, "Watch_seated_activity_level": "Seated", "Watch_standing_breathing": 50, "Watch_standing_shouting": 20, "Watch_standing_speaking": 30, "Watch_standing_activity_level": "Light activity"}');
var RoomId = 0

function addRoom(room={}) {
  /*Clone the hidden room form*/ 
    const clone = $("#Room_to_clone").clone(true)

  /*Make the clone visible and change its id and inner html*/
    clone.removeClass("d-none")

    clone.attr("id", "Room_" + RoomId)

    clone.find("#room_id").append('<b>' + '\xa0' +RoomId+'</b>');

  /*Update ids and names*/
    clone.find('*').each(function(){
        if (this.id){
          $(this).attr("id", $(this).attr("id") + "[" + RoomId + "]" )
        }
        if (this.name){
          if (this.name in room){
            if ($(this).is(':radio')){
              clone.find(':radio[value='+room[this.name]+'][name^='+this.name+']').attr('checked','checked')
            }
            else {
              $(this).attr('value',room[this.name])
            }
          }
          $(this).attr("name", $(this).attr("name") + "[" + RoomId + "]" )
        }
        if ($(this).attr("for")){
          $(this).attr("for", $(this).attr("for") + "[" + RoomId + "]" )
        }
        if ($(this).attr("data-enables")){
          $(this).attr("data-enables", $(this).attr("data-enables") + "\\[" + RoomId + "\\]" )
        }
      })

    $("#Room_list").append(clone)

    const i = RoomId

      
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

      
      $("#heating_no\\["+i+"\\]").change(function() {
          if(this.checked) {
              $("#humidity\\["+i+"\\]").val(0.5)
          }
        });
      
      $("#heating_yes\\["+i+"\\]").change(function() {
          if(this.checked) {
              $("#humidity\\["+i+"\\]").val(0.3)
          }
        });


          //Check all radio buttons previously selected
        $("input[type=radio]:checked").each(function() {require_fields(this)});

        //Validate all non zero values
        $("input[required].non_zero").each(function() {validateValue(this)});
        $(".non_zero").change(function() {validateValue(this)});
        /* Add event listeners */
        $("#delete_room\\["+i+"\\]").click(function(){deleteRoom(i)})
        $("input[type=radio][name=ventilation_type\\["+i+"\\]]").change(function(){on_ventilation_type_change(i)});
        on_ventilation_type_change(i);
        $(".room_btn_class").click(function(){on_room_list_change()})
        on_room_list_change()
        disable_room_delete()
    
    RoomId = RoomId+1
    }
  
function deleteRoom(i) {
  $("#Room_"+i).remove()
  for(let j = 0;j<=EventId; j++){
    if ($("input[name=event_location\\["+j+"\\]]").val()==i){
      deleteEvent(j)
    }
  }
  disable_room_delete()
}

var EventId = 0
var PersonId = 0
var Calendars = [] 

function addPerson(person={}) {
    /*Clone the hidden person form*/ 
    const clone = $("#Person_to_clone").clone(true)

    /*Make the clone visible and change its id and inner html*/
      clone.removeClass("d-none")

      clone.attr("id", "Person_" + PersonId)

      clone.find("#person_id").append('<b>' + '\xa0' +PersonId+'</b>');

    /*Update ids and names*/
      clone.find('*').each(function(){
          if (this.id){
            $(this).attr("id", $(this).attr("id") + "[" + PersonId + "]" )
          }
          if (this.name){
            if (this.name in person){
                $(this).attr('value',person[this.name])
            }
            $(this).attr("name", $(this).attr("name") + "[" + PersonId + "]" )
          }
          if ($(this).attr("for")){
            $(this).attr("for", $(this).attr("for") + "[" + PersonId + "]" )
          }
          if ($(this).attr("data-target")){
            $(this).attr("data-target", $(this).attr("data-target") + "\\[" + PersonId + "\\]" )
          }
        })
    

        $("#PeopleList").append(clone)

      const i = PersonId

              // Update expiration on change
      $("#event_activity_type\\["+ i +"\\]").change(function() {
        $("#event_activity_breathing\\["+ i +"\\]").val(js_expiration[this.value+"_breathing"] || 0)
      })
      $("#event_activity_type\\["+ i +"\\]").change(function() {
        $("#event_activity_speaking\\["+ i +"\\]").val(js_expiration[this.value+"_speaking"] || 0)
      })
      $("#event_activity_type\\["+ i +"\\]").change(function() {
        $("#event_activity_shouting\\["+ i +"\\]").val(js_expiration[this.value+"_shouting"] || 0)
      })
      $("#event_activity_type\\["+ i +"\\]").change(function() {
        $("#event_activity_level\\["+ i +"\\]").val(js_expiration[this.value+"_activity_level"] || 0)
      })
      $("#saveEvent\\["+i+"\\]").click(function(){saveEvent(i)})
      $("#delete_person\\["+i+"\\]").click(function(){deletePerson(i)})
      
      var calendarEl = $('#calendar\\['+ i +'\\]').get(0);
        
      var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridDay',
        headerToolbar: false,
        dayHeaders: false,
        slotDuration: '00:15:00',
        slotMinTime:  "00:00:00",
        slotMaxTime:  "23:59:59",
        aspectRatio: 2,
        allDaySlot: false,
        eventDidMount: function(arg) { 
          arg.el.querySelector('.fc-event-title').innerHTML = `<button type="button" id="deleteEvent[` + EventId + `]" class="btn btn-danger float-right mr-2" onclick=deleteEvent(` + EventId + `)>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
          <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"></path>
          <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"></path>
          </svg>
          </button>`},
      });

      Calendars[PersonId] = calendar
      
      PersonId += 1

      disable_people_delete()

      calendar.render();
  }

function saveEvent(i, event={}){
    var events = Calendars[i].getEvents()
    var start = new Date();
    var end = new Date();



    if ('start' in event){
      start_hour = event['start'].split(':')
      event_start = event['start']
    }
    else {
      start_hour = document.getElementById('event_start['+i+']').value.split(':');
      event_start = $('#event_start\\['+i+'\\]').val();
    }
    if ('end' in event){
      end_hour = event['end'].split(':')
      event_finish = event['end']
    }
    else {
      end_hour = document.getElementById('event_finish['+i+']').value.split(':');
      event_finish = $('#event_finish\\['+i+'\\]').val();
    }
    if ('event_mask_wearing_option' in event) {
      event_mask_wearing_option = event['event_mask_wearing_option']
    }
    else {
      event_mask_wearing_option = $('input[name="mask_wearing_option_form\\['+i+'\\]"]:checked').val()
    }
    if ('event_activity_level' in event){
      event_activity_level = event['event_activity_level']
    }
    else {
      event_activity_level = $('#event_activity_level\\['+i+'\\]').val()
    }
    if ('event_activity_breathing' in event){
      event_activity_breathing = event['event_activity_breathing']
    }
    else {
      event_activity_breathing = $('#event_activity_breathing\\['+i+'\\]').val()
    }
    if ('event_activity_speaking' in event){
      event_activity_speaking = event['event_activity_speaking']
    }
    else {
      event_activity_speaking = $('#event_activity_speaking\\['+i+'\\]').val()
    }
    if ('event_activity_shouting' in event){
      event_activity_shouting = event['event_activity_shouting']
    }
    else {
      event_activity_shouting = $('#event_activity_shouting\\['+i+'\\]').val()
    }
    if('location' in event){
      event_location = event['location']
    }
    else {
      event_location = $('#event_location\\['+i+'\\]').val()
    }
    if('mask_ratio' in event){
      event_mask_ratio = event['mask_ratio']
    }
    else {
      event_mask_ratio = $('#event_mask_wear_ratio\\['+i+'\\]').val()
    }
    if ('mask_type' in event){
      event_mask_type = event['mask_type']
    }
    else {
      event_mask_type = $('input[name="mask_type_option_form\\['+i+'\\]"]:checked').val()
    }
    if ('activity' in event){
      event_activity = event['activity']
    }
    else {
      event_activity = $('#event_activity_type\\['+i+'\\]').val()
    }





    start.setHours(start_hour[0], start_hour[1]);
    start.setSeconds(0)
    start.setMilliseconds(0)
    end.setHours(end_hour[0], end_hour[1]);
    end.setSeconds(0)
    end.setMilliseconds(0)

    //Validate event
    if (start>=end){
        return false
    }

    //Prevent simultaneous events
    for(var el of events){
        if ((el.start < start && el.end > start)||(el.start < end && el.end > end)||(el.start>=start && el.end<=end)){
          $("#event_start\\["+i+"\\]").addClass("red_border")
          $("#event_finish\\["+i+"\\]").addClass("red_border")
          return false
        }
    }
    $("#event_start\\["+i+"\\]").removeClass("red_border")
    $("#event_finish\\["+i+"\\]").removeClass("red_border")


    Calendars[i].addEvent({id: ""+EventId,
    title: $("option[value='"+event_activity+"']").first().text() + $("#type_name\\["+event_location+"\\]").val() + " " +event_location,
    start : start,
    end : end,
    allDay: false,
    eventDisplay: 'list-item',
    description: "Test"}
    );
    //Keep event values in hidden fields
    $('#Person_' + i).append(`
    <div id="Event_`+EventId+`">
    <input type="hidden" name="event_start[`+EventId+`]" value="`+event_start+`">
    <input type="hidden" name="event_person[`+EventId+`]" value="`+i+`">
    <input type="hidden" name="event_finish[`+EventId+`]" value="`+event_finish+`">
    <input type="hidden" name="event_location[`+EventId+`]" value="`+event_location+`">
    <input type="hidden" name="event_mask_ratio[`+EventId+`]" value="`+event_mask_ratio+`">
    <input type="hidden" name="event_mask_type[`+EventId+`]" value="`+event_mask_type+`">
    <input type="hidden" name="event_activity[`+EventId+`]" value="`+event_activity+`">
    <input type="hidden" name="event_activity_breathing[`+EventId+`]" value="`+event_activity_breathing+`">
    <input type="hidden" name="event_activity_speaking[`+EventId+`]" value="`+event_activity_speaking+`">
    <input type="hidden" name="event_activity_shouting[`+EventId+`]" value="`+event_activity_shouting+`">
    <input type="hidden" name="event_activity_level[`+EventId+`]" value="`+event_activity_level+`">
    <input type="hidden" name="event_mask_wearing_option[`+EventId+`]" value="`+event_mask_wearing_option+`">
    </div>`)

    $("#eventModal\\["+i+"\\]").modal('hide')
    EventId = EventId + 1;
    Calendars[i].render()
}

function deletePerson(i) {
    try {
        document.getElementById("Person_"+i).remove()
        disable_people_delete()
    }
    catch(error){}
    
}

function deleteEvent(e){
    for (var calendar of Calendars){
        try{
            calendar.getEventById(e).remove()
        }
        catch(error){}
    }
    $("#Event_"+e).remove()
    
}

/* -------On Load------- */
$(document).ready(function () {
  //Remove delete buttons if only 1 room/person
  disable_room_delete()
  disable_people_delete()

  //Hide carousel prev/next arrow on first/last page and render hidden calendars
  $('.carousel-control-prev').hide();
  $('#carousel').on('slid.bs.carousel', function(event) {
    if(event.to == 0) {
      $('.carousel-control-next').show();
      $('.carousel-control-prev').hide();
    } else if(event.to == 3) {
      $('.carousel-control-prev').show();
      $('.carousel-control-next').hide();
      for(let i = 0; i<Calendars.length; i++){
        Calendars[i].render()
      }

    } else {
      $('.carousel-control-prev').show();
      $('.carousel-control-next').show();
    }    
  });



    // When the document is ready, deal with the fact that we may be here
  // as a result of a forward/back browser action. If that is the case, update
  // the visibility of some of our inputs.

  //Check all radio buttons previously selected
  $("input[type=radio]:checked").each(function() {require_fields(this)});

  //Validate all non zero values
  $("input[required].non_zero").each(function() {validateValue(this)});
  $(".non_zero").change(function() {validateValue(this)});

  //Validate expiration
  $("#exposed_activity_breathing").change(function(){validateExpiration("exposed")});
  $("#exposed_activity_speaking").change(function(){validateExpiration("exposed")});
  $("#exposed_activity_shouting").change(function(){validateExpiration("exposed")});
  $("#infected_activity_breathing").change(function(){validateExpiration("infected")});
  $("#infected_activity_speaking").change(function(){validateExpiration("infected")});
  $("#infected_activity_shouting").change(function(){validateExpiration("infected")});

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


  var url = new URL(decodeURIComponent(window.location.href));
  //Pre-fill form with known values
  url.searchParams.forEach((value, name) => {
          string_value = value.replace(/'/g, '"')
          var elemObj = document.getElementById(name);
          if (name == 'Room_list') {
            for (const room of JSON.parse(string_value)) {
              addRoom(room);
            }
          }
          
          else if (name == 'People_list'){
            for (const person of JSON.parse(string_value)) {
              addPerson(person);
            }
          }

          else if (name == 'Event_list') {
            for (const event of JSON.parse(string_value)) {
              saveEvent(event['event_person'], event);
            }
          }
          else if (name == 'simulation_name') {
            $("#"+name).attr("value", value)
          }
          else if (name == 'virus_type'){
            $("option[value="+value+"]").attr('selected','selected')
          }
          else if (name == 'location_name'){
            $("#"+name).attr("value", value)
          }
          else if (name == 'location_latitude'){
            $("#"+name).attr("value", value)
          }
          else if (name == 'location_longitude'){
            $("#"+name).attr("value", value)
          }
          else if (name == 'event_month'){
            $("option[value="+value+"]").attr('selected','selected')
          }    
    })
    if($("div[id^=Room_]").length<3){
      addRoom()
    }     
    if($("div[id^=Person_]").length<2){
      addPerson()
    } 
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
  try {
    id = $(obj).attr('id').split("[")[1].split("]")[0]
    switch ($(obj).attr('id').split("[")[0]) {
      case "room_data_volume":
        require_room_volume(true, id);
        require_room_dimensions(false, id);
        break;
      case "room_data_dimensions":
        require_room_volume(false, id);
        require_room_dimensions(true, id);
        break;
      case "mechanical_ventilation":
        require_mechanical_ventilation(true, id);
        require_natural_ventilation(false, id);
        break;
      case "natural_ventilation":
        require_mechanical_ventilation(false, id);
        require_natural_ventilation(true, id);
        break;
      case "window_sliding":
        require_window_width(false, id);
        break;
      case "window_hinged":
        require_window_width(true, id);
        break;
      case "mech_type_air_changes":
        require_air_changes(true, id);
        require_air_supply(false, id);
        break;
      case "mech_type_air_supply":
        require_air_changes(false, id);
        require_air_supply(true, id);
        break;
      case "windows_open_periodically":
        require_venting(true, id);
        break;
      case "windows_open_permanently":
        require_venting(false, id);
        break;
      case "biov_yes":
        require_biov(true, id);
        break;
      case "biov_no":
        require_biov(false, id);
        break;
      case "mask_on":
        require_mask(true, id);
        break;
      case "mask_off":
        require_mask(false, id);
        break;
      default:
        break;
    }
  } 
  catch {}
}

function unrequire_fields(obj) {
  id = $(obj).attr('id').split("[")[1].split("]")[0]
  switch ($(obj).attr('id').split("[")[0]) {
    case "mechanical_ventilation":
      require_mechanical_ventilation(false, id);
      break;
    case "natural_ventilation":
      require_natural_ventilation(false, id);
      break;
    default:
      break;
  }
}

function require_room_volume(option, id) {
  require_input_field("#room_volume\\[" + id +"\\]", option);
  set_disabled_status("#room_volume\\[" + id +"\\]", !option);
}

function require_room_dimensions(option, id) {
  require_input_field("#floor_area\\[" + id +"\\]", option);
  require_input_field("#ceiling_height\\[" + id +"\\]", option);
  set_disabled_status("#floor_area\\[" + id +"\\]", !option);
  set_disabled_status("#ceiling_height\\[" + id +"\\]", !option);
}

function require_mechanical_ventilation(option, id) {
  $("#mech_type_air_changes\\[" + id +"\\]").prop('required', option);
  $("#mech_type_air_supply\\[" + id +"\\]").prop('required', option);
  if (!option) {
    require_input_field("#air_changes\\[" + id +"\\]", option);
    require_input_field("#air_supply\\[" + id +"\\]", option);
  }
}

function require_natural_ventilation(option,id) {
  require_input_field("#windows_number\\[" + id +"\\]", option);
  require_input_field("#window_height\\[" + id +"\\]", option);
  require_input_field("#opening_distance\\[" + id +"\\]", option);
  $("#window_sliding\\[" + id +"\\]").prop('required', option);
  $("#window_hinged\\[" + id +"\\]").prop('required', option);
  $("#windows_open_permanently\\[" + id +"\\]").prop('required', option);
  $("#windows_open_periodically\\[" + id +"\\]").prop('required', option);
  if (!option) {
    require_input_field("#window_width\\[" + id +"\\]", option);
    require_input_field("#windows_duration\\[" + id +"\\]", option);
    require_input_field("#windows_frequency\\[" + id +"\\]", option);
  }
}

function require_window_width(option, id) {
  require_input_field("#window_width\\[" + id +"\\]", option);
  set_disabled_status("#window_width\\[" + id +"\\]", !option);
}

function require_air_changes(option, id) {
  require_input_field("#air_changes\\[" + id +"\\]", option);
  set_disabled_status("#air_changes\\[" + id +"\\]", !option);
}

function require_air_supply(option, id) {
  require_input_field("#air_supply\\[" + id +"\\]", option);
  set_disabled_status("#air_supply\\[" + id +"\\]", !option);
}

function require_venting(option, id) {
  require_input_field("#windows_duration\\[" + id +"\\]", option);
  require_input_field("#windows_frequency\\[" + id +"\\]", option);
  set_disabled_status("#windows_duration\\[" + id +"\\]", !option);
  set_disabled_status("#windows_frequency\\[" + id +"\\]", !option);
}

function require_mask(option, id) {
  $("#mask_type_1\\[" + id +"\\]").prop('required', option);
  $("#mask_type_ffp2\\[" + id +"\\]").prop('required', option);
}

function require_biov(option, id) {
  require_input_field("#biov_amount\\[" + id +"\\]", option);
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

function removeInvalid(id) {
  if ($(id).hasClass("red_border")) {
    $(id).val("");
    $(id).removeClass("red_border");
    removeErrorFor(id);
  }
}

function on_ventilation_type_change(i) {
  ventilation_types = $('input[type=radio][name=ventilation_type\\['+i+'\\]]');
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

function on_room_list_change(){
  var rooms=[]
  $("div[id^=Room_]").each(
    function(){
        n = Number($(this).attr('id').split("_")[1])
        if (typeof n === 'number' && !isNaN(n)){
          rooms.push(n)
        }
    }
  )


  $(".event_location").each(function(){
    $(this).empty()
    for (let i = 0; i<rooms.length; i++){
      $(this).append("<option>"+ rooms[i] +"</option>")
    }
    
  })
}


function room_count() {
  return $("div[id^=Room_]").length - 2
}

function people_count() {
  return $("div[id^=Person_]").length - 1
}

function disable_room_delete() {
    //Disable delete button when only one room/person
    if (room_count()<2){
      $(".btn-danger.room_btn_class").prop( "disabled", true );
    }
    else {
      $(".btn-danger.room_btn_class").prop( "disabled", false );
    }
}

function disable_people_delete() {
      //Disable delete button when only one room/person
      if (people_count()<2){
        $(".btn-danger.people_btn_class").prop( "disabled", true );
      }
      else {
        $(".btn-danger.people_btn_class").prop( "disabled", false );
      }
}
