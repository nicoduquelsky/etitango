$(document).ready(function() {
    $("#id_country").change(function() {
        var url = $("#edit_profile_form").attr("data-provinces-url");
        var countryId = $(this).val();
        $.ajax({
          url: url,
          data: {
            'country': countryId
          },
          success: function(result) {
            $("#id_province").html(result);
          }
        });
      });
      
      $("#id_province").change(function() {
        var url = $("#edit_profile_form").attr("data-cities-url");
        var provinceId = $(this).val();
        $.ajax({
          url: url,
          data: {
            'province': provinceId
          },
          success: function(data) {
            $("#id_city").html(data);
          }
        });
      });
  });