from pathlib import Path
from corsheaders.defaults import default_headers
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", 'django-insecure-temp')  # Лучше вынести в ENV
DEBUG = False

# ALLOWED_HOSTS = [
#     'justdonate-production.up.railway.app',
#     'localhost',
#     '127.0.0.1',
# ]
DEBUG = True
ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    "https://tezkor-donat-front.vercel.app",  # если фронт на Vercel
    "http://localhost:5173",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    "x-user-id",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',
    'transaction',

    'corsheaders',
    'django_celery_results'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <- для отдачи static на Railway
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bek.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'nLbVLCMWpFxeadITGEAKrKWUaUpPBGHF',
        'HOST': 'tramway.proxy.rlwy.net',
        'PORT': '55407',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', }
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

MOOGOLD_SECRET_KEY = "Eo4DjOYw28"
MOOGOLD_PARTNER = "2cf929d9c587473dc4ae9e2f38db635a"
TELEGRAM_BOT_TOKEN = "твой_токен"
TELEGRAM_ADMIN_ID = "8146970004"

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'

# 👇 Используй директории внутри проекта
YAML_OUTPUT_DIR = BASE_DIR / 'static' / 'config'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'  # всё хранится в /static
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
