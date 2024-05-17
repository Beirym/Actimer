from django.urls import *

from .views import *


urlpatterns = [
    path('', activities, name='activities'),
]