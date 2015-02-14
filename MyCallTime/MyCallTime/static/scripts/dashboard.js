$(document).ready(function () {
    var count = $("input[type='radio']").length
    if (count > 0){
        $("input[type=radio]:first-child").attr('checked', 'checked');
    };

    $('#editShoot').click(function()
    {

        var shootID = $("input[type='radio']:checked").val();
        window.location = "/shoots/"+shootID;

        }
    );

    $('#duplicateShoot').click(function () {
        var shootID = $("input[type='radio']:checked").val();
        window.location = "/copy/" + shootID;

    }
       );
  
    $('#deleteShoot').click(function () {
        var shootID = $("input[type='radio']:checked").val();
        window.location = "/delete/" + shootID;

    }
     );

  
});
