$(document).ready(function () { $(".btn-link").on('click', function() {
    var utc = new Date().toJSON()
    var parent = $(this).parent().parent()
    var table = parent.find("table")
    var title = parent.find("#DivProbabilityOfInfection").attr('value');
    table.table2csv({filename: (utc+title+'.csv').replace(/:/g,"_")});
    })
})