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
            var no_content_text = "no content available - try searching for a different subject or time period";
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
        // var node = document.createElement("BUTTON")
        // node.innerHTML = "show more...";
        // var button_text = document.createTextNode("load more")
        // node.appendChild(button_text);                              // Append the text to <li>

        // if($(`#show-more-button`+i).length == 0){
        // $("#list-group"+i).after(" <div class='show-more-button' id=`show-more-button${i}`> <button class='btn btn-primary'> show more... </button> </div>")
        // document.getElementById("list-group"+i).appendChild(node)
    })

        // })
    document.getElementById("date-today").innerHTML = date;


    if (scrollToAnchor != 0) {
            // document.location.hash = '#' + scrollToAnchor;
             $('html, body').animate({
        scrollTop: $(`#${scrollToAnchor}`).offset().top
            }, 1500);
        }

}


$(document).ready(function() {

    // load page for first time
    updateContent()

    // handle if user chooses a subject
    $('.subject-button').click(function(event){
        console.log(event.currentTarget.value)

           $.ajax({
            data: {
                query: event.currentTarget.value,
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
    })


    // handle if user enters text (and/or date)
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

    // handle show more button
    // #todo: fix this behaviour
    $('.show-more-button').on("click", function() {


        var node = document.createElement("DIV")
        node.id = "second-carousel"

        $('#main-carousel-row').after(node)

        var elem = document.querySelector('#second-carousel')

        var cell = document.createElement("DIV")
        cell.className = "carousel-cell"
        var cell_content = document.createElement("P")
        cell_content.innerHTML = "hello hello"
        cell.appendChild(cell_content)

             var cell2 = document.createElement("DIV")
        cell2.className = "carousel-cell"
        var cell_content2 = document.createElement("P")
        cell_content2.innerHTML = "hello hello"
        cell2.appendChild(cell_content2)

        $('#second-carousel').append(cell)
        $('#second-carousel').append(cell2)


        var flkty = new Flickity( elem, {
        cellAlign: 'left',
        contain: true
            });



        $('second-carousel').flickity('resize');

        flkty.reloadCells()
        var cellElements = flkty.getCellElements()
    })




    // handle the range slider:
    var slider = document.getElementById("myRange");
    var slider_color_range = ["#2171b5",
        "#6baed6",
        "#bdd7e7",
        "#eff3ff",
        "#fee5d9",
        "#fcae91",
        "#fb6a4a",
        "#cb181d"]
    slider.oninput = function() {
        var slider_value = this.value;
        slider.style.background = slider_color_range[slider_value]
         $('.main-carousel').flickity('select', slider_value)
        // if (slider_value ==0){
        //     slider.className = ""
        // }
        // else if(slider_value ==1){
        //     slider.className = "slidercolor1"
        // }
        //         else if(slider_value ==2){
        //     slider.className = "slidercolor2"
        // }
        //                 else if(slider_value ==3){
        //     slider.className = "slidercolor3"
        // }
        //                         else if(slider_value ==4){
        //     slider.className = "slidercolor4"
        // }
        //                                 else if(slider_value ==5){
        //     slider.className = "slidercolor5"
        // }
        //                                         else if(slider_value ==6){
        //     slider.className = "slidercolor6"
        // }
        // else{ slider.className = "slidercolor7"}



    }











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





