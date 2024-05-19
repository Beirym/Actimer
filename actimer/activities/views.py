from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse, Http404

from auth.decorators import is_authorized
from .activities import *

from users.models import User

import math


@is_authorized
def activities(request):
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        if page.isnumeric():
            page = int(page)
        else:
            raise Http404

    user = User.objects.get(pk=request.session['user']['id'])
    activities = getUserActivities(user)
    pages_count = math.ceil(len(activities) / 10)

    context = {
        'activities': {
            'count': len(activities),
            'list': activities[(page-1)*10:page*10],
        },
        'paginator': {
            'pages': {
                'count': pages_count,
                'range': range(1, pages_count+1)
            },
            'current_page': page,
        },
    }

    if request.GET.get('ajax_request'):
        html = render_to_string('activities/inc/activities-list.html', context)
        return JsonResponse(html, safe=False)
    else:
        return render(request, 'activities/activities.html', context)