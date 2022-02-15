'use strict';
//Main__slide
var images = ['./../static/slide1.jpg', './../static/slide2.jpg', './../static/slide3.jpg']
var i = 0;

function slideShow() {
    document.getElementById("image").src = images[i];

    if (i < images.length - 1) {
        i++;
    } else {
        i = 0;
    }
    setTimeout("slideShow()", 3000);
}

window.onload = slideShow();

//dice

var elDiceOne = document.getElementById('dice1');
var elComeOut = document.getElementById('dice1');

elComeOut.onmouseover = function () {
    rollDice();
};

function rollDice() {

    var diceOne = Math.floor((Math.random() * 6) + 1);

    console.log(diceOne + ' ');

    for (var i = 1; i <= 6; i++) {
        elDiceOne.classList.remove('show-' + i);
        if (diceOne === i) {
            elDiceOne.classList.add('show-' + i);
        }else{
            console.log("Mouse out")
        }
    }

    setTimeout(rollDice(), 2000);
}



var elDiceTwo = document.getElementById('dice2');
var elComeOut2 = document.getElementById('dice2');

elComeOut2.onmouseover = function () {
    rollDice2();
};
