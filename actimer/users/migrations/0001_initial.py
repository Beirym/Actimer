# Generated by Django 4.2.5 on 2024-05-12 23:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-Mail')),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^(?=.*[a-zA-Z])(?=.*\\d)(?=.*[^a-zA-Z\\d\\s]).{8,}$')], verbose_name='Password')),
                ('timezone', models.CharField(blank=True, default='UTC')),
                ('registrationDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['-registrationDate'],
            },
        ),
    ]
