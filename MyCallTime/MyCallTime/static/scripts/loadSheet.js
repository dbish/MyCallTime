$(document).ready(function () {
    console.log('ready!');
    talentPanel = $('#collapseTalent > .panel-body > .row > .col-lg-6');
    talentPanel.append('<div class="input-group"><label>Talent</label></div>');
    talentPanel.append('<div class="input-group"><div class="input-group-btn"><input type="time" class="form-control"></div><input type="text" class="form-control"></div>');
});