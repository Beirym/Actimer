from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

from users.models import User


class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    activity = models.CharField(max_length=50, blank=True, null=True, verbose_name='Activity')
    pauses = models.JSONField(null=True, blank=True, encoder=DjangoJSONEncoder, verbose_name='Pauses')
    startTime = models.DateTimeField(auto_now_add=True, verbose_name='Start time')
    endTime = models.DateTimeField(blank=True, null=True, verbose_name='End time')

    class Meta:
        db_table = 'timers'