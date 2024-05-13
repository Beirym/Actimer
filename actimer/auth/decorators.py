from django.shortcuts import redirect
from django.http import HttpResponseForbidden

from .auth_check import is_auth


def is_authorized(func):
    '''Checks the web-client is access to the requested page.'''
    
    def wrapper(request, **kwargs):
        user = is_auth(request)

        if user is None:
            return redirect('login')
        return func(request, kwargs) if kwargs else func(request)

    return wrapper


def is_unauthorized(func):
    '''Checks the web-client is not authorized.'''

    def wrapper(request):
        user = is_auth(request)

        if user is not None:
            return redirect('timers')
        return func(request)
        
    return wrapper