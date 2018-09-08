// Variable to hold request
var request;

// Bind to the submit event of our form
$("#foo").submit(function(event){

    // Abort any pending request
    if (request) {
        request.abort();
    }

    window.location.href = "http://buxtonschool.github.io/attendance/CordeliaAttendance";
});