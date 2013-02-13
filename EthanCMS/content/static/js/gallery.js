$(document).ready(function() {

    $('.thumbnail').hover(
        function(){
            $(this).addClass("highlight-link")
        },
        function(){
            $(this).removeClass("highlight-link")
        })

});
