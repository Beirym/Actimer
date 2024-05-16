from timers.models import Timer
from django.utils import timezone

from timers.timers import getTimerDuration

import datetime
import calendar


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


def periodToDates(period: str) -> tuple[datetime.datetime]:
    periods_days = {
        'day': 1,
        'week': 7,
        'month': 30,
    }
    end_date = timezone.now()
    start_date = end_date - datetime.timedelta(days=periods_days[period])
    return start_date, end_date, periods_days[period]


def secondsIntoNextTimeUnit(seconds: int) -> str:
    hours = seconds / 3600
    minutes = (seconds % 3600) // 60
    if int(hours) > 0:
        new_time = int(hours)
        unit = 'h'
    elif int(minutes) > 0:
        new_time = int(minutes)
        unit = 'min'
    else:
        new_time = int(seconds)
        unit = 'sec'

    return f"{new_time} {unit}"


def calculateImprovementPercent(user, period: str, current_activities_seconds: int) -> int:
    start_date, end_date, period_days = periodToDates(period)
    last_start_date = start_date - datetime.timedelta(days=period_days)
    last_end_date = end_date - datetime.timedelta(days=period_days)

    last_activities_stats, last_activities_seconds = getActivitiesStats(user, last_start_date, last_end_date)

    try:
        improvement_percent = int((current_activities_seconds / last_activities_seconds) * 100 - 100)
    except ZeroDivisionError:
        improvement_percent = 0
    return improvement_percent


def getPeriodStatsBlock(user, period: str) -> dict:
    start_date, end_date, period_days = periodToDates(period)

    activities_stats, activities_seconds = getActivitiesStats(user, start_date, end_date)
    activities = []
    if activities_seconds > 0:
        activities.append({'title': 'Total', 'total_time': secondsIntoNextTimeUnit(activities_seconds)})
    for activity, duration_seconds in activities_stats.items():
        if int(duration_seconds) > 0:
            activities.append({'title': activity, 'total_time': secondsIntoNextTimeUnit(duration_seconds)})

    improvement_percent = calculateImprovementPercent(
        user,
        period=period,
        current_activities_seconds=activities_seconds,
    )

    stats_block = {
        'period': {
            'title': period,
            'start_date': start_date,
            'end_date': end_date,
        },
        'improvement_percent': improvement_percent,
        'activities': activities,
    }

    return stats_block