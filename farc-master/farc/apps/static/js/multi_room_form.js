var RoomId = 0

function addRoom() {
  /*Clone the hidden room form*/ 
    const div = $("#Room_to_clone").get(0)
    const clone = div.cloneNode(true);

  /*Make the clone visible*/
    clone.classList.remove("d-none")

  /*Update ids and names*/
    clone.id = "Room_" + RoomId
    clone.querySelector("#room_id").insertAdjacentHTML('beforeend', '<b>' + '\xa0' +RoomId+'</b>');
    clone.querySelector("#room_id").id = "room_id[" + RoomId + "]"
    clone.querySelector("#room_volume").name = "room_volume[" + RoomId + "]"
    clone.querySelector("#room_volume").id = "room_volume[" + RoomId + "]"
    clone.querySelector("#heating_no").name = "heating_no[" + RoomId + "]"
    clone.querySelector("#heating_no").id = "room_heating_option[" + RoomId + "]"
    clone.querySelector("#heating_yes").name = "heating_yes[" + RoomId + "]"
    clone.querySelector("#heating_yes").id = "room_heating_option[" + RoomId + "]"
    clone.querySelector("#humidity").name = "humidity[" + RoomId + "]"
    clone.querySelector("#humidity").id = "humidity[" + RoomId + "]"
    clone.querySelector("#inside_temp").name = "inside_temp[" + RoomId + "]"
    clone.querySelector("#inside_temp").id = "inside_temp[" + RoomId + "]"
    clone.querySelector("#no_ventilation").name = "ventilation_type[" + RoomId + "]"
    clone.querySelector("#no_ventilation").id = "no_ventilation[" + RoomId + "]"
    clone.querySelector("#mechanical_ventilation").name = "ventilation_type[" + RoomId + "]"
    clone.querySelector("#mechanical_ventilation").id = "mechanical_ventilation[" + RoomId + "]"
    clone.querySelector("#natural_ventilation").name = "ventilation_type[" + RoomId + "]"
    clone.querySelector("#natural_ventilation").id = "natural_ventilation[" + RoomId + "]"
    clone.querySelector("#mech_type_air_supply").name = "mechanical_ventilation_type[" + RoomId + "]"
    clone.querySelector("#mech_type_air_supply").id = "mech_type_air_supply[" + RoomId + "]"
    clone.querySelector("#air_supply").name = "air_supply[" + RoomId + "]"
    clone.querySelector("#air_supply").id = "air_supply[" + RoomId + "]"
    clone.querySelector("#mech_type_air_changes").name = "mechanical_ventilation_type[" + RoomId + "]"
    clone.querySelector("#mech_type_air_changes").id = "mech_type_air_changes[" + RoomId + "]"
    clone.querySelector("#air_changes").name = "air_changes[" + RoomId + "]"
    clone.querySelector("#air_changes").id = "air_changes[" + RoomId + "]"
    clone.querySelector("#windows_number").name = "windows_number[" + RoomId + "]"
    clone.querySelector("#windows_number").id = "windows_number[" + RoomId + "]"
    clone.querySelector("#window_height").name = "window_height[" + RoomId + "]"
    clone.querySelector("#window_height").id = "window_height[" + RoomId + "]"   
    clone.querySelector("#window_sliding").name = "window_type[" + RoomId + "]"
    clone.querySelector("#window_sliding").id = "window_sliding[" + RoomId + "]"
    clone.querySelector("#window_hinged").name = "window_type[" + RoomId + "]"
    clone.querySelector("#window_hinged").id = "window_hinged[" + RoomId + "]"
    clone.querySelector("#window_width").name = "window_width[" + RoomId + "]"
    clone.querySelector("#window_width").id = "window_width[" + RoomId + "]"   
    clone.querySelector("#opening_distance").name = "opening_distance[" + RoomId + "]"
    clone.querySelector("#opening_distance").id = "opening_distance[" + RoomId + "]"  
    clone.querySelector("#windows_open_permanently").name = "window_opening_regime[" + RoomId + "]"  
    clone.querySelector("#windows_open_permanently").id = "window_open_permanently[" + RoomId + "]"  
    clone.querySelector("#windows_open_periodically").name = "window_opening_regime[" + RoomId + "]"  
    clone.querySelector("#windows_open_periodically").id = "windows_open_periodically[" + RoomId + "]"  
    clone.querySelector("#windows_duration").name = "window_duration[" + RoomId + "]"
    clone.querySelector("#windows_duration").id = "window_duration[" + RoomId + "]"  
    clone.querySelector("#windows_frequency").name = "window_frequency[" + RoomId + "]"
    clone.querySelector("#windows_frequency").id = "window_frequency[" + RoomId + "]"
    clone.querySelector("#biov_no").name = "biov_option[" + RoomId + "]"
    clone.querySelector("#biov_no").id = "biov_no[" + RoomId + "]" 
    clone.querySelector("#biov_yes").name = "biov_option[" + RoomId + "]"
    clone.querySelector("#biov_yes").id = "biov_yes[" + RoomId + "]"
    clone.querySelector("#biov_amount").name = "biov_amount[" + RoomId + "]"
    clone.querySelector("#biov_amount").id = "biov_amount[" + RoomId + "]"

    $("#Room_list").append(clone)

    

    RoomId = RoomId+1
    }
    
function deleteRoom(i) {
    document.getElementById("Room_" + i).remove()
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
    <button type="button" id="deleteRoom[` + PersonId + `]" class="btn btn-secondary" onclick=deletePerson(` + PersonId + `)>
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





