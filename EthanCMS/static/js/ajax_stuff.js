$(document).ready(function() {
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;}}}
		return cookieValue;}

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));}

	$.ajaxSetup({
		crossDomain: false, // obviates need for sameOrigin test
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);}}});

	var csrftoken = getCookie('csrftoken');


	// form-specific handlers from here down

	// handle form submission and initiate response actions
	$('#submit_gs_query').submit(function(event){
		event.preventDefault();
		var form = this;
		var data = {};
		data.post_data = $(form).find('input[name=gs_query]').val();
		$.post("/blog/ajax_test/",
			data,
			function(responseData) {
				// call external function on response
				showSongs(responseData);
			},"json");
		$("#submit_gs_query")[0].reset(); // clear the form
	});

	function showSongs(responseData) {
		$("#song_list #no_songs").css("display", "none");
		$("#song_list").append(responseData.song_html)
	}

	// make songs sortable by mouse
	$("#song_list").sortable({ cursor: 'crosshair', containment: 'parent' });

	// submit playlist and name
	// make this a link to the next page as well.
	$("#orderedlist").find("li").each(function(i) {
		$(this).append( " BAM! " + i );
	});


	// change link appearance on mouseover
	$('#links a').hover(
		function(){
			$(this).addClass("highlight_link")
			// $(this).css("background", "blue")
		},
		function(){
			$(this).removeClass("highlight_link")
			$(this).css("background", "black")
		})

});