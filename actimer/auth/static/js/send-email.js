function sendEmailWithNewPassword(csrf_token) {
    action_button_stock_html = $('.action-button').html()
    $('.action-button').html(loadingSpinner(color="#2D2D2D"))

    $.ajax({
        type: "POST",
        url: "",
        data: {
            csrfmiddlewaretoken: csrf_token,
            email: $('#email').val()
        },

        success: function(response){
            $('.action-button').html(action_button_stock_html)
            showModalWindow(
                'standartModal', 
                height='230px',
                heading='An email has been sent', 
                content=`An email with a new password has been sent to the specified E-Mail address. 
                         After logging in, you can change it in your personal account.`, 
                accept_text='Close', 
                accept_action= `hideModalWindow('standartModal')`, 
            )
        },

        error: function(response){
            $('.action-button').html(action_button_stock_html)
            showModalWindow(
                'standartModal', 
                height='200px',
                heading='Error', 
                content=response.responseJSON['errors'][0]['error'], 
                accept_text='Close', 
                accept_action= `hideModalWindow('standartModal')`, 
            )
        }
    });
}