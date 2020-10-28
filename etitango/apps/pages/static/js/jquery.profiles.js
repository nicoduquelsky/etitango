$(document).ready(function() {
  $("#id_country").change(function() {changeProvince();});
  $("#id_province").change(function() {changeCity();});
});

function changeProvince() {
  var countryId = $("#id_country").val();
  var url = $("#edit_profile_form").attr("data-provinces-url");
  $.ajax({
    url: url,
    data: {
      'country': countryId
    },
    success: function(result) {
      $("#id_province").html(result);
    }
  });
  changeCity();
}

function changeCity() {
  var url = $("#edit_profile_form").attr("data-cities-url");
  var provinceId = $("#id_province").val();
  $.ajax({
    url: url,
    data: {
      'province': provinceId
    },
    success: function(data) {
      $("#id_city").html(data);
    }
  });
}