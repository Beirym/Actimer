function sendNewUserDataByAjax(csrf_token, field, new_value) {
    href = window.location.href;
    $.ajax({
        method: 'POST',
        url: href + 'change_user_data/',
        data: {
            csrfmiddlewaretoken: csrf_token,
            field_to_change: field,
            new_value: new_value,
        },

        success: function(response) {
            window.location.reload();
        },

        error: function(response) {
            error_text = response.responseJSON['errors'][0]
            showModalWindow(
                'standartModal', 
                height='220px',
                heading='Error', 
                content=error_text, 
                accept_text='Close', 
                accept_action= `hideModalWindow('standartModal')`
            );
        }
    })
}


function changeUserData(csrf_token, field, new_value=null, placeholder=null) {
    if (new_value === null) {
        if (placeholder === null) {
            placeholder = "Specify new {0}".f(field)
        }

        showModalWindow(
            'standartModal', 
            height='220px',
            heading='Change {0}'.f(field), 
            content='<input id="new-{0}" placeholder="{1}">'.f(field, placeholder), 
            accept_text='Change', 
            accept_action=`changeUserData("{0}", "{1}", new_value=$('#new-{1}').val())`.f(csrf_token, field)
        );
    } else {
        sendNewUserDataByAjax(csrf_token, field, new_value);
    }
}
