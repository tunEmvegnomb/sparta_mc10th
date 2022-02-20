'use strict';
//Main__slide
// var images = ['./../static/slide1.jpg', './../static/slide2.jpg', './../static/slide3.jpg']
// var i = 0;
//
// function slideShow() {
//     document.getElementById("image").src = images[i];
//
//     if (i < images.length - 1) {
//         i++;
//     } else {
//         i = 0;
//     }
//     setTimeout("slideShow()", 3000);
// }

window.onload = showGames();

function showGames() {
    $.ajax({
        type: 'GET',
        url: '/rand',
        data: {},
        success: function (response) {
            let todaygames = response[1]
            console.log(todaygames)

            var images = todaygames
            var i = 0;

            document.getElementById("image").src = images[i];

            if (i < images.length - 1) {
                i++;
            } else {
                i = 0;
            }
            setTimeout("showGames()", 3000);
        }
    })
}









