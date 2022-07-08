var js_default = JSON.parse('{"exposed_activity_type": "Office_worker", "exposed_activity_level": "Seated", "exposed_breathing": 8, "exposed_speaking": 2, "exposed_shouting": 0, "exposed_mask_wear_ratio": 0.7, "infected_activity_type": "Office_worker", "infected_activity_level": "Seated", "infected_breathing": 8, "infected_speaking": 2, "infected_shouting": 0, "infected_mask_wear_ratio": 0.7, "air_changes": 1.0, "air_supply": 100, "calculator_version": "1.0.3", "ceiling_height": 2.5, "humidity": "", "inside_temp": 20, "exposed_coffee_break_option": "coffee_break_0", "exposed_coffee_duration": 5, "exposed_finish": "17:30", "exposed_lunch_finish": "13:30", "exposed_lunch_option": 1, "exposed_lunch_start": "12:30", "exposed_start": "08:30", "event_month": "January", "floor_area": 40, "biov_amount": 1000, "biov_option": 0, "infected_coffee_break_option": "coffee_break_0", "infected_coffee_duration": 5, "infected_dont_have_breaks_with_exposed": 0, "infected_finish": "17:30", "infected_lunch_finish": "13:30", "infected_lunch_option": 1, "infected_lunch_start": "12:30", "infected_people": 1, "infected_start": "08:30", "location_latitude": 47.21725, "location_longitude": -1.55336, "location_name": "Nantes, Loire-Atlantique, Pays de la Loire, FRA", "mask_type": "Type_I", "mask_wearing_option": "mask_off", "mechanical_ventilation_type": "mech_type_air_supply", "opening_distance": 0.5, "room_heating_option": 1, "room_number": "1", "room_volume": 100, "simulation_name": "My simulation", "total_people": 10, "ventilation_type": "mechanical_ventilation", "virus_type": "SARS_CoV_2_OMICRON", "viruses": {"SARS_CoV_2": "SARS-CoV-2 (nominal strain)", "SARS_CoV_2_ALPHA": "SARS-CoV-2 (Alpha VOC)", "SARS_CoV_2_BETA": "SARS-CoV-2 (Beta VOC)", "SARS_CoV_2_GAMMA": "SARS-CoV-2 (Gamma VOC)", "SARS_CoV_2_DELTA": "SARS-CoV-2 (Delta VOC)", "SARS_CoV_2_OMICRON": "SARS-CoV-2 (Omicron VOC)"}, "volume_type": "room_volume_explicit", "window_type": "window_sliding", "window_height": 1.0, "window_width": 1.0, "windows_duration": 15, "windows_frequency": 60, "windows_number": 1, "window_opening_regime": "windows_open_permanently"}');

var RoomId = 0

function addRoom() {
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

      //Set humidity value according to heating option

      if($("#heating_no\\["+i+"\\]").is(':checked')){
          $("#humidity").val(0.5)
        }
      if($("#heating_yes\\["+i+"\\]").is(':checked')){
          $("#humidity\\["+i+"\\]").val(0.3)
        }
      
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

    
    RoomId = RoomId+1
    }
  
function deleteRoom(i) {
  $("#Room_"+i).remove()
}

var EventId = 0
var PersonId = 0
var Calendars = [] 

function addPerson() {
    $("#PeopleList").append(`
    <div id = "peopleFormContainer[` + PersonId + `]">
    <div class="PeopleForm">
    <table>
    <tbody><tr><th>Id</th><th>Name</th><th>Role</th></tr>
    <tr>
      <td><div>` + PersonId + `</div>
      <td><input class="col-sm-8 form-control" type="text" name="person_name[` + PersonId + `]" value="Person" required></td>
      <td><input class="col-sm-8 form-control" type="text" name="role[` + PersonId + `]" value="Office" required></td>
    </tr>
    </tbody></table>
    <br>
    <div class="schedule"> 
    <label>Schedule:</label>
    <div class="calendar" id='calendar[` + PersonId + `]'></div>
    <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#eventModal\\[` + PersonId + `\\]">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
    <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"></path>
  </svg>
    </button>
    <button type="button" id="deletePerson[` + PersonId + `]" class="btn btn-secondary" onclick=deletePerson(` + PersonId + `)>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"></path>
    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"></path>
    </svg>
    </button>

    <div class="modal fade" id="eventModal[` + PersonId + `]" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="newEventTitle">New event</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
          <form id="newEventForm">
            <div class="split">
              <div>
                <label class="tabbed mb-` + PersonId + `">Start:</label>
                <input type="time" id="event_start[` + PersonId + `]" class="start_time" value="08:30" required>
              </div>
              <div>
                <label class="tabbed mb-` + PersonId + `">End: </label>
                <input type="time" id="event_finish[` + PersonId + `]" class="finish_time" value="17:30" required>
              </div>
            </div>
            <div class="form-group row">
            <div class="col-sm-4"><label class="col-form-label">Activity:</label></div>
            <div class="col-sm-6">
                <select id="event_activity[` + PersonId + `]" name="event_activity[` + PersonId + `]" class="form-control" required>
                      
                <optgroup label="---- Default ----">
                  <option selected="" value="Office_worker">Office worker</option>
                </optgroup>
              
                  <optgroup label="---- Business ----">
                    
                      
                  
                      
                        <option value="Workshop_worker">Workshop worker</option>
                      
                  
                      
                        <option value="Meeting_participant">Meeting participant</option>
                      
                  
                      
                        <option value="Meeting_leader">Meeting leader</option>
                      
                  
                  </optgroup>
                
                  <optgroup label="---- Hospital ----">
                    
                      
                        <option value="Hospital_patient">Hospital patient</option>
                      
                  
                      
                        <option value="Nurse_working">Nurse working</option>
                      
                  
                      
                        <option value="Physician_working">Physician working</option>
                      
                  
                  </optgroup>
                
                  <optgroup label="---- Education ----">
                    
                      
                        <option value="Student_sitting">Student sitting</option>
                      
                  
                      
                        <option value="Professor_teaching">Professor teaching</option>
                      
                  
                      
                        <option value="Professor_conferencing">Professor conferencing</option>
                      
                  
                  </optgroup>
                
                  <optgroup label="---- Events ----">
                    
                      
                        <option value="Concert_musician_soft_music">Concert musician (soft music)</option>
                      
                  
                      
                        <option value="Concert_musician_rock">Concert musician (rock)</option>
                      
                  
                      
                        <option value="Concert_singer_rock">Concert singer (rock)</option>
                      
                  
                      
                        <option value="Concert_spectator_standing">Concert spectator (standing)</option>
                      
                  
                      
                        <option value="Concert_spectator_sitting">Concert spectator (sitting)</option>
                      
                  
                      
                        <option value="Museum_visitor">Museum visitor</option>
                      
                  
                      
                        <option value="Theater_spectator">Theater spectator</option>
                      
                  
                      
                        <option value="Theater_actor">Theater actor</option>
                      
                  
                      
                        <option value="Conferencer">Conferencer</option>
                      
                  
                      
                        <option value="Conference_attendee">Conference attendee</option>
                      
                  
                  </optgroup>
                
                  <optgroup label="---- Restaurant and Bar ----">
                    
                      
                        <option value="Guest_standing">Guest standing</option>
                      
                  
                      
                        <option value="Guest_sitting">Guest sitting</option>
                      
                  
                      
                        <option value="Server">Server</option>
                      
                  
                      
                        <option value="Barrista">Barrista</option>
                      
                  
                      
                        <option value="Nightclub_dancing">Nightclub dancing</option>
                      
                  
                      
                        <option value="Nightclub_sitting">Nightclub sitting</option>
                      
                  
                  </optgroup>
                
                  <optgroup label="---- Store and Retail ----">
                    
                      
                        <option value="Customer_standing">Customer standing</option>
                      
                  
                      
                        <option value="Cashier_sitting">Cashier sitting</option>
                      
                  
                      
                        <option value="Vendor_standing">Vendor standing</option>
                      
                  
                  </optgroup>
                
                  <optgroup label="---- Sport ----">
                    
                      
                        <option value="Musculation">Musculation</option>
                      
                  
                      
                        <option value="Floor_gymnastics">Floor gymnastics</option>
                      
                  
                      
                        <option value="Team_competition">Team competition</option>
                      
                  
                  </optgroup>
                
                  <optgroup label="---- Miscellaneous ----">
                    
                      
                        <option value="Trip_in_elevator">Trip in elevator</option>
                      
                  
                  </optgroup>
                
                  <optgroup label="---- Navy ----">
                    
                      
                        <option value="Watch_seated">Watch seated</option>
                      
                  
                      
                        <option value="Watch_standing">Watch standing</option>
                      
                  
                  </optgroup>
                
               </select>
                </div>
            </div>
            <div class="form-group row">
            <div class="col-sm-4"><label class="col-form-label">Room id:</label></div>
            <div class="col-sm-6">
              <input type="number" step="any" id="event_room_id[` + PersonId + `]" class="non_zero form-control" min="0"  value="0"  max="` + RoomId + `" required="">
                </div>
            </div>

            <div class="form-group row">
             <div class="col-sm-4"><label class="col-form-label">Mask wear ratio: </label></div>
             <div class="col-sm-6 align-self-center"><input type="number" id="event_mask_ratio[` + PersonId + `]" class="form-control" name="event_mask_ratio[` + PersonId + `]" min="0.0" max="1.0" value="0.7" step="0.1" required=""></div>
            </div>
            <div>
            <input type="radio" id="mask_type_1" name="event_mask_type[` + PersonId + `]" value="Type_I" checked="checked">
              <label for="mask_type_1">
                Surgical/Type I
                <img class="mask_icons" src="/static/images/masks/t1.png">
              </label>
            </div>
            <div>
            <input type="radio" id="mask_type_ffp2"  name="event_mask_type[` + PersonId + `]" value="FFP2" >
                <label for="mask_type_ffp2">
                Respirator/FFP2
                <img class="mask_icons" src="/static/images/masks/ffp2.png">
                </label>
            </div>
              
            </div>

          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button type="submit" id="saveEvent[` + PersonId + `]" onclick=saveEvent(` + PersonId + `) class="btn btn-primary" data-dismiss="modal" >Save changes</button>
          </div>
          </form>
        </div>
      </div>
    </div>
    </div>
    <div class="d-flex justify-content-center">------------------------------------------------------------------------------------------------------------------</div>
    </div>
    </div>`)
    var calendarEl = document.getElementById('calendar['+ PersonId +']');
      
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
        arg.el.querySelector('.fc-event-title').innerHTML = `<button type="button" id="deleteEvent[` + EventId + `]" class="btn btn-secondary" onclick=deleteEvent(` + EventId + `)>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"></path>
        <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"></path>
        </svg>
        </button>`},
    });

    Calendars[PersonId] = calendar
    
    PersonId += 1

    calendar.render();
}


function saveEvent(i){
    var events = Calendars[i].getEvents()
    var start = new Date();
    var end = new Date();
    start_hour = document.getElementById('event_start['+i+']').value.split(':');
    end_hour = document.getElementById('event_finish['+i+']').value.split(':');
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
            return false
        }
    }
    Calendars[i].addEvent({id: ""+EventId,
    title: document.getElementById('event_activity['+i+']').options[document.getElementById('event_activity['+i+']').selectedIndex].text,
    start : start,
    end : end,
    allDay: false,
    eventDisplay: 'list-item',
    description: "Test"}
    );
    $('#peopleFormContainer\\[' + i + '\\]').append(`
    <input type="hidden" name="event_start[`+EventId+`]" value="`+document.getElementById('event_start['+i+']').value+`">
    <input type="hidden" name="event_person[`+EventId+`]" value="`+i+`">
    <input type="hidden" name="event_finish[`+EventId+`]" value="`+document.getElementById('event_finish['+i+']').value+`">
    <input type="hidden" name="event_location[`+EventId+`]" value="`+document.getElementById('event_room_id['+i+']').value+`">
    <input type="hidden" name="event_mask_ratio[`+EventId+`]" value="`+document.getElementById('event_mask_ratio['+i+']').value+`">
    <input type="hidden" name="event_mask_type[`+EventId+`]" value="`+document.querySelector('input[name="event_mask_type['+i+']"]:checked').value+`">
    <input type="hidden" name="event_activity[`+EventId+`]" value="`+document.getElementById('event_activity['+i+']').value+`">`)

    
    EventId = EventId + 1;
    Calendars[i].render()
}

function deletePerson(i) {
    try {
        document.getElementById("peopleFormContainer[" + i + "]").remove()
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
    
}

/* -------On Load------- */
$(document).ready(function () {

  //Add first room
  addRoom()
  //Hide carousel prev/next arrow on first/last page
  $('.carousel-control-prev').hide();
  $('#carousel').on('slide.bs.carousel', function(event) {
    if(event.from == 1 && event.to == 0) {
      $('.carousel-control-prev').hide();
    } else if(event.from == 2 && event.to == 3) {
      $('.carousel-control-next').hide();
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


  var url = new URL(decodeURIComponent(window.location.href));
  //Pre-fill form with known values
  url.searchParams.forEach((value, name) => {
          string_value = value.replace(/'/g, '"')
          var elemObj = document.getElementById(name);
          console.log(string_value)
          if (name == 'Room_list') {
            for (const room of JSON.parse(string_value)) {
              addRoom(RoomId);
            }
          }
          
          else if (name == 'People_list'){
            for (const person of JSON.parse(string_value)) {
              addPerson();
            }
          }

          else{
            for (const event of JSON.parse(string_value)) {
              saveEvent(EventId);
            }
          }

    
    })
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


