// https://www.javascripttutorial.net/javascript-dom/javascript-checkbox/
function check(checked = true, list) {
    for (let i = 0; i < list.length; i++) {
        let str = "input[value=" + "\'" + list[i] + "\'" + "]";
        $(str).prop('checked', checked);
    }
}

function prefill(){

    $("#name_input_edit").val(product["name"])
    $("#company_input_edit").val(product["company"])
    $("#type_input_edit").val(product["type"])

    let cost_numeric = product["cost"].replace(/[^0-9]/g,'')
    let size_numeric = product["size"].replace(/[^0-9]/g,'')

    $("#cost_input_edit").val(cost_numeric)
    $("#size_input_edit").val(size_numeric)
    
    $("#image_input_edit").val(product["image"])
    $("#summary_input_edit").val(product["summary"])
    $("#container_input_edit").val(product["container"])
    $("#ingredients_input_edit").val(product["ingredients"])
    $("#directions_input_edit").val(product["directions"])

    let skin_list = product["skin"]
    let problem_list = product["problem"]

    check(true, skin_list)
    check(true, problem_list)

}

function submit_Rec(ingredients_input){
    $(".error").remove();
    $(".success").remove();

    // Add the newest record to the model
    let name_input = $.trim($("#name_input_edit").val())
    let company_input = $.trim($("#company_input_edit").val())
    let type_input = $.trim($("#type_input_edit").val())
    let size_input = $.trim($("#size_input_edit").val())
    let cost_input = $.trim($("#cost_input_edit").val())
    let image_input = $.trim($("#image_input_edit").val())
    let summary_input = $.trim($("#summary_input_edit").val())
    let container_input = $.trim($("#container_input_edit").val())
    let directions_input = $.trim($("#directions_input_edit").val())

    let skin_input = []
    let problem_input = []

    let checkboxes_skin = document.querySelectorAll('input[name="skin"]:checked')
    checkboxes_skin.forEach((checkbox) => {
        skin_input.push(checkbox.value) // MOST RECENT CHANGE
    });

    let checkboxes_problem = document.querySelectorAll('input[name="problem"]:checked')
    checkboxes_problem.forEach((checkbox) => {
        problem_input.push(checkbox.value) // MOST RECENT CHANGE
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
            $("#name_input_edit").focus()
            $('#name_input_edit').after('<span class="error">This field is required</span>')
        }
        else if(company_input.length == 0){
            //$(".error").remove();
            $("#company_input_edit").focus()
            $('#company_input_edit').after('<span class="error">This field is required</span>')
        }
        else if(type_input.length == 0){
            //$(".error").remove();
            $("#type_input_edit").focus()
            $('#type_input_edit').after('<span class="error">This field is required</span>');
        }
        else if(size_input.length == 0){
            //$(".error").remove();
            $("#size_input_edit").focus()
            $('#size_input_edit').after('<span class="error">This field is required</span>');
        }
        else if(cost_input.length == 0){
            //$(".error").remove();
            $("#cost_input_edit").focus()
            $('#cost_input_edit').after('<span class="error">This field is required</span>');
        }
        else if(image_input.length == 0){
            //$(".error").remove();
            $("#image_input_edit").focus()
            $('#image_input_edit').after('<span class="error">This field is required</span>');
        }
        else if(summary_input.length == 0){
            //$(".error").remove();
            $("#summary_input_edit").focus()
            $('#summary_input_edit').after('<span class="error">This field is required</span>');
        }
        else if(container_input.length == 0){
            //$(".error").remove();
            $("#container_input_edit").focus()
            $('#container_input_edit').after('<span class="error">This field is required</span>');
        }
        else if(ingredients_input.length == 0){
            //$(".error").remove();
            $("#ingredients_input_edit").focus()
            $('#ingredients_input_edit').after('<span class="error">Add at least one ingredient</span>');
        }
        else if(directions_input.length == 0){
            //$(".error").remove();
            $("#directions_input_edit").focus()
            $('#directions_input_edit').after('<span class="error">This field is required</span>');
        }
        else if(skin_input.length == 0){
            //$(".error").remove();
            $('#skin_input_edit').after('<span class="error">Select at least one skin type</span>');
        }
        else if(problem_input.length == 0){
            //$(".error").remove();
            $('#problem_input_edit').after('<span class="error">Select at least one skin problem</span>');
        }
    }
    else if(size_input <= 0){
        $("#size_input_edit").focus()
        $('#size_input_edit').after('<span class="error">Please enter a valid number greater than 0</span>')
    }
    else if(cost_input < 0){
        $("#cost_input_edit").focus()
        $('#cost_input_edit').after('<span class="error">Please enter a valid number greater than or equal to 0</span>')
    }
    // DO PROPER URL CHECK
    // DO CHECKS FOR CHECKBOX STUFF (SKIN TYPE AND PROBLEM TYPE)
    else{
        $(".error").remove();
        $(".success").remove();

        let edited_product = {
            "id": product["id"],
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
    
        console.log("Edited product: ", edited_product)
        save_product(edited_product)
    }
}

function after_save(current_id){
    $('#edit_product_heading').after("<div><button><a href='/view/" + current_id + "'>Click here to see it: </a></button></div>")
    $('#edit_product_heading').after("<div class='success'>New item successfully created</div>")
        
    $("#name_input_edit").focus()
}

function save_product(edited_product){

    $.ajax({
        type: "POST",
        url: "/edit_product",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(edited_product),
        success: function(result){
            let all_data = result["data"]
            let current_id = result["current_id"]
            after_save(current_id)
            data = all_data

            $("#name_input_edit").focus()
            console.log("After edit: ", data)
            
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){

    prefill()

    $("#name_input_edit").focus()

    let ingredients_input = [...product["ingredients"]]

    $("#add_ingredient_edit").click(function(){
        $(".success").remove();
        if(($.trim($("#ingredients_input_edit").val())).length > 0){
            ingredients_input.push($.trim($("#ingredients_input_edit").val()))
            $('#add_ingredient_edit').after("<span class='success'>Added ingredient: " + $("#ingredients_input_edit").val() + "</span>");
            $(".error").remove();
        }
        $("#ingredients_input_edit").val("")
    })

    $("#submit_edit").click(function(){
        submit_Rec(ingredients_input)
    })

    $("#discard").click(function(){
        if(confirm("Are you sure you want to discard?") == true){
            prefill()
        } 
        console.log("Product: ", product)
    })

})