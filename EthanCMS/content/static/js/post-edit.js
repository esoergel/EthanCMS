(function () {
    var converter1 = Markdown.getSanitizingConverter();
    var editor1 = new Markdown.Editor(converter1);
    editor1.run();

    var converter2 = new Markdown.Converter();

    converter2.hooks.chain("preConversion", function (text) {
        return text.replace(/\b(a\w*)/gi, "*$1*");
    });

    converter2.hooks.chain("plainLinkText", function (url) {
        return "This is a link to " + url.replace(/^https?:\/\//, "");
    });

    var help = function () { alert("Do you need help?"); }
    var options = {
        helpButton: { handler: help },
        strings: { quoteexample: "whatever you're quoting, put it right here" }
    };
    var editor2 = new Markdown.Editor(converter2, "-second", options);

    editor2.run();
})();


// var http = require("http"),
//     url = require("url"),
//     querystring = require("querystring"),
//     Converter = require("../../Markdown.Converter").Converter,
//     getSanitizingConverter = require("../../Markdown.Sanitizer").getSanitizingConverter,
//     conv = new Converter(),
//     saneConv = getSanitizingConverter();

// http.createServer(function (req, res) {

//     var route = url.parse(req.url);
//     if (route.pathname !== "/") {
//         res.writeHead(404);
//         res.end("Page not found");
//         return;
//     }

//     var query = querystring.parse(route.query);

//     res.writeHead(200, { "Content-type": "text/html" });
//     res.write("<html><body>");

//     var markdown = query.md || "## Hello!\n\n<marquee>I'm walking</marquee>\n\nVisit [Stack Overflow](http://stackoverflow.com)\n\n<b><i>This is never closed!";

//     res.write("<h1>Your output, sanitized:</h1>\n" + saneConv.makeHtml(markdown))
//     res.write("<h1>Your output, unsanitized:</h1>\n" + conv.makeHtml(markdown))

//     res.write(
//         "<h1>Enter Markdown</h1>\n" +
//         "<form method='get' action='/'>" +
//             "<textarea cols=50 rows=10 name='md'>" +
//                 markdown.replace(/</g, "&lt;") +
//             "</textarea><br>" +
//             "<input type='submit' value='Convert!'>" +
//         "</form>"
//     );

//     res.end("</body></html>");

// }).listen(8000);