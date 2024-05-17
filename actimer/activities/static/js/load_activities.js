function loadActivities() {
    $.ajax({
        method: "GET",
        url: "",
        data: {
            ajax_request: true,
        },

        success: function(response) {
            $('#activities-list').html(response);
        },

        error: function(response) {
            showModalWindow(
                'standartModal', 
                height='200px',
                heading='Error', 
                content='Activities loading error. Please, try again.', 
                accept_text='Close', 
                accept_action= `hideModalWindow('standartModal')`, 
            )
        },
    })
}