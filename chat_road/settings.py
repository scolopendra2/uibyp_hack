import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(override=False)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'not_so_secret')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG_ENV = os.getenv('DJANGO_DEBUG', 'False').lower()

DEBUG = DEBUG_ENV in ('true', 'yes', 'y', 't', '1', '', 'none')

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(
    ',',
)

ALLOW_REVERSE_ENV = os.getenv('DJANGO_ALLOW_REVERSE', 'True').lower()

ALLOW_REVERSE = ALLOW_REVERSE_ENV in ('true', 'yes', 'y', 't', '1', '', 'none')

INSTALLED_APPS = [
    'homepage.apps.HomepageConfig',
    'about.apps.AboutConfig',
    'find_answer.apps.FindAnswerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS.append(
        'debug_toolbar',
    )
    MIDDLEWARE.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

INTERNAL_IPS = os.getenv('DJANGO_INTERNAL_IPS', '127.0.0.1,localhost').split(
    ',',
)

ROOT_URLCONF = 'chat_road.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'chat_road.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static_dev']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
