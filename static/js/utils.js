// Modal functionality
$(document).ready(function(){
    setTimeout(function(){
	$('#welcomeModal').modal('show');
	$('#welcomeModal').fadeIn();
    }, 700);
});
// Form functionality
$(".checkboxes input:checkbox:first").change(function () {
$(".checkboxes").find(':checkbox').prop("checked", this.checked);
});