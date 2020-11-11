$(document).ready(function() {
  initEditProfilePage();
  $("#id_country").change(function() {
    loadProvinces("#edit_profile_form");
    setTimeout(function() {loadCities("#edit_profile_form");}, 200);
  });
  $("#id_province").change(function() {loadCities("#edit_profile_form");});
});