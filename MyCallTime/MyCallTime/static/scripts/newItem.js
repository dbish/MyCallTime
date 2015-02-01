$(document).ready(function () {
    $('#addTalent').click(function()
    {
        var index = $('#talentList').children().length

        //$('#talentList').append('<li class="well"><div class="row"><div class="name col-md-4"><label for="talent-' + index + '-name">name</label> <input id="talent-' + index + '-name" name="talent-' + index + '-name" type="text" value=""></div><label for="talent-' + index + '-start_time">start_time</label> <input id="talent-' + index + '-start_time" name="talent-' + index + '-start_time" type="time" value=""></div><div><label for="talent-' + index + '-agency">agency</label> <input id="talent-' + index + '-agency" name="talent-' + index + '-agency" type="text" value=""></div><div><label for="talent-' + index + '-notes">notes</label> <input id="talent-' + index + '-notes" name="talent-' + index + '-notes" type="text" value=""></div></li>')
              
        var newHtml = '<li class="well"><div class="row"><div><input id="talent-' + index + '-csrf_token" name="talent-' + index + '-csrf_token" type="hidden" value=""></div><div class="name col-md-4"><label for="talent-' + index + '-name">name</label>'
        newHtml += '<input id="talent-' + index + '-name" name="talent-' + index + '-name" type="text" value=""></div><div class="start_time col-md-4">'
        newHtml += '<label for="talent-' + index + '-start_time">start_time</label><input id="talent-' + index + '-start_time" name="talent-' + index + '-start_time" type="time" value=""></div>'
        newHtml += '</div><div class="row"><div class="agency col-md-4"><label for="talent-' + index + '-agency">agency</label><input id="talent-' + index + '-agency" name="talent-' + index + '-agency" type="text" value=""></div>'
        newHtml += '</div><div class="row"><div class="notes col-md-4"><label for="talent-' + index + '-notes">notes</label><input id="talent-' + index + '-notes" name="talent-0-notes" type="text" value=""></div></div></li>'
        $('#talentList').append(newHtml)

        }
    );


  
});
