$(document).ready(function () { $(".btn-link").on('click', function() {
    var parent = $(this).parent().parent()
    var table = parent.find("table")
    table.table2csv();
    })
})