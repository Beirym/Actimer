from django.urls import path

from .views import *


urlpatterns = [
    path('', stats, name='stats'),
]