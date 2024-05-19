from django.urls import path

from .views import *


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/change_user_data/', changeUserData, name='change_user_data'),
]