function initRegisterPage() {
    $("#id_country").change(function() {
        loadProvinces("#register-form");
        setTimeout(function() {loadCities("#register-form");}, 200);
      });
    $("#id_province").change(function() {loadCities("#register-form");});
    loadProvinces("#register-form");
    loadCities("#register-form");
}

function initEditProfilePage() {
    var provVal = $("#id_province").val();
    var cityVal = $("#id_city").val();
    loadProvinces("#edit_profile_form");
    loadCities("#edit_profile_form");
    setTimeout(function() {
      $("#id_province").val(provVal);
      $("#id_city").val(cityVal);
    }, 500);
  }

function loadProvinces(formSelector) {
    var url = $(formSelector).attr("data-provinces-url");
    var countryId = $("#id_country").val();
    ajaxCall(formSelector, 'country', countryId);
}
  
function loadCities(formSelector) {
    var url = $(formSelector).attr("data-cities-url");
    var provinceId = $("#id_province").val();
    if (!provinceId) {
        $("#id_city").html("<option value=''>None</option>");
    }
    else {
        ajaxCall(formSelector, 'province', provinceId);
    }
}
  
function ajaxCall(formSelector, location, locationId) {
  var url="";
  var selector="";
  var data={};
  
  switch (location) {
    case 'country':
      selector = "#id_province";
      url = $(formSelector).attr("data-provinces-url");
      data = {'country': locationId};
      break;
    
    case 'province':
      selector = "#id_city";
      url = $(formSelector).attr("data-cities-url");
      data = {'province': locationId}
      break;
  }

  $.ajax({
      url: url,
      data: data,
      success: function(data) {$(selector).html(data);}
  });
}