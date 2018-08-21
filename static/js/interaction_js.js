// The javascript for interaction handling

function func_example_select(){
    // When selected, look at example type and selection region
    var example_type = document.getElementById("example_type_select")

    // do something according to the value of example_type defined in drum_visualize.html
    // if example_type.value == ...

    // call python
    my_number = 0   // a dummy number
    callPython_here(my_number)
}


function callPython_here(my_number){
    console.log("[js -> python]", my_number)
    $.ajax({
        url: "receiver/lets_talk",
        type: "POST",
        data: JSON.stringify(my_number),
        dataType: 'json',
        contentType: 'application/json',
        success: function(result){
            console.log("python -> js", result)
        }

    })
}

