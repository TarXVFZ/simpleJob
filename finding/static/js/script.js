$(function() {
	$(".button_send").click(function() {
		$.ajax({
			type: "post",
			url: '/find/',
			data: {
				tegs: $('.input_send').val()
			},
			success: function(request) {
				if (request != "bad") {
					alert(request);
					$('.input_send').val("");
				} else
					alert("Bad request!");
			}
		});
	});
});