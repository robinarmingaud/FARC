var RoomId = 0

function addRoom() {
    $("#RoomList").append(`<div id = "roomFormContainer[` + RoomId + `]">
    <div class="RoomForm">
    <table>
    <tbody><tr><th>Id</th><th>Name</th><th>Volume</th><th>Humidity</th><th>Temperature</th><th>Ventilation type</th><th></th><th></th><th>Duration</th><th>Frequency</th></tr>
    <tr>
      <td><div>` + RoomId + `</div>
      <td><input type="text" name="name[` + RoomId + `]"></td>
      <td><input type="text" name="volume[` + RoomId + `]"></td>
      <td><input type="text" name="humidity[` + RoomId + `]"></td>
      <td><input type="text" name="temperature[` + RoomId + `]"></td>
      <td><input type="radio" name="ventilation[` + RoomId + `]">No ventilation</td>
      <td><input type="radio" name="ventilation[` + RoomId + `]">Mechanical</td>
      <td><input type="radio" name="ventilation[` + RoomId + `]">Natural</td>
      <td><input type="text" name="duration[` + RoomId + `]"></td>
      <td><input type="text" name="frequency[` + RoomId + `]"></td>
    </tr>
    </tbody></table>
    <table>
    <tbody><tr><th>Window height</th><th>Window width</th><th>Window number</th><th>Window opening regime</th><th></th><th>Opening distance</th><th>Month</th><th></th></tr>
    <tr>
      <td><input type="text" name="height[` + RoomId + `]"></td>
      <td><input type="text" name="width[` + RoomId + `]"></td>
      <td><input type="text" name="number[` + RoomId + `]"></td>
      <td><input type="radio" name="openingRegime[` + RoomId + `]">Periodically</td>
      <td><input type="radio" name="openingRegime[` + RoomId + `]">Permanently</td>
      <td><input type="text" name="openingDistance[` + RoomId + `]"></td>
      <td><input type="text" name="month[` + RoomId + `]"></td>
      <td><input type="checkbox" name="openingRegime[` + RoomId + `]">Room heating</td>
    </tr>
    </tbody></table>
    <table>
    <tbody><tr><th>Air supply</th><th></th><th>Biov Amount</th></tr>
    <tr>
      <td><input type="text" name="airSupply[` + RoomId + `]"></td>
      <td><input type="checkbox" name="biovOption[` + RoomId + `]">Biov option</td>
      <td><input type="text" name="biovAmount[` + RoomId + `]"></td>
    </tr>
    </tbody></table>
    <button type="button" id="deleteRoom[` + RoomId + `]" class="btn btn-secondary" onclick=deleteRoom(` + RoomId + `)>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"></path>
    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"></path>
    </svg>
    </button>
    <br>
    <div class="d-flex justify-content-center">------------------------------------------------------------------------------------------------------------------</div>
    </div>
    </div>`)
    RoomId += 1
    }
    
function deleteRoom(i) {
    document.getElementById("roomFormContainer[" + i + "]").remove()
}

var EventId = 0
var PersonId = 0
var Calendars = [] 

function addPerson() {
    $("#PeopleList").append(`
    <div id = "peopleFormContainer[` + PersonId + `]">
    <div class="PeopleForm">
    <table>
    <tbody><tr><th>Id</th><th>Name</th><th>Role</th><th>Number</th></tr>
    <tr>
      <td><div>` + PersonId + `</div>
      <td><input type="text" name="name[` + PersonId + `]"></td>
      <td><input type="text" name="role[` + PersonId + `]"></td>
      <td><input type="text" name="number[` + PersonId + `]"></td>
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
                <select id="eventActivity[` + PersonId + `]" name="eventActivity[` + PersonId + `]" class="form-control" required>
                      
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
              <input type="number" step="any" id="roomid[` + PersonId + `]" class="non_zero form-control" min="0"  value="0"  max="` + RoomId + `" required="">
                </div>
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
    end.setHours(end_hour[0], end_hour[1]);

    //Validate event
    if (start>=end){
        return false
    }

    //Prevent simultaneous events
    for(var el of events){
        if ((el.start < start && el.end > start)||(el.start < end && el.end > end)||(el.start>start && el.end<end)){
            return false
        }
    }
    Calendars[i].addEvent({id: ""+EventId,
    title: document.getElementById('eventActivity['+i+']').value,
    start : start,
    end : end,
    allDay: false,
    eventDisplay: 'list-item',
    description: "Test"}
    );
    EventId = EventId + 1;
    Calendars[i].render()
}

function deletePerson(i) {
    document.getElementById("peopleFormContainer[" + i + "]").remove()
}

function deleteEvent(e){
    for (var calendar of Calendars){
        calendar.getEventById(e).remove()
    }
    
}