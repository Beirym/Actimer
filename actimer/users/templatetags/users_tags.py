from django import template
from django.utils import timezone

register = template.Library()

import datetime


@register.filter(name='local_time')
def fromUTCtoLocalTime(utc_time: datetime.datetime, request) -> datetime.datetime:
    timezone = request.session['user']['timezone']
    if timezone != 'UTC':
        utc_delta_value = int(''.join(timezone.split('UTC')[1:]))
        local_time = utc_time + datetime.timedelta(hours=utc_delta_value)
    else:
        local_time = utc_time

    return local_time