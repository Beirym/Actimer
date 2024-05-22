from django.db import models

from users.models import User


class Session(models.Model):
    id = models.CharField(primary_key=True, verbose_name="ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    ip = models.GenericIPAddressField(verbose_name="IP-address")
    authDate = models.DateTimeField(auto_now_add=True, verbose_name="Auth date")

    class Meta:
        db_table = 'sessions'
        ordering = ['-authDate']


class UserActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    code = models.CharField(verbose_name='Confirmation code')
    sendingTime = models.DateTimeField(auto_now_add=True, verbose_name='Sending time')

    class Meta:
        db_table = 'email_confirmations'