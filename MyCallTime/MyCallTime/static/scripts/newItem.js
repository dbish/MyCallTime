$(document).ready(function () {
    $('#addTalent').click(function()
    {
        var index = $('#talentList').children().length


        var newHtml ='<li class="well">'
        newHtml += '<input id="talent-' + index + '-csrf_token" name="talent-' + index + '-csrf_token" type="hidden" value="None">'
        newHtml += '<div class="row">'
        newHtml +=                        '<div class="col-md-5">'
        newHtml +=                            '<label>Name</label>'
        newHtml += '<div><input id="talent-' + index + '-full_name" name="talent-' + index + '-full_name" type="text" value=""></div>'
        newHtml +=                        '</div>'
        newHtml +=                        '<div class="col-md-5">'
        newHtml +=                             '<label>Call Time</label>'
        newHtml += '<div><input id="talent-' + index + '-start_time" name="talent-' + index + '-start_time" type="time" value=""></div>'
        newHtml +=                        '</div>'
        newHtml +=                      '</div>'
        newHtml +=                    '<div class="row">'
        newHtml +=                       '<div class="col-md-5">'
        newHtml +=                           '<label>Agent/Contact</label>'
        newHtml += '<div><input id="talent-' + index + '-agency" name="talent-' + index + '-agency" type="text" value=""</div>'
        newHtml += '<div><input id="talent-' + index + '-notes" name="talent-' + index + '-notes" type="text" value=""></div>'
        newHtml +=                       '</div>'
        newHtml +=                  '</div>'
        newHtml +=              '</li>'



        $('#talentList').append(newHtml)
        }
    );


  
});
