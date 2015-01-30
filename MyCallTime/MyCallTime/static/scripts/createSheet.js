$(document).ready(function () {
    //$('#cancelCreate').hide();

    $('#createSheet').click(function()
    {
        $(".create").show();
        $(".cancel").hide();
        }
    );

    $('#cancelCreate').click(function () {
        $(".create").hide();
        $(".cancel").show();
    }
  );
  
});

