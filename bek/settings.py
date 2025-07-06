from pathlib import Path
from corsheaders.defaults import default_headers

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-x*#e%6z(b&9w$2*2yq(koh@lj8qxpn)k_gl^bskbmi+=c6!!y!'

DEBUG = False
ALLOWED_HOSTS = [
    'tezkor.kodi.uz', 'localhost', '127.0.0.1',
    # "balanced-pipefish-settling.ngrok-free.app" # fake
]


CORS_ALLOWED_ORIGINS = [
    "https://tezkor-donat-front.vercel.app",
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', }
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

MOOGOLD_SECRET_KEY = "Eo4DjOYw28"
MOOGOLD_PARTNER = "2cf929d9c587473dc4ae9e2f38db635a"

TELEGRAM_BOT_TOKEN = "8190740090:AAEDSCuLIRCFZbPAaEZwP0JztjkG7V9M4eA"
TELEGRAM_ADMIN_ID = "8146970004"

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'



# YAML_OUTPUT_DIR = BASE_DIR / 'cdn/config/'

# STATIC_URL = '/cdn/'
# STATICFILES_DIRS = [
#     BASE_DIR / 'cdn',
# ]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True

YAML_OUTPUT_DIR = '/var/www/tezkor-donat/static/config/'
STATIC_URL = '/cdn/'
STATIC_ROOT = '/var/www/tezkor-donat/static/'
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
