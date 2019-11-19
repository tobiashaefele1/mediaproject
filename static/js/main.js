/* main JS file */


//
//
//     }

// console.log(NYT)

console.log(content);
var outlets = ["MSNBC", "Huffington Post", "CNN", "Politico", "NYT", "Reuters", "USA Today", "FOX"];

content.forEach(function(d,i){

        document.getElementById("outlet"+i).innerHTML = (outlets[i]);
        document.getElementById("outlet"+i).className = "outlet"

    if(content[i].totalResults != 0) {

        document.getElementById("headline"+i).innerHTML = (content[i].articles[0].title)
        document.getElementById("photo"+i).src = (content[i].articles[0].urlToImage)
        document.getElementById("content"+i).innerHTML = (content[i].articles[0].content)
        document.getElementById("photo-link"+i).href = (content[i].articles[0].url)

    }
    else{
        var no_content_text = "no content available";
        document.getElementById("content"+i).innerHTML = (no_content_text)
        document.getElementById("content"+i).style.textAlign = "center"
                document.getElementById("content"+i).style.color = "grey"
                        document.getElementById("content"+i).style.fontStyle = "italic"


    }
})

if(scrollToAnchor != 0) {
       document.addEventListener("DOMContentLoaded", function () {
            document.location.hash = '#' + scrollToAnchor;
                })
    }


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





