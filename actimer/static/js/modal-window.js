function showModalWindow(windowID, height, heading, content, accept_text, accept_action) {
    if (height !== undefined) {
        $('#' + windowID + ' ' + '.modal-window').css('height', height);
    }
    if (heading !== undefined) {
        $('#' + windowID + ' ' + '.modal-heading h2').html(heading);
    }
    if (content !== undefined) {
        $('#' + windowID + ' ' + '.modal-content').css('display', 'inline-block');
        $('#' + windowID + ' ' + '.modal-content').html('<p>' + content + '</p>');
    }
    if (accept_text !== undefined && accept_action !== undefined) {
        $('#' + windowID + ' ' + '.modal-buttons').css('display', 'flex');
        $('#' + windowID + ' ' + '.modal-buttons .accept').html('<p>' + accept_text + '</p>');
        $('#' + windowID + ' ' + '.modal-buttons .accept').attr(
            'onclick', accept_action + '; hideModalWindow("standartModal");'
        );
    }

    $('#' + windowID).css('display', 'table')
}


function hideModalWindow(windowID) {
    $('#' + windowID).css('display', 'none')
}


$(document).mouseup(function (e) {
    if (e.target.classList[0] === 'inner'){
        windowID = $('.inner').parent().attr('id')
        $('#' + windowID).css('display', 'none')
    }
});