from django.utils import timezone

from timers.models import Timer

import datetime


def addTimerDataToSession(request, timer: Timer) -> None:
    request.session['timer'] = {'id': timer.id}
    request.session.save()

def deleteTimerDataFromSession(request) -> None:
    if 'timer' in request.session.keys():
        del request.session['timer']
        request.session.save()
        

def getTimerDuration(timer: Timer) -> datetime.timedelta:
    if timer.endTime is None:
        end_time = timezone.now()
    else:
        end_time = timer.endTime
    start_time = timer.startTime

    timer_duration = end_time - start_time
    if timer.pauses:
        for p in timer.pauses.values():
            pause_start = datetime.datetime.strptime(p['start'], '%Y-%m-%dT%H:%M:%S.%f')
            try:
                pause_end = datetime.datetime.strptime(p['end'], '%Y-%m-%dT%H:%M:%S.%f')
                pause_duration = pause_end - pause_start
            except KeyError:
                pause_duration = end_time - pause_start
            timer_duration -= pause_duration
    return timer_duration


def tiemerIsPaused(timer: Timer) -> bool:
    if timer.endTime is None:
        if timer.pauses:
            for i in timer.pauses.values():
                if len(i) == 1:
                    return True
    return False


def getTimerCurrentTime(timer: Timer) -> str:
    timer_seconds = getTimerDuration(timer).total_seconds()
    hours = int(timer_seconds // 3600)
    minutes = int((timer_seconds % 3600) // 60)
    seconds = int(timer_seconds % 60)
    return f"{hours}:{minutes}:{seconds}"


def getTimerData(request) -> dict:
    timer_data = {
        'status': 'disabled',
        'activity': None,
        'current_time': '00:00:00'
    }
    if 'timer' in request.session.keys():
        timer_id = request.session['timer']['id']
        timer = Timer.objects.get(pk=timer_id)
        timer_data['status'] = 'active' if tiemerIsPaused(timer) is False else 'paused'
        timer_data['activity'] = timer.activity
        timer_data['current_time'] = getTimerCurrentTime(timer)
    return timer_data