$(document).ready(function () {

    $('#title').text($('#name').val());

    $(':input').change(
        function () {
            $(this).css({ 'background-color': '#FFCCCC' });
        }
        );

    $('#addTalent').click(function()
    {
        var index = $('#talentList').children().length

        var newHtml ='<li class="well">'
        newHtml += '<input id="talent-' + index + '-csrf_token" name="talent-' + index + '-csrf_token" type="hidden" value="None">'
        newHtml += '<div class="archived hide"><input id="talent-' + index + '-archived" name="talent-' + index + '-archived" step="1" type="number" value=""></div>'
        newHtml +='<div class="row">'
        newHtml +='<div class="col-md-5">'
        newHtml +='<label>Name</label>'
        newHtml += '<div><input id="talent-' + index + '-full_name" name="talent-' + index + '-full_name" type="text" value=""></div>'
        newHtml +='</div>'
        newHtml +='<div class="col-md-5">'
        newHtml +='<label>Call Time</label>'
        newHtml += '<div><input id="talent-' + index + '-start_time" name="talent-' + index + '-start_time" type="time" value=""></div>'
        newHtml +='</div>'
        newHtml +='</div>'
        newHtml +='<div class="row">'
        newHtml +='<div class="col-md-5">'
        newHtml +='<label>Agent/Contact</label>'
        newHtml += '<div><input id="talent-' + index + '-agent_name" name="talent-' + index + '-agent_name" placeholder="name" type="text" value=""></div>'
        newHtml += '<div><input id="talent-' + index + '-agent_email" name="talent-' + index + '-agent_email" placeholder="email" type="text" value=""></div>'
        newHtml += '<div><input id="talent-' + index + '-agent_phone" name="talent-' + index + '-agent_phone" placeholder="phone" type="text" value=""></div>'
        newHtml +='</div>'
        newHtml +='</div>'
        newHtml +='<div class="col-md-1" style="float:right"><span class="fake-link deleteTalent">-delete-</span></div>'    
        newHtml +='</li>'

        $('#talentList').append(newHtml)

        }
    );

    $('#addProdAssistant').click(function () {
        var index = $('#prodAssistants').children().length
        var newHtml = '<div class="col-md-5 assistant">'
        newHtml += '<div class="archived hide"><input id="production-assistants-' + index + '-archived" name="production-assistants-' + index + '-archived" step="1" type="number" value=""></div>'
        newHtml += '<div class="row col-lg-6"><div class="col-lg-3"><label>Assistant</label></div><div class="col-lg-1" style="float:right"><span class="fake-link deleteAssist">x</span></div></div>'
        newHtml += '<div class="row col-lg-9"><input id="production-assistants-' + index + '-assistantName" name="production-assistants-' + index + '-assistantName" placeholder="name" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="production-assistants-' + index + '-email" name="production-assistants-' + index + '-email" placeholder="email" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="production-assistants-' + index + '-phone" name="production-assistants-' + index + '-phone" placeholder="phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#prodAssistants').append(newHtml)
        
    }
    );

    $('#addPhotoAssistant').click(function () {
        var index = $('#photoAssistants').children().length
        var newHtml = '<div class="col-md-5 assistant">'
        newHtml += '<div class="archived hide"><input id="photo-assistants-' + index + '-archived" name="photo-assistants-' + index + '-archived" step="1" type="number" value=""></div>'
        newHtml += '<div class="row col-lg-6"><div class="col-lg-3"><label>Assistant</label></div><div class="col-lg-1" style="float:right"><span class="fake-link deleteAssist">x</span></div></div>'
        newHtml += '<div class="row col-lg-9"><input id="photo-assistants-' + index + '-assistantName" name="photo-assistants-' + index + '-assistantName" placeholder="name" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="photo-assistants-' + index + '-email" name="photo-assistants-' + index + '-email" placeholder="email" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="photo-assistants-' + index + '-phone" name="photo-assistants-' + index + '-phone" placeholder="phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#photoAssistants').append(newHtml)

    }
   );

    $('#addMakeupAssistant').click(function () {
        var index = $('#makeupAssistants').children().length
        var newHtml = '<div class="col-md-5 assistant">'
        newHtml += '<div class="archived hide"><input id="makeup-assistants-' + index + '-archived" name="makeup-assistants-' + index + '-archived" step="1" type="number" value=""></div>'
        newHtml += '<div class="row col-lg-6"><div class="col-lg-3"><label>Assistant</label></div><div class="col-lg-1" style="float:right"><span class="fake-link deleteAssist">x</span></div></div>'
        newHtml += '<div class="row col-lg-9"><input id="makeup-assistants-' + index + '-assistantName" name="makeup-assistants-' + index + '-assistantName" placeholder="name" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="makeup-assistants-' + index + '-email" name="makeup-assistants-' + index + '-email" placeholder="email" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="makeup-assistants-' + index + '-phone" name="makeup-assistants-' + index + '-phone" placeholder="phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#makeupAssistants').append(newHtml)

    }
   );

    $('#addArtAssistant').click(function () {
        var index = $('#artAssistants').children().length
        var newHtml = '<div class="col-md-5 assistant">'
        newHtml += '<div class="archived hide"><input id="art-assistants-' + index + '-archived" name="art-assistants-' + index + '-archived" step="1" type="number" value=""></div>'
        newHtml += '<div class="row col-lg-6"><div class="col-lg-3"><label>Assistant</label></div><div class="col-lg-1" style="float:right"><span class="fake-link deleteAssist">x</span></div></div>'
        newHtml += '<div class="row col-lg-9"><input id="art-assistants-' + index + '-assistantName" name="art-assistants-' + index + '-assistantName" placeholder="name" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="art-assistants-' + index + '-email" name="art-assistants-' + index + '-email" placeholder="email" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="art-assistants-' + index + '-phone" name="art-assistants-' + index + '-phone" placeholder="phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#artAssistants').append(newHtml)

    }
   );

    $('#addWardrobeAssistant').click(function () {
        var index = $('#wardrobeAssistants').children().length
        var newHtml = '<div class="col-md-5 assistant">'
        newHtml += '<div class="archived hide"><input id="wardrobe-assistants-' + index + '-archived" name="wardrobe-assistants-' + index + '-archived" step="1" type="number" value=""></div>'
        newHtml += '<div class="row col-lg-6"><div class="col-lg-3"><label>Assistant</label></div><div class="col-lg-1" style="float:right"><span class="fake-link deleteAssist">x</span></div></div>'
        newHtml += '<div class="row col-lg-9"><input id="wardrobe-assistants-' + index + '-assistantName" name="wardrobe-assistants-' + index + '-assistantName" placeholder="name" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="wardrobe-assistants-' + index + '-email" name="wardrobe-assistants-' + index + '-email" placeholder="email" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="wardrobe-assistants-' + index + '-phone" name="wardrobe-assistants-' + index + '-phone" placeholder="phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#wardrobeAssistants').append(newHtml)

    }
   );

    $('#addHairAssistant').click(function () {
        var index = $('#hairAssistants').children().length
        var newHtml = '<div class="col-md-5 assistant">'
        newHtml += '<div class="archived hide"><input id="hair-assistants-' + index + '-archived" name="hair-assistants-' + index + '-archived" step="1" type="number" value=""></div>'
        newHtml += '<div class="row col-lg-6"><div class="col-lg-3"><label>Assistant</label></div><div class="col-lg-1" style="float:right"><span class="fake-link deleteAssist">x</span></div></div>'
        newHtml += '<div class="row col-lg-9"><input id="hair-assistants-' + index + '-assistantName" name="hair-assistants-' + index + '-assistantName" placeholder="name" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="hair-assistants-' + index + '-email" name="hair-assistants-' + index + '-email" placeholder="email" type="text" value=""></div>'
        newHtml += '<div class="row col-lg-9"><input id="hair-assistants-' + index + '-phone" name="hair-assistants-' + index + '-phone" placeholder="phone" type="text" value=""></div>'
        newHtml += '</div>'
        $('#hairAssistants').append(newHtml)

    }
   );

    $('#talentList').on("click", '.deleteTalent', function () {
        alert("delete");
        $(this).parent().parent().find(".archived").find("input").val(1);
        $(this).parent().parent().addClass('deleted');
        $('#talent').prepend('<div class="unsaved"><p>- unsaved deletion -</p></div>');

    });

    $('.assistants').on("click", '.deleteAssist', function () {
        $(this).parent().parent().parent().find(".archived").find("input").val(1);
        $(this).parent().parent().parent().addClass('deleted');
        $(this).parent().parent().parent().parent().prepend('<div class="unsaved"><p> - unsaved deletion -</p></div>');

    });

  
});
