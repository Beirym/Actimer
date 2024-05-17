import os
from pathlib import Path
from .config import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'auth.apps.AuthConfig',
    'users.apps.UsersConfig',
    'timers.apps.TimersConfig',
    'stats.apps.StatsConfig',
    'history.apps.HistoryConfig',
    'activities.apps.ActivitiesConfig',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'actimer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'actimer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'Actimer',
       'USER': 'postgres',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'auth/static'),
    os.path.join(BASE_DIR, 'users/static'),
    os.path.join(BASE_DIR, 'timers/static'),
    os.path.join(BASE_DIR, 'stats/static'),
    os.path.join(BASE_DIR, 'history/static'),
    os.path.join(BASE_DIR, 'activities/static'),
]
if DEBUG is False:
    STATIC_ROOT = 'static'
else:
    STATICFILES_DIRS.append(os.path.join('static'))


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REGEXES = {
    'email': r'''([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|"([]!#-[^-~ \t]|(\\[\t -~]))+")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])''',
    'password': r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[^a-zA-Z\d\s]).{8,}$",
}


EMAIL_HOST = EMAIL['HOST']
EMAIL_HOST_USER = EMAIL['HOST_USER']
EMAIL_HOST_PASSWORD = EMAIL['HOST_PASSWORD']
EMAIL_PORT = EMAIL['PORT']
EMAIL_USE_SSL = True