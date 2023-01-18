import { fade, fly } from 'svelte/transition'

function displayTopProducts(data){
    //empty old data
    $("#top_products").empty()
    console.log("in displayProducts")

    //insert all new data
    $.each([data["1"],data["2"],data["3"]], function(i, datum){

        let new_name= $("<div class='col-md-4' data-id='"+datum["id"]+"'>" +  
            "<a class = links_home href=/view/" + datum["id"] + ">" + datum["name"]+" by "+datum["company"] + 
            "<img class = 'product_img home_product_img' src=" + datum["image"] + " alt = " + "'Image of " + datum["name"] + " by " + datum["company"]  + "'>" +
            "</div>")
        
        let new_img = $("<div <img class='list' src=" + datum["image"] + ">" + "</div>")
            
        $("#top_products").append(new_name)

    });
}

function submit_Rec(ingredients_input){
    $(".error").remove();
    $(".success").remove();

    // Add the newest record to the model
    let name_input = $.trim($("#name_input").val())
    let company_input = $.trim($("#company_input").val())
    let type_input = $.trim($("#type_input").val())
    let size_input = $.trim($("#size_input").val())
    let cost_input = $.trim($("#cost_input").val())
    let image_input = $.trim($("#image_input").val())
    let summary_input = $.trim($("#summary_input").val())
    let container_input = $.trim($("#container_input").val())
    let directions_input = $.trim($("#directions_input").val())

    //let ingredients_input = []
    let skin_input = []
    let problem_input = []

    let checkboxes_skin = document.querySelectorAll('input[name="skin"]:checked')
    checkboxes_skin.forEach((checkbox) => {
        skin_input.push(checkbox.value)
    });

    let checkboxes_problem = document.querySelectorAll('input[name="problem"]:checked')
    checkboxes_problem.forEach((checkbox) => {
        problem_input.push(checkbox.value)
    });

    // Error checking

    if(name_input.length == 0 || company_input.length == 0 || type_input.length == 0 || 
        size_input.length == 0 || cost_input.length == 0 || image_input.length == 0 || summary_input.length == 0 || 
        container_input.length == 0 || ingredients_input.length == 0 || directions_input.length == 0 || 
        skin_input.length == 0 || problem_input.length == 0){
        $(".error").remove();
        $(".success").remove();
        if(name_input.length == 0){
            //$(".error").remove();
            $("#name_input").focus()
            $('#name_input').after('<span class="error">This field is required</span>')
        }
        else if(company_input.length == 0){
            //$(".error").remove();
            $("#company_input").focus()
            $('#company_input').after('<span class="error">This field is required</span>')
        }
        else if(type_input.length == 0){
            //$(".error").remove();
            $("#type_input").focus()
            $('#type_input').after('<span class="error">This field is required</span>');
        }
        else if(size_input.length == 0){
            //$(".error").remove();
            $("#size_input").focus()
            $('#size_input').after('<span class="error">This field is required</span>');
        }
        else if(cost_input.length == 0){
            //$(".error").remove();
            $("#cost_input").focus()
            $('#cost_input').after('<span class="error">This field is required</span>');
        }
        else if(image_input.length == 0){
            //$(".error").remove();
            $("#image_input").focus()
            $('#image_input').after('<span class="error">This field is required</span>');
        }
        else if(summary_input.length == 0){
            //$(".error").remove();
            $("#summary_input").focus()
            $('#summary_input').after('<span class="error">This field is required</span>');
        }
        else if(container_input.length == 0){
            //$(".error").remove();
            $("#container_input").focus()
            $('#container_input').after('<span class="error">This field is required</span>');
        }
        else if(ingredients_input.length == 0){
            //$(".error").remove();
            $("#ingredients_input").focus()
            $('#ingredients_input').after('<span class="error">Add at least one ingredient</span>');
        }
        else if(directions_input.length == 0){
            //$(".error").remove();
            $("#directions_input").focus()
            $('#directions_input').after('<span class="error">This field is required</span>');
        }
        else if(skin_input.length == 0){
            console.log("skin")
            //$(".error").remove();
            $('#skin_input').after('<span class="error">Select at least one skin type</span>');
        }
        else if(problem_input.length == 0){
            console.log("problem")
            //$(".error").remove();
            $('#problem_input').after('<span class="error">Select at least one skin problem</span>');
        }
    }
    else if(size_input <= 0){
        $("#size_input").focus()
        $('#size_input').after('<span class="error">Please enter a valid number greater than 0</span>')
    }
    else if(cost_input < 0){
        $("#cost_input").focus()
        $('#cost_input').after('<span class="error">Please enter a valid number greater than or equal to 0</span>')
    }
    // DO PROPER URL CHECK
    // DO CHECKS FOR CHECKBOX STUFF (SKIN TYPE AND PROBLEM TYPE)
    else{
        $(".error").remove();
        $(".success").remove();

        console.log(size_input)

        let newRec = {
            "name": name_input,
            "company": company_input,
            "image": image_input,
            "summary": summary_input,
            "cost": cost_input,
            "size": size_input,
            "container": container_input,
            "ingredients": ingredients_input,
            "directions": directions_input,
            "type": type_input,
            "problem": problem_input,
            "skin": skin_input
        }
    
        save_product(newRec)
        
    }
}

function after_save(current_id){
    $('#new_product_div').after("<div><button><a href='/view/" + current_id + "'>Click here to see it: </a></button></div>")
    $('#new_product_div').after("<div class='success'>New item successfully created</div>")
        
    $("#name_input").focus()
}

function save_product(new_product){

    $.ajax({
        type: "POST",
        url: "add_product",           
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_product),
        success: function(result){
            let all_data = result["data"]
            let current_id = result["current_id"]
            after_save(current_id)
            data = all_data

            $("#name_input").val("")
            $("#company_input").val("")
            $("#type_input").val("")
            $("#size_input").val("")
            $("#cost_input").val("")
            $("#image_input").val("")
            $("#summary_input").val("")
            $("#container_input").val("")
            $("#ingredients_input").val("")
            $("#directions_input").val("")
            check(false)

            $("#name_input").focus()
            console.log(data)
            
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

// https://www.javascripttutorial.net/javascript-dom/javascript-checkbox/
function check(checked = true) {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach((checkbox) => {
      checkbox.checked = checked;
    });
}

function highlight(query) {
    var inputText = query;
    var innerHTML = inputText.innerHTML;
    var index = innerHTML.indexOf(text);
    if (index >= 0) { 
        innerHTML = innerHTML.substring(0,index) + "<span class='highlight'>" + innerHTML.substring(index,index+text.length) + "</span>" + innerHTML.substring(index + text.length);
        inputText.innerHTML = innerHTML;
    }
}


$(document).ready(function(){

    // Display first 3 elements
    displayTopProducts(data)

    $("#product_to_search").focus()

    $("#name_input").focus()

    let ingredients_input = []

    $("#add_ingredient").click(function(){
        $(".success").remove();
        if(($.trim($("#ingredients_input").val())).length > 0){
            ingredients_input.push($.trim($("#ingredients_input").val()))
            $('#add_ingredient').after("<span class='success'>Added ingredient: " + $("#ingredients_input").val() + "</span>");
            $(".error").remove();
        }
        $("#ingredients_input").val("")
    })

    $("#submit_new_product").click(function(){
        submit_Rec(ingredients_input)
    })

})