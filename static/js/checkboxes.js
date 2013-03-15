// Form functionality
$(".checkboxes input:checkbox:first").change(function () {
$(".checkboxes").find(':checkbox').prop("checked", this.checked);
});
$('#avatars ul li input:radio:eq(0), #backgrounds ul li input:radio:eq(0)').attr('checked', 'checked');
