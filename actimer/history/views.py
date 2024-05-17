from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse, Http404

from users.models import User
from timers.models import Timer

import math


def history(request):
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        if page.isnumeric():
            page = int(page)
        else:
            raise Http404

    user = User.objects.get(pk=request.session['user']['id'])
    timers_count = Timer.objects.filter(user=user).count()
    timers_list = Timer.objects.filter(user=user).order_by('-endTime')[(page-1)*10:page*10]
    pages_count = math.ceil(timers_count / 10)

    context = {
        'timers': {
            'count': timers_count,
            'list': timers_list,
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
        html = render_to_string('history/inc/timers-history-list.html', context)
        return JsonResponse(html, safe=False)
    else:
        return render(request, 'history/history.html', context)