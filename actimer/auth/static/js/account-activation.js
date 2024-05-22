function stopConfirmationProcess(csrf_token) {
    $.ajax({
        method: 'POST',
        url: '',
        data: {
            csrfmiddlewaretoken: csrf_token,
        },

        success: function(response) {
            href = window.location.protocol + '//' +  window.location.host
            window.location.assign(href + '/auth/signup/');
        },
    })
}