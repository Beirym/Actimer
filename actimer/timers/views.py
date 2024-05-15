from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.urls import reverse_lazy

from .models import *
from .timers import *

from auth.decorators import is_authorized
from users.models import User


@is_authorized
def timer(request):
    user = User.objects.get(pk=request.session['user']['id'])
    active_timers = Timer.objects.filter(user=user, endTime=None).count()
    
    if active_timers > 0:
        timer = getActiveTimer(request, user)
    else:
        timer = getTimerData(timer=None)

    context = {
        'active_timers': active_timers,
        'timer': timer,
    }
    return render(request, 'timers/timer.html', context)


@is_authorized
def startTimer(request):
    user = User.objects.get(pk=request.session['user']['id'])

    active_timers = Timer.objects.filter(user=user, endTime=None)
    if active_timers:
        return JsonResponse({'error': 'Timer already started'}, status=400)

    activity = request.POST.get('activity')
    timer = Timer.objects.create(user=user, activity=activity)

    deleteTimerDataFromSession(request)
    addTimerDataToSession(request, timer)
    return HttpResponse(status=204)


@is_authorized
def stopTimer(request):
    user = User.objects.get(pk=request.session['user']['id'])

    active_timers = Timer.objects.filter(user=user, endTime=None)
    if len(active_timers) == 0:
        return JsonResponse({'error': 'Active timers does not exist'}, status=400)
    else:
        timer = active_timers[0]
        timer.endTime = timezone.now()
        timer.save()

        deleteTimerDataFromSession(request)
        return HttpResponse(status=204)


@is_authorized
def pauseTimer(request):
    user = User.objects.get(pk=request.session['user']['id'])

    active_timers = Timer.objects.filter(user=user, endTime=None)
    if len(active_timers) == 0:
        return JsonResponse({'error': 'Active timers does not exist'}, status=400)
    else:
        timer = active_timers[0]
        pauses = timer.pauses

        pause_action = request.POST.get('pause_action')
        if pause_action == 'add':
            if pauses:
                keys_count = len(pauses.keys())
                new_key = str(keys_count+1)
                pauses[new_key] = {'start': timezone.now()}
            else:
                pauses = dict()
                pauses["1"] = {'start': timezone.now()}
        elif pause_action == 'stop':
            keys_count = len(pauses.keys())
            new_key = str(keys_count)
            pauses[new_key]['end'] = timezone.now()

        timer.pauses = pauses
        timer.save()
        return HttpResponse(status=204)


@is_authorized
def clearTimers(request):
    user = User.objects.get(pk=request.session['user']['id'])
    active_timers = Timer.objects.filter(user=user, endTime=None)

    if len(active_timers) == 0:
        return JsonResponse({'error': 'Active timers does not exist'}, status=400)
    else:
        for timer in active_timers:
            deleteTimerDataFromSession(request)
            timer.endTime = timezone.now()
            timer.save()

        return JsonResponse({'link': reverse_lazy('timer')}, status=301)