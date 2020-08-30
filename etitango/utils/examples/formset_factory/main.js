$(document).ready(function() {
    $("#addButton").click(function() {cloneForm("#expenditureTable", "form");});
    $("#removeButton").click(function() {removeForm("#expenditureTable", "form");});
  });
  
  function cloneForm(selector, type) {
    var totalForms = $("#id_" + type + "-TOTAL_FORMS");
    var total = totalForms.val();
    var table = $(selector);
    var baseForm = table.find("tr:last");
    var newForm = baseForm.clone(true);
    newForm.find(":input").each(function(){
      var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
      var id = "id_" + name;
      $(this).attr("value","");
      $(this).attr({"name":name, "id":id}).val("").removeAttr("checked");
    });
    total++;
    totalForms.val(total);
    baseForm.after(newForm);
  }
  
  function removeForm(selector, type) {
    var totalForms = $("#id_" + type + "-TOTAL_FORMS");
    var total = totalForms.val();
    var table = $(selector);
    if (total > 1) {
      table.find("tr:last").remove();
      total--;
      totalForms.val(total);
    }
  }  