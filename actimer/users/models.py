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
    registrationDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        ordering = ['-registrationDate']