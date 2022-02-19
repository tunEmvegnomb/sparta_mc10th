$(".calculator input").on("input change", function (event) {
    var parameterName = $(this).attr("id").split("calc-")[1];
    var min = $(this).val()

    switch (parameterName) {
        case "playtime":
            var kg = $(this).val();
            $("#calc-playtime_value").html("Playtime: " + min + " min");
            break;
        case "people":
            $("#calc-people_value").html("People: " + 명 + " 명");
            break;
        case "age":
            $("#calc-age_value").html("Age: " + $(this).val());
            break;
    }

    var playtime = parseInt($("#calc-playtime").val(), 10);
    var people = parseInt($("#calc-people").val(), 10);
    var age = parseInt($("#calc-age").val(), 10);

});