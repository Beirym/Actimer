from django.urls import path

from .views import *


urlpatterns = [
    path('', timer, name='timer'),
    path('start_timer/', startTimer, name='start_timer'),
    path('stop_timer/', stopTimer, name='stop_timer'),
    path('pause_timer/', pauseTimer, name='pause_timer'),
    path('clear_timers/', clearTimers, name='clear_timers'),
]