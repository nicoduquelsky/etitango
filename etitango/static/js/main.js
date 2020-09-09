$(document).ready(function() {
    $("#addButton").click(function() {cloneForm("#addEditorForm", "form");});
    $("#removeButton").click(function() {removeForm("#addEditorForm", "form");});
  });

  function cloneForm(selector, type) {
    var totalForms = $("#id_" + type + "-TOTAL_FORMS");
    var total = totalForms.val();
    var srcForm = $(selector);
    var baseForm = srcForm.find("div.form-group:first");
    // var baseForm = srcForm.find("#id_id_" + type + "-0-members");
    // var baseForm = $('#' + srcForm.find("div:first").attr("id"));
    var newForm = baseForm.clone(true);
    newForm.find(":input").each(function(){
      var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
      var id = "id_" + name;
      $(this).attr("value","");
      $(this).attr({"name":name, "id":id}).val("").removeAttr("checked");
    });
    total++;
    totalForms.val(total);
    //srcForm.find("div.form-group").last().after(newForm);
    srcForm.find("div.form-group:last").after(newForm);
  }

  function removeForm(selector, type) {
    var totalForms = $("#id_" + type + "-TOTAL_FORMS");
    var total = totalForms.val();
    var div = $(selector);
    if (total > 1) {
      div.find("div.form-group:last").remove();
      total--;
      totalForms.val(total);
    }
  }