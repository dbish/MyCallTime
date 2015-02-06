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

    $('#addProdAssistant').click(function () {
        var index = $('#prodAssistants').children().length
        var newHtml = '<div class="col-md-5">'
        newHtml +=                  '<label>Assistant</label>'
        newHtml +=                   '<div><input id="production-assistants-' + index + '-assistantName" name="production-assistants-' + index + '-assistantName" type="text" value=""></div>'
         newHtml +=                    '<div><input id="production-assistants-' + index + '-email" name="production-assistants-' + index + '-email" type="text" value=""></div>'
        newHtml +=                    '<div><input id="production-assistants-' + index + '-phone" name="production-assistants-' + index + '-phone" type="text" value=""></div>'
        newHtml +=                '</div>'
        $('#prodAssistants').append(newHtml)
        
    }
    );

    $('#addPhotoAssistant').click(function () {
        var index = $('#photoAssistants').children().length
        var newHtml = '<div class="col-md-5">'
        newHtml += '<label>Assistant</label>'
        newHtml += '<div><input id="photo-assistants-' + index + '-assistantName" name="photo-assistants-' + index + '-assistantName" type="text" value=""></div>'
        newHtml += '<div><input id="photo-assistants-' + index + '-email" name="photo-assistants-' + index + '-email" type="text" value=""></div>'
        newHtml += '<div><input id="photo-assistants-' + index + '-phone" name="photo-assistants-' + index + '-phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#photoAssistants').append(newHtml)

    }
   );

    $('#addMakeupAssistant').click(function () {
        var index = $('#makeupAssistants').children().length
        var newHtml = '<div class="col-md-5">'
        newHtml += '<label>Assistant</label>'
        newHtml += '<div><input id="makeup-assistants-' + index + '-assistantName" name="makeup-assistants-' + index + '-assistantName" type="text" value=""></div>'
        newHtml += '<div><input id="makeup-assistants-' + index + '-email" name="makeup-assistants-' + index + '-email" type="text" value=""></div>'
        newHtml += '<div><input id="makeup-assistants-' + index + '-phone" name="makeup-assistants-' + index + '-phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#makeupAssistants').append(newHtml)

    }
   );

    $('#addArtAssistant').click(function () {
        var index = $('#artAssistants').children().length
        var newHtml = '<div class="col-md-5">'
        newHtml += '<label>Assistant</label>'
        newHtml += '<div><input id="art-assistants-' + index + '-assistantName" name="art-assistants-' + index + '-assistantName" type="text" value=""></div>'
        newHtml += '<div><input id="art-assistants-' + index + '-email" name="art-assistants-' + index + '-email" type="text" value=""></div>'
        newHtml += '<div><input id="art-assistants-' + index + '-phone" name="art-assistants-' + index + '-phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#artAssistants').append(newHtml)

    }
   );

    $('#addWardrobeAssistant').click(function () {
        var index = $('#wardrobeAssistants').children().length
        var newHtml = '<div class="col-md-5">'
        newHtml += '<label>Assistant</label>'
        newHtml += '<div><input id="wardrobe-assistants-' + index + '-assistantName" name="wardrobe-assistants-' + index + '-assistantName" type="text" value=""></div>'
        newHtml += '<div><input id="wardrobe-assistants-' + index + '-email" name="wardrobe-assistants-' + index + '-email" type="text" value=""></div>'
        newHtml += '<div><input id="wardrobe-assistants-' + index + '-phone" name="wardrobe-assistants-' + index + '-phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#wardrobeAssistants').append(newHtml)

    }
   );

    $('#addHairAssistant').click(function () {
        var index = $('#hairAssistants').children().length
        var newHtml = '<div class="col-md-5">'
        newHtml += '<label>Assistant</label>'
        newHtml += '<div><input id="hair-assistants-' + index + '-assistantName" name="hair-assistants-' + index + '-assistantName" type="text" value=""></div>'
        newHtml += '<div><input id="hair-assistants-' + index + '-email" name="hair-assistants-' + index + '-email" type="text" value=""></div>'
        newHtml += '<div><input id="hair-assistants-' + index + '-phone" name="hair-assistants-' + index + '-phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#hairAssistants').append(newHtml)

    }
   );


  
});
