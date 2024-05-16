from django.shortcuts import render

from .stats import *

from auth.decorators import is_authorized
from users.models import User


@is_authorized
def stats(request):
    user = User.objects.get(pk=request.session['user']['id'])
    context = {
        'stats_blocks': [
            getPeriodStatsBlock(user, 'day'),
            getPeriodStatsBlock(user, 'week'),
            getPeriodStatsBlock(user, 'month'),
        ]
    }
    
    return render(request, 'stats/stats.html', context)