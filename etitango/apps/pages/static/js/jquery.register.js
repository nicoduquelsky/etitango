$(document).ready(function() {
    initRegisterPage();
    $("#id_country").change(function() {
      loadProvinces("#register-form");
      setTimeout(function() {loadCities("#register-form");}, 200);
    });
    $("#id_province").change(function() {loadCities("#register-form");});
  });