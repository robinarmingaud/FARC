function addRoom() {
    /* Declare variables */
    var elements, templateRow, rowCount, row, className, newRow, element;
    var i, s, t;
    
    /* Get and count all "tr" elements with class="row".    The last one will
     * be serve as a template. */
    if (!document.getElementsByTagName)
        return false; /* DOM not supported */
    elements = document.getElementsByClassName("RoomForm");
    templateRow = null;
    rowCount = 0;
    for (i = 0; i < elements.length; i++) {
        row = elements.item(i);
        elementsrow = row.querySelectorAll("*");
        for (j = 0; j < elementsrow.length; j++) {
            element = elementsrow.item(j);
            s = null;
            s = element.getAttribute("name");
            if (s == null)
                continue;
            t = s.split("[");
            if (t.length < 2)
                continue;
            s = t[0] + "[" + i.toString() + "]";
            element.setAttribute("name", s);
            element.value = "";
        }
        for (j = 0; j < elementsrow.length; j++) {
            element = elementsrow.item(j);
            s = null;
            s = element.getAttribute("id");
            if (s == null)
                continue;
            t = s.split("[");
            if (t.length < 2)
                continue;
            s = t[0] + "[" + i.toString() + "]";
            element.setAttribute("id", s);
            element.value = "";
        }
        row.getElementsByTagName("div")[1].innerText = i;

        $('#deleteRoom\\['+ i + '\\]').on('click', function() {
            var room = document.getElementById('roomFormContainer['+ i + ']');
            if (document.getElementsByClassName('RoomForm').length>1){
                room.parentNode.remove();
            }
        })

        
        /* Get the "class" attribute of the row. */
        className = null;
        if (row.getAttribute)
            className = row.getAttribute('class')
        if (className == null && row.attributes) {    // MSIE 5
            /* getAttribute('class') always returns null on MSIE 5, and
             * row.attributes doesn't work on Firefox 1.0.    Go figure. */
            className = row.attributes['class'];
            if (className && typeof(className) == 'object' && className.value) {
                // MSIE 6
                className = className.value;
            }
        }
        
        /* This is not one of the rows we're looking for.    Move along. */
        if (className != "RoomForm")
            continue;
        
        /* This *is* a row we're looking for. */
        templateRow = row;
        rowCount++;
    }
    if (templateRow == null)
        return false; /* Couldn't find a template row. */
    
    /* Make a copy of the template row */
    newRow = templateRow.cloneNode(true);

    newRow.getElementsByTagName("div")[1].innerText = rowCount;


    /* Change the form variables e.g. price[x] -> price[rowCount] */
    elements = newRow.querySelectorAll("*");
    for (i = 0; i < elements.length; i++) {
        element = elements.item(i);
        s = null;
        s = element.getAttribute("name");
        if (s == null)
            continue;
        t = s.split("[");
        if (t.length < 2)
            continue;
        s = t[0] + "[" + rowCount.toString() + "]";
        element.setAttribute("name", s);
        element.value = "";
    }
    for (i = 0; i < elements.length; i++) {
        element = elements.item(i);
        s = null;
        s = element.getAttribute("id");
        if (s == null)
            continue;
        t = s.split("[");
        if (t.length < 2)
            continue;
        s = t[0] + "[" + rowCount.toString() + "]";
        element.setAttribute("id", s);
        element.value = "";
    }


    /* Add the newly-created row to the table */
    templateRow.parentNode.appendChild(newRow);

    
    $('#deleteRoom\\['+ rowCount + '\\]').on('click', function() {
        var room = document.getElementById('roomFormContainer['+ rowCount + ']');
        if (document.getElementsByClassName('RoomForm').length>1){
            room.parentNode.remove();
        }
    })

    return true;
}

function addPerson() {
    /* Declare variables */
    var elements, templateRow, rowCount, row, className, newRow, element;
    var i, s, t;
    
    /* Get and count all "tr" elements with class="row".    The last one will
     * be serve as a template. */
    if (!document.getElementsByTagName)
        return false; /* DOM not supported */
    elements = document.getElementsByClassName("PeopleForm");
    templateRow = null;
    rowCount = 0;
    for (i = 0; i < elements.length; i++) {
        row = elements.item(i);
        
        /* Get the "class" attribute of the row. */
        className = null;
        if (row.getAttribute)
            className = row.getAttribute('class')
        if (className == null && row.attributes) {    // MSIE 5
            /* getAttribute('class') always returns null on MSIE 5, and
             * row.attributes doesn't work on Firefox 1.0.    Go figure. */
            className = row.attributes['class'];
            if (className && typeof(className) == 'object' && className.value) {
                // MSIE 6
                className = className.value;
            }
        } 
        
        /* This is not one of the rows we're looking for.    Move along. */
        if (className != "PeopleForm")
            continue;
        
        /* This *is* a row we're looking for. */
        templateRow = row;
        rowCount++;
    }
    if (templateRow == null)
        return false; /* Couldn't find a template row. */
    
    /* Make a copy of the template row */
    newRow = templateRow.cloneNode(true);

    newRow.getElementsByTagName("div")[0].innerText = rowCount;

    /* Change the form variables e.g. price[x] -> price[rowCount] */
    elements = newRow.querySelectorAll("*");
    for (i = 0; i < elements.length; i++) {
        element = elements.item(i);
        s = null;
        s = element.getAttribute("name");
        if (s == null)
            continue;
        t = s.split("[");
        if (t.length < 2)
            continue;
        s = t[0] + "[" + rowCount.toString() + "]";
        element.setAttribute("name", s);
        element.value = "";
    }
    for (i = 0; i < elements.length; i++) {
        element = elements.item(i);
        s = null;
        s = element.getAttribute("id");
        if (s == null)
            continue;
        t = s.split("[");
        if (t.length < 2)
            continue;
        s = t[0] + "[" + rowCount.toString() + "]";
        element.setAttribute("id", s);
        element.value = "";
    }
    for (i = 0; i < elements.length; i++) {
        element = elements.item(i);
        s = null;
        s = element.getAttribute("data-target");
        if (s == null)
            continue;
        t = s.split("[");
        if (t.length < 2)
            continue;
        s = t[0] + "[" + rowCount.toString() + "\\]";
        element.setAttribute("data-target", s);
        element.value = "";
    }
    /* Add the newly-created row to the table */
    templateRow.parentNode.appendChild(newRow);


    document.getElementById('calendar['+ rowCount +']').innerHTML = "";

        var calendarEl = document.getElementById('calendar['+ rowCount +']');
      
        var calendar = new FullCalendar.Calendar(calendarEl, {
          initialView: 'timeGridDay',
          headerToolbar: false,
          dayHeaders: false,
          slotDuration: '00:15:00',
          slotMinTime:  "06:00:00",
          slotMaxTime:  "21:00:00",
          aspectRatio: 2,
          dateClick: function(info) {
            alert('Clicked on: ' + info.dateStr);
          }
        });

        calendar.render();
    
        $('a[href="#people_data_form"]').on('shown.bs.tab',function(){
            calendar.render();
        });
    
        var eventId = 0;
        $('#saveEvent\\['+ rowCount + '\\]').on('click', function() {
            var start = new Date();
            var end = new Date();
            start_hour = document.getElementById('event_start['+ rowCount +']').value.split(':');
            end_hour = document.getElementById('event_finish['+ rowCount +']').value.split(':');
            start.setHours(start_hour[0], start_hour[1]);
            end.setHours(end_hour[0], end_hour[1]);
            calendar.addEvent({id: ""+eventId,
            title: document.getElementById('eventActivity['+ rowCount +']').value,
            start : start,
            end : end,
            allDay: false,
            eventDisplay: 'list-item',
            description: "Musculation"}
            );
    
            eventId = eventId + 1;
        });

        

    return true;
}

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar[0]');
  
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'timeGridDay',
      headerToolbar: false,
      dayHeaders: false,
      slotDuration: '00:15:00',
      slotMinTime:  "06:00:00",
      slotMaxTime:  "21:00:00",
      aspectRatio: 2,
      dateClick: function(info) {
        alert('Clicked on: ' + info.dateStr);
      }
    });

    $('a[href="#people_data_form"]').on('shown.bs.tab',function(){
        calendar.render();
    });

    var eventId = 0;
    $('#saveEvent\\[0\\]').on('click', function() {
        var start = new Date();
        var end = new Date();
        start_hour = document.getElementById('event_start[0]').value.split(':');
        end_hour = document.getElementById('event_finish[0]').value.split(':');
        start.setHours(start_hour[0], start_hour[1]);
        end.setHours(end_hour[0], end_hour[1]);
        calendar.addEvent({id: ""+eventId,
        title: document.getElementById('eventActivity[0]').value,
        start : start,
        end : end,
        allDay: false,
        eventDisplay: 'list-item',
        description: "Musculation"}
        );

        eventId = eventId + 1;
    })
  });

  $('#deleteRoom\\[0\\]').on('click', function() {
    var room = document.getElementById('roomFormContainer[0]');
    if (document.getElementsByClassName('RoomForm').length>1){
        room.parentNode.remove();
    }
})

  
