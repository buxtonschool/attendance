var $form = $('form#test-form'),
    url = "https://script.google.com/macros/s/AKfycbyzf1nQf4j-IKLplUq5VO5wCAkTncHRkSU77He8JdDs779nc3TI/exec"

$('#submit-form').on('click', function(e) {
  e.preventDefault();
  var jqxhr = $.ajax({
    url: url,
    method: "GET",
    dataType: "json",
    data: $form.serializeObject()
  }).success(
    window.location.href = "http://buxtonschool.github.io/attendance/AdrianAttendance"
  );
  var jqxhr = $.ajax({
    url: url,
    method: "GET",
    dataType: "json",
    data: $form.serializeObject()
  }).success(
    window.location.href = "http://buxtonschool.github.io/attendance/AdrianAttendance"
  );
});