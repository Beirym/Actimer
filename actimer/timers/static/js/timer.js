let timerInterval;
let seconds = 0, minutes = 0, hours = 0;
let timerIsPaused = false;


// Timer starting
function startTimer(csrf_token) {
    if ($('#activity').val().length === 0) { // Activity isn't filled in
        changeStyles('invalid_activity');
    } else {
        if (timerIsPaused === false) { // Create new timer
            activity = $('#activity').val();
            sendAjaxRequest(
                'start_timer/',
                data='{"csrfmiddlewaretoken": "{0}", "activity": "{1}"}'.f(csrf_token, activity),
                error_actions_func=function () {
                    resetTimer(csrf_token);
                    changeStyles('start_timer_error');
                }
            );
        } 
        else { // Start current timer
            timerIsPaused = false; 
            sendAjaxRequest(
                'pause_timer/', 
                data='{"csrfmiddlewaretoken": "{0}", "pause_action": "{1}"}'.f(csrf_token, 'stop'),
            );
        }

        changeStyles('start_timer');
        timerInterval = setInterval(updateTimer, 1000);
    }
}


// Timer pausing
function pauseTimer(csrf_token) {
    timerIsPaused = true;
    sendAjaxRequest('pause_timer/', data='{"csrfmiddlewaretoken": "{0}", "pause_action": "{1}"}'.f(csrf_token, 'add'));
    changeStyles('pause_timer');
    clearInterval(timerInterval);
}


// Timer reseting
function resetTimer(csrf_token, stop_timer=false) {
    if (stop_timer === true) {
        timerIsPaused = false;
        sendAjaxRequest('stop_timer/', data='{"csrfmiddlewaretoken": "{0}"}'.f(csrf_token));
    }

    changeStyles('reset_timer');
    clearInterval(timerInterval);
    seconds = 0;
    minutes = 0;
    hours = 0;
    document.getElementById("timer").value = formatTime(hours) + ":" + formatTime(minutes) + ":" + formatTime(seconds);
}


// Timer functionality
function updateTimer() {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
        if (minutes >= 60) {
            minutes = 0;
            hours++;
        }
    }
    document.getElementById("timer").value = formatTime(hours) + ":" + formatTime(minutes) + ":" + formatTime(seconds);
}

function formatTime(time) {
    return (time < 10) ? "0" + time : time;
}

// System functions
function sendAjaxRequest(url, data, error_actions_func) {
    href = window.location.href;

    $.ajax({
        method: "POST",
        url: href + url,
        data: JSON.parse(data),

        error: function(response) {
            error_text = response.responseJSON['error']
            showModalWithError(error_text);

            if (error_actions_func !== undefined) {
                error_actions_func();
            }
        }
    })
}

function showModalWithError(error_text) {
    showModalWindow(
        'standartModal', 
        height='230px',
        heading='Error', 
        content=error_text, 
        accept_text='Close', 
        accept_action= `hideModalWindow('standartModal')`, 
    );
}

function changeStyles(config) {
    switch (config) {
        case 'start_timer':
            $('#pause').css('display', 'block');
            $('#reset').css('display', 'block');
            $('#start').css('display', 'none');
            $('#activity').prop('disabled', true);
            break;
        
        case 'invalid_activity':
            $('#activity').removeClass('base-field');
            $('#activity').addClass('invalid-field');
            break;

        case 'start_timer_error':
            $('#start').removeClass('middle-button');
            $('#start').addClass('long-button');
            $('#start').css('display', 'block');
            $('#pause').css('display', 'none');
            $('#reset').css('display', 'none');
            $('#activity').prop('disabled', false);
            break;

        case 'pause_timer':
            $('#start').removeClass('long-button');
            $('#start').addClass('middle-button');
            $('#start').css('display', 'block');
            $('#pause').css('display', 'none');
            break;

        case 'reset_timer': 
            $('#start').removeClass('middle-button');
            $('#start').addClass('long-button');
            $('#start').css('display', 'block');
            $('#pause').css('display', 'none');
            $('#reset').css('display', 'none');
            $('#activity').prop('disabled', false);
            break;
    }
}