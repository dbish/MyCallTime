$(document).ready(function () {
    var count = $("input[type='radio']").length
    if (count > 0){
        $("input[type=radio]:first-child").attr('checked', 'checked');
    };

    var today = new Date();

    $('.date').each(function () {
        dateText = $(this).text();
        if (dateText != "None") {
            var date = new Date(dateText);
            if (date < today) {
                $(this).parent().addClass("past");
            };
        };
       
    });


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

    $('#filter').keyup(function () {

        var rex = new RegExp($(this).val(), 'i');
        $('.searchable tr').hide();
        $('.searchable tr').filter(function () {
            return rex.test($(this).text());
        }).show();

    });



  
});
