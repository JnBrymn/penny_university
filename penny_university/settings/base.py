"""
Django settings for penny_university project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if SECRET_KEY is None:
    raise EnvironmentError('Secret key is not set!')

ALLOWED_HOSTS = ['*']  # TODO this is a hack - fix once we have domain name set up

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'background_task',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django_filters',
    'bot',
    'api',
    'home',
    'pennychat',
    'users',
    'penny_university',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'penny_university.middleware.debug_passthrough.DebugPassthrough',
    'penny_university.middleware.integration_test_logging.IntegrationTestLogging',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'penny_university.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'penny_university.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {}
# in .github/workflows/unit_testing.yml we define a DATABASE_URL corresponding to the test postgres
# in heroku the production DATABASE_URL is defined (see `heroku config`)
# if neither is defined then we presume we're in dev and just use sqlite
DATABASES['default'] = dj_database_url.config(default='sqlite:///db.sqlite3', conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "penny_university/static")
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            # NOTE this is probably stupid, but I'm redirecting every log message to the console including errors
            'stream': sys.stdout,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}


AUTH_USER_MODEL = 'users.User'


############################################
# Put basic django stove above
# Put stuff more specific to our app below
############################################

# Slack
SLACK_API_KEY = os.environ.get('SLACK_API_KEY')
if SLACK_API_KEY is None:
    print('WARNING: SLACK_API_KEY is None')
PENNY_ADMIN_USERS = ['@JB', '@nick.chouard']

SLACK_TEAM_ID = 'T41DZFW4T'

SLACK_INVITE_LINK = os.environ.get('SLACK_INVITE_LINK')
if SLACK_INVITE_LINK is None:
    print('WARNING: SLACK_INVITE_LINK is None')

SLACK_DEV_CHANNEL = '#penny-labs'

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


# Background Tasks
REMINDER_BEFORE_PENNY_CHAT_MINUTES = 75  # to make sure we remind them MORE than an hour in advance
