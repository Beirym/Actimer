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