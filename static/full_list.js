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
