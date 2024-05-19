from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from .validators import *

from auth.decorators import is_authorized
from auth.security import encrypt
from .models import User


@is_authorized
def profile(request):
    user = User.objects.get(pk=request.session['user']['id'])
    context = {'user': user}
    return render(request, 'users/profile.html', context)


@is_authorized
def changeUserData(request):
    user = User.objects.get(pk=request.session['user']['id'])
    

    field_to_change = request.POST.get('field_to_change')
    new_field_value = request.POST.get('new_value')

    validation_errors = userDataValidation(field=field_to_change, value=new_field_value)
    if validation_errors:
        return JsonResponse({'errors': validation_errors}, status=400)

    match field_to_change:
        case 'email':
            user.email = new_field_value
            user.save()
        case 'password':
            user.password = encrypt(new_field_value)
            user.save()
        case 'timezone':
            current_utc_hour = timezone.now().hour
            delta = int(new_field_value) - current_utc_hour
            if delta > 0:
                user.timezone = f'UTC+{delta}'
            elif delta < 0:
                user.timezone = f'UTC-{abs(delta)}'
            else:
                user.timezone = 'UTC'
            user.save()


    return HttpResponse(status=204)