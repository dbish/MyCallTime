$(document).ready(function () {
    //$(".btn-success").click(function () {
    //    saveValues($(this).parent());
    //});

    $('.btn-success').bind('click', function () {
        $.post($SCRIPT_ROOT + '/save', {
            name: $('input[name="shootName"]').val(),
            client: $('input[name="client"]').val(),
            contactName: $('input[name="contactName"]').val(),
            contactEmail: $('input[name="contactEmail"]').val(),
            contactPhone: $('input[name="contactPhone"]').val(),
            date: $('input[name="date"]').val(),
            startTime: $('input[name="startTime"]').val(),
            wrapTime: $('input[name="wrapTime"]').val(),
            location: $('input[name="location"]').val(),
            studio: $('input[name="studio"]').val()
        }, function (data) {
            $("#result").text(data.result);
        }, "json");
        return false;
    });

  
});



function saveValues(parent) {


    $(parent).find(".form-control").each(function (i) {
        console.log($(this).val());
    });
};