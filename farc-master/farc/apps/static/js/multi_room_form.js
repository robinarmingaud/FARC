function addRow() {
    /* Declare variables */
    var elements, templateRow, rowCount, row, className, newRow, element;
    var i, s, t;
    
    /* Get and count all "tr" elements with class="row".    The last one will
     * be serve as a template. */
    if (!document.getElementsByTagName)
        return false; /* DOM not supported */
    elements = document.getElementsByTagName("tr");
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
        if (className != "row_to_clone")
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
    elements = newRow.getElementsByTagName("input");
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
    
    /* Add the newly-created row to the table */
    templateRow.parentNode.appendChild(newRow);
    return true;
}