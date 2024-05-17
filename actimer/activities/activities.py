from django.utils import timezone

from timers.models import Timer
from timers.timers import getTimerDuration
from stats import stats

import datetime


def getActivitiesStats(user, start_date: datetime.datetime, end_date: datetime.datetime):
    total_activities_seconds = 0
    activities = Timer.objects.values('activity').filter(
        user=user,
        startTime__range=[start_date, end_date],
    )
    activities_stats = {}

    for a in activities:
        a = a['activity']
        timers = Timer.objects.filter(
            user=user,
            activity=a,
            startTime__range=[start_date, end_date],
        )

        for t in timers:
            timer_duration = getTimerDuration(t).total_seconds()
            if a not in activities_stats.keys():
                activities_stats[a] = timer_duration
            else:
                activities_stats[a] += timer_duration
            total_activities_seconds += timer_duration

    return activities_stats, total_activities_seconds


def getUserActivities(user) -> list:
    start_date = user.registrationDate
    end_date = timezone.now()
    activities_stats = getActivitiesStats(user, start_date, end_date)[0]

    activities = []
    for activity, total_duration in activities_stats.items():
        timers_count = Timer.objects.filter(user=user, activity=activity).count()
        total_duration = stats.secondsIntoNextTimeUnit(total_duration)

        activity_data = {
            'title': activity,
            'timers_count': timers_count,
            'total_duration': total_duration,
        }
        activities.append(activity_data)

    return activities