from django import template

from ..timers import getTimerDuration

import datetime


register = template.Library()


@register.inclusion_tag('timers/inc/buttons.html')
def addButtonsHtml(timer_status):
    '''Creates a template for timer control buttons depending on its state.'''

    return {'timer_stats': timer_status}


@register.filter(name='timer_duration')
def timerDuration(timer):
    duration = getTimerDuration(timer)
    duration = duration - datetime.timedelta(microseconds=duration.microseconds)
    return duration