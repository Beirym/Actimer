from django.urls import *

from .views import *


urlpatterns = [
    path('', history, name='history'),
]