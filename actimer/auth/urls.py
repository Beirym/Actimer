from django.urls import path

from .views import *


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('confirm_email/', confirmEmail, name='confirm_email'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('forgot_password/', forgotPassword, name='forgot_password'),
]