// $(".calculator input").on("input change", function (event) {
//     var parameterName = $(this).attr("id").split("calc-")[1];
//     var min = $(this).val()
//
//     switch (parameterName) {
//         case "playtime":
//             var kg = $(this).val();
//             $("#calc-playtime_value").html("Playtime: " + min + " min");
//             break;
//         case "people":
//             $("#calc-people_value").html("People: " + 명 + " 명");
//             break;
//         case "age":
//             $("#calc-age_value").html("Age: " + $(this).val());
//             break;
//     }
//
//     var playtime = parseInt($("#calc-playtime").val(), 10);
//     var people = parseInt($("#calc-people").val(), 10);
//     var age = parseInt($("#calc-age").val(), 10);
//
// });
// 모달창 on/off 함수
function handleModal() {
    let status = $("#modal").css("display");
    if (status === "none") {
        $("#modal").css("display", "flex");
    } else {
        $("#modal").hide();
    }
}


// For Filters
document.addEventListener("DOMContentLoaded", function () {

// For Applying Filters
    $('#inner-box').collapse(false);
    $('#inner-box2').collapse(false);

// Showing tooltip for AVAILABLE COLORS
    $(function () {
        $('[data-tooltip="tooltip"]').tooltip()
    })

// For Range Sliders
    const inputLeft = document.getElementById("input-left");
    const inputRight = document.getElementById("input-right");

    const thumbLeft = document.querySelector(".slider > .thumb.left");
    const thumbRight = document.querySelector(".slider > .thumb.right");
    const range = document.querySelector(".slider > .range");

    const amountLeft = document.getElementById('amount-left');
    const amountRight = document.getElementById('amount-right');

    function setLeftValue() {
        const _this = inputLeft,
            min = parseInt(_this.min),
            max = parseInt(_this.max);

        _this.value = Math.min(parseInt(_this.value), parseInt(inputRight.value) - 1);

        const percent = ((_this.value - min) / (max - min)) * 100;

        thumbLeft.style.left = percent + "%";
        range.style.left = percent + "%";
        amountLeft.innerText = parseInt(percent * 100);
    }

    setLeftValue();

    function setRightValue() {
        const _this = inputRight,
            min = parseInt(_this.min),
            max = parseInt(_this.max);

        _this.value = Math.max(parseInt(_this.value), parseInt(inputLeft.value) + 1);

        const percent = ((_this.value - min) / (max - min)) * 100;

        amountRight.innerText = parseInt(percent * 100);
        thumbRight.style.right = (100 - percent) + "%";
        range.style.right = (100 - percent) + "%";
    }

    setRightValue();

    inputLeft.addEventListener("input", setLeftValue);
    inputRight.addEventListener("input", setRightValue);

    inputLeft.addEventListener("mouseover", function () {
        thumbLeft.classList.add("hover");
    });
    inputLeft.addEventListener("mouseout", function () {
        thumbLeft.classList.remove("hover");
    });
    inputLeft.addEventListener("mousedown", function () {
        thumbLeft.classList.add("active");
    });
    inputLeft.addEventListener("mouseup", function () {
        thumbLeft.classList.remove("active");
    });

    inputRight.addEventListener("mouseover", function () {
        thumbRight.classList.add("hover");
    });
    inputRight.addEventListener("mouseout", function () {
        thumbRight.classList.remove("hover");
    });
    inputRight.addEventListener("mousedown", function () {
        thumbRight.classList.add("active");
    });
    inputRight.addEventListener("mouseup", function () {
        thumbRight.classList.remove("active");
    });
});

//태그
$('.md-select').on('click', function () {
    $(this).toggleClass('active')
})

$('.md-select ul li').on('click', function () {
    var v = $(this).text();
    $('.md-select ul li').not($(this)).removeClass('active');
    $(this).addClass('active');
    $('.md-select label button').text(v)
})


//range
window.onload = function(){
    slideOne();
    slideTwo();
}

let sliderOne = document.getElementById("slider-1");
let sliderTwo = document.getElementById("slider-2");
let displayValOne = document.getElementById("range1");
let displayValTwo = document.getElementById("range2");
let minGap = 0;
let sliderTrack = document.querySelector(".slider-track");
let sliderMaxValue = document.getElementById("slider-1").max;

function slideOne(){
    if(parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap){
        sliderOne.value = parseInt(sliderTwo.value) - minGap;
    }
    displayValOne.textContent = sliderOne.value;
    fillColor();
}
function slideTwo(){
    if(parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap){
        sliderTwo.value = parseInt(sliderOne.value) + minGap;
    }
    displayValTwo.textContent = sliderTwo.value;
    fillColor();
}
function fillColor(){
    percent1 = (sliderOne.value / sliderMaxValue) * 100;
    percent2 = (sliderTwo.value / sliderMaxValue) * 100;
    sliderTrack.style.background = `linear-gradient(to right, #dadae5 ${percent1}% , #11698e ${percent1}% , #11698e ${percent2}%, #dadae5 ${percent2}%)`;
}
