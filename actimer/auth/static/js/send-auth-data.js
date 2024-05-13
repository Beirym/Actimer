function sendAuthData(auth_type, csrf_token){
    action_button_stock_html = $(".action-button").html();
    $('.messages').empty();
    $(".action-button").html(loadingSpinner(color="#2D2D2D"));

    auth_data = {
        'email': $('#email').val(),
        'password': $('#password').val(),
    }

    validation_errors = authDataValidation(auth_type, auth_data)
    if (validation_errors.length > 0) {
        $(".action-button").html(action_button_stock_html);
        compileValidationErrorMessages(validation_errors);
        
    } else {
        $.ajax({
            type: "POST",
            url: "",
            data: {
                csrfmiddlewaretoken: csrf_token,
                auth_data: JSON.stringify(auth_data),
            },
    
            success: function(response){
                location.reload()
            },
    
            error: function(response){
                $(".action-button").html(action_button_stock_html);
                errors = response.responseJSON['errors'];
                if (errors.length > 0) {
                    compileValidationErrorMessages(errors);
                } else {

                }
            }
        });
    }
    
    return false;
}


function authDataValidation(auth_type, auth_data) {
    errors = []

    for (const [field, value] of Object.entries(auth_data)) {
        if (value === undefined || value.length === 0) {
            errors.push({'field': field, 'error': 'Fill in this field'});
            continue
        }
        
        if (field == 'name') {
            if (value.length < 2) {
                errors.push({'field': field, 'error': 'The name is too short'});
                continue
            }
            else if (/^[A-Za-zА-Яа-я\s]+$/.test(value) == false) {
                errors.push({'field': field, 'error': 'The name should consist only of letters'});
                continue
            }
        }

        else if (field == 'email') {
            if (email_regex.test(value) == false) {
                errors.push({'field': field, 'error': 'Incorrect E-Mail'});
                continue
            }
        }

        else if (field == 'password') {
            if (value.length < 8) {
                errors.push({'field': field, 'error': 'The password is too short'});
                continue
            }
        }
    }

    return errors;
}


function compileValidationErrorMessages(validation_errors) {
    validation_errors.forEach(row => {
        $('#' + row['field']).addClass('invalid-field');
        onfocus_actions = []

        current_value = $('#' + row['field']).val();
        onfocus_actions.push("$(this).val('" + current_value + "')");;
        $('#' + row['field']).val(null);

        current_placeholder = $('#' + row['field']).attr('placeholder');
        onfocus_actions.push("$(this).attr('placeholder', '" + current_placeholder + "')");
        $('#' + row['field']).attr('placeholder', row['error']);
        
        $('#' + row['field']).attr('onfocus', onfocus_actions.join('; '));
    }); 
}