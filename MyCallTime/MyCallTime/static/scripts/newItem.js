$(document).ready(function () {
    $('#addTalent').click(function()
    {
        var index = $('#talentList').children().length

        //$('.talent').append('<li><label for="talent-' + index + '">Talent-' + index + '</label> <table id="talent-' + index + '"><tr><th><label for="talent-' + index + '-start_time">start_time</label></th><td><input id="talent-' + index + '-start_time" name="talent-' + index + '-start_time" type="time" value=""></td></tr><tr><th><label for="talent-' + index + '-name">name</label></th><td><input id="talent-' + index + '-name" name="talent-' + index + '-name" type="text" value=""></td></tr><tr><th><label for="talent-' + index + '-agency">agency</label></th><td><input id="talent-' + index + '-agency" name="talent-' + index + '-agency" type="text" value=""></td></tr><tr><th><label for="talent-' + index + '-notes">notes</label></th><td><input id="talent-' + index + '-notes" name="talent-' + index + '-notes" type="text" value=""></td></tr></table></li>')
        $('#talentList').append('<li><label for="talent-' + index + '">Talent-' + index + '</label><div><label for="talent-' + index + '-start_time">start_time</label> <input id="talent-' + index + '-start_time" name="talent-' + index + '-start_time" type="time" value=""></div><div><label for="talent-' + index + '-name">name</label> <input id="talent-' + index + '-name" name="talent-' + index + '-name" type="text" value=""></div><div><label for="talent-' + index + '-agency">agency</label> <input id="talent-' + index + '-agency" name="talent-' + index + '-agency" type="text" value=""></div><div><label for="talent-' + index + '-notes">notes</label> <input id="talent-' + index + '-notes" name="talent-' + index + '-notes" type="text" value=""></div></li>')
                                            


        }
    );
  
});



function saveValues(parent) {


    $(parent).find(".form-control").each(function (i) {
        console.log($(this).val());
    });
};