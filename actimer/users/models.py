from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator


class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='E-Mail')
    password = models.CharField(
        max_length=100, 
        validators=[RegexValidator(regex=settings.REGEXES['password'])],
        verbose_name='Password'
    )
    timezone = models.CharField(blank=True, default='UTC')
    is_activated = models.BooleanField(default=False, verbose_name='Account activation status')
    registrationDate = models.DateTimeField(auto_now_add=True, verbose_name='Registration date')

    class Meta:
        db_table = 'users'
        ordering = ['-registrationDate']