$(document).ready(function () {
    $('#addTalent').click(function()
    {
        var index = $('.talent').children().length

        $('.talent').append('<li><label for="talent-' + index + '">Talent-' + index + '</label> <table id="talent-' + index + '"><tr><th><label for="talent-' + index + '-start_time">start_time</label></th><td><input id="talent-' + index + '-start_time" name="talent-' + index + '-start_time" type="time" value=""></td></tr><tr><th><label for="talent-' + index + '-name">name</label></th><td><input id="talent-' + index + '-name" name="talent-' + index + '-name" type="text" value=""></td></tr><tr><th><label for="talent-' + index + '-agency">agency</label></th><td><input id="talent-' + index + '-agency" name="talent-' + index + '-agency" type="text" value=""></td></tr><tr><th><label for="talent-' + index + '-notes">notes</label></th><td><input id="talent-' + index + '-notes" name="talent-' + index + '-notes" type="text" value=""></td></tr></table></li>')

        }
    );


  
});



function saveValues(parent) {


    $(parent).find(".form-control").each(function (i) {
        console.log($(this).val());
    });
};