from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail

from .models import *
from .decorators import *
from .validators import *
from .sessions import *
from .security import *

from users.models import User
from actimer.ip import getIP

import json
import secrets
import string


@is_unauthorized
def signup(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html')
    elif request.method == 'POST':
        auth_data = json.loads(request.POST.get('auth_data'))

        validation_errors = signupValidation(auth_data)
        if validation_errors:
            response = JsonResponse({'errors': validation_errors}, status=400)
            return response
        else:
            auth_data['password'] = encrypt(auth_data['password'])

            user = User.objects.create(**auth_data)
            createSession(request, user)

            return HttpResponse(status=204)



@is_unauthorized
def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    elif request.method == 'POST':
        auth_data = json.loads(request.POST.get('auth_data'))

        validation_errors = loginValidation(auth_data)
        if validation_errors:
            response = JsonResponse({'errors': validation_errors}, status=400)
            return response
        else:
            user = User.objects.get(email=auth_data['email'])
            createSession(request, user)

            return HttpResponse(status=204)


@is_authorized
def logout(request):
    user = User.objects.get(pk=request.session['user']['id'])
    Session.objects.get(pk=request.session['session_id']).delete()
    return HttpResponse(status=204)
    

@is_unauthorized
def forgotPassword(request):
    if request.method == 'GET':
        return render(request, 'auth/forgot_password.html')
    elif request.method == 'POST':
        email = request.POST.get('email')

        validation_errors = forgotPasswordValidation(email)
        if validation_errors:
            response = JsonResponse({'errors': validation_errors}, status=400)
            return response
        else:
            alphabet = string.ascii_letters + string.digits
            new_password = ''.join(secrets.choice(alphabet) for i in range(20)) 

            user = User.objects.get(email=email)
            user.password = encrypt(new_password)
            user.save()

            send_mail(
                "Your password has been updated!",
                f"The new passoword: {new_password}",
                "Actimer <AsureTeam@yandex.ru>",
                [email],
                fail_silently=False,
            )

            return HttpResponse(status=204)