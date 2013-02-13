$(document).ready(function() {
    // change this value to "Markdown" for that to be the default output
    var source_type = "HTML";
    // var source_type = "Markdown";

    function addSource(display_type, name, source) {
        var html = '<li name="'+ name +'">'+source+
            '<i class="icon-align-justify hidden"></i>'+
            '<i class="icon-remove hidden"></i></li>';
        $(display_type).append(html);
    }

    function manageSource() {
        $(".image-html, .image-markdown").sortable(
            { handle: '.icon-align-justify', cursor: 'crosshair'});
        $(".image-selector > ul > li").hover( function() {
            $(this).children('i').removeClass("hidden");
        }, function() {
            $(this).children('i').addClass("hidden");
        });
        $(".icon-remove").click(function () {
            var parent = $(this).parents("li");
            var name = parent.attr("name");

            // click the appropriate thumbnail
            $(".thumbnails").find("li").each(function(i) {
                if ( $(this).attr("name") == name ){
                    $(this).children().click();
                }
            });
            parent.remove();
        });
    }

    $('button').click(function(){
        $(this).button('toggle');
        if ( $(this).is('.html') ) {
            $('.image-markdown').addClass("hidden");
            $('.image-html').removeClass("hidden");
        } else {
            $('.image-html').addClass("hidden");
            $('.image-markdown').removeClass("hidden");
        }
    });

    if (source_type=="HTML") {
        $('button.html').click();
    } else {
        $('button.markdown').click();
    }

    $('.thumbnail').toggle(
        function(){
            $(this).addClass("selected-link");
            var location = $(this).children().attr("src");
            var name = location.split("/").pop();
            var source = '&lt;img src="' + location +
                '" alt="' + name + '"&gt;';
            addSource('.image-html', name, source);
            // $('.image-html').append('<li name="'+ name +'">'+source+'</li>');
            var source = '!['+ name + '](' +
                location + ')';
            addSource('.image-markdown', name, source);
            manageSource();
        },
        function(){
            var location = $(this).children().attr("src");
            var name = location.split("/").pop();
            console.log("toggle thingy");
            manageSource();
            $(this).removeClass("selected-link");
            $(".image-selector").find("li").each(function(i) {
                if ( $(this).attr("name")==name ) {
                    $(this).remove();
                }
            });

        });

});