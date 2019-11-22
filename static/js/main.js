/* main JS file */


//
//
//     }

// console.log(NYT)

console.log(content);

function updateContent() {
    var outlets = ["MSNBC", "Huffington Post", "CNN", "Politico", "NYT", "Reuters", "USA Today", "FOX"];

    content.forEach(function (d, i) {

        document.getElementById("outlet" + i).innerHTML = (outlets[i]);
        document.getElementById("outlet" + i).className = "outlet"

        if (content[i].totalResults != 0) {

            document.getElementById("headline" + i).innerHTML = (content[i].articles[0].title)
            document.getElementById("photo" + i).src = (content[i].articles[0].urlToImage)
            document.getElementById("content" + i).innerHTML = (content[i].articles[0].description)
            document.getElementById("photo-link" + i).href = (content[i].articles[0].url)
            if(content[i].totalResults > 1) {
                document.getElementById("1_list" + i).innerHTML = (content[i].articles[1].title).link(content[i].articles[1].url)}
                else{document.getElementById("1_list" + i).style.visibility = "hidden";}

            if(content[i].totalResults >2){
                 document.getElementById("2_list" + i).innerHTML = (content[i].articles[2].title).link(content[i].articles[2].url)}
                            else{document.getElementById("2_list" + i).style.visibility = "hidden";}


            if(content[i].totalResults >3) {
                 document.getElementById("3_list" + i).innerHTML = (content[i].articles[3].title).link(content[i].articles[3].url)}
                            else{document.getElementById("3_list" + i).style.visibility = "hidden";}



        } else {
            var no_content_text = "no content available";
            document.getElementById("content" + i).innerHTML = (no_content_text)
               document.getElementById("headline" + i).innerHTML = "";
            document.getElementById("photo" + i).style.visibility = "hidden";

            document.getElementById("content" + i).style.textAlign = "center"
            document.getElementById("content" + i).style.color = "grey";
            document.getElementById("content" + i).style.borderBottom = "none";

            document.getElementById("content" + i).style.fontStyle = "italic";

            document.getElementById("1_list" + i).style.visibility = "hidden";
            document.getElementById("2_list" + i).style.visibility = "hidden";
            document.getElementById("3_list" + i).style.visibility = "hidden";



        }
    })


    if (scrollToAnchor != 0) {

            // document.location.hash = '#' + scrollToAnchor;
             $('html, body').animate({
        scrollTop: $(`#${scrollToAnchor}`).offset().top
            }, 1500);
        }

}


$(document).ready(function() {
    updateContent()

    $('#my-form').on('submit', function(event) {
            event.preventDefault();
        $.ajax({
            data: {
                query: $('#inlineforminput').val(),
                date: $('#datepicker-large').val()
            },
            type: 'POST',
            url: '/form_data'
        })
            .done(function(data){
                console.log(data)
                content = data.content
                date = data.date
                scrollToAnchor = data.scrollToAnchor
                updateContent()

            })
    });
});



 //


    //     var div = document.createElement("div")
    //     div.className = "carousel-cell"
    //     div.ID = "content"+i
    //     document.getElementById("carousel").appendChild(div)
    //
    //
    // //     var outlet = document.createElement("p")
    //     var outlet_text = outlets[i]);
    // //     outlet.append(outlet_text)

    //     var headline = document.createElement("h3")
    //     var photo = document.createElement("img")
    //     var content = document.createElement("p")
    //
    //     var headline_text = document.createTextNode((content[i].articles[0].title))
    //     photo.src = (content[i].articles[0].urlToImage)
    //     var content_text = document.createTextNode(content[i].articles[0].content)
    //
    //     headline.append(headline_text)
    //     content.append(content_text)





