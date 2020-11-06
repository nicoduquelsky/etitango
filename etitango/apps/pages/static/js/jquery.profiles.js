$(document).ready(function() {
  initPage();
  $("#id_country").change(function() {
    loadProvinces();
    setTimeout(function() {loadCities();}, 200);
  });
  $("#id_province").change(function() {loadCities();});
});

function initPage() {
  var provVal = $("#id_province").val();
  var cityVal = $("#id_city").val();
  loadProvinces();
  loadCities();
  setTimeout(function() {
    $("#id_province").val(provVal);
    $("#id_city").val(cityVal);
  }, 500);
}

function loadProvinces() {
  var url = $("#edit_profile_form").attr("data-provinces-url");
  var countryId = $("#id_country").val();
  ajaxCall('country', countryId);
}

function loadCities() {
  var url = $("#edit_profile_form").attr("data-cities-url");
  var provinceId = $("#id_province").val();
  if (!provinceId) {
    $("#id_city").html("<option value=''>None</option>");
  }
  else {
    ajaxCall('province', provinceId);
  }
}

function ajaxCall(location, locationId) {
  var url="";
  var selector="";
  var data={};
  
  switch (location) {
    case 'country':
      selector = "#id_province";
      url = $("#edit_profile_form").attr("data-provinces-url");
      data = {'country': locationId};
      break;
    
    case 'province':
      selector = "#id_city";
      url = $("#edit_profile_form").attr("data-cities-url");
      data = {'province': locationId}
      break;
  }

  $.ajax({
      url: url,
      data: data,
      success: function(data) {$(selector).html(data);}
  });
}