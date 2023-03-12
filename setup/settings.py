"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path, os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

USE_S3 = str(os.getenv('USE_S3')) == 'TRUE'

if USE_S3:
    # Configurando para armazenar os Statics e Media no Bucket S3 da AWS
    # Utilizando essa documentação:
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

    # django < 4.2
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # STATICFILES_STORAGE mostra para o Django onde ele deve depositar os
    # arquivos estáticos quando usarmos o comando collectstatics
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

    SECRET_KEY = str(os.getenv('SECRET_KEY'))
    AWS_S3_ACCESS_KEY_ID = str(os.getenv('AWS_S3_ACCESS_KEY_ID'))
    AWS_S3_SECRET_ACCESS_KEY = str(os.getenv('AWS_S3_SECRET_ACCESS_KEY'))
    AWS_STORAGE_BUCKET_NAME = str(os.getenv('AWS_STORAGE_BUCKET_NAME'))
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    #AWS_DEFAULT_ACL = 'public-read'
    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATIC_ROOT = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    MEDIA_ROOT = '/media/'
else:
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    STATIC_URL = 'static/'
    STATICFILES_DIRS =  [
        os.path.join(BASE_DIR, 'setup/static'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.vercel.app',
    '.now.sh',
    '127.0.0.1',
    '.herokuapp.com',
    '.onrender.com',
    '0.0.0.0'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'galeria.apps.GaleriaConfig',
    'usuarios.apps.UsuariosConfig',
    'storages'
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

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

USE_POSTGRESQL = str(os.getenv('USE_POSTGRESQL')) == 'TRUE'

if USE_POSTGRESQL:
    # Database para hosts externos com Postgresql
    DATABASES = {
        'default': dj_database_url.config(
            default='postgres://matheus:yvX9sriq8TNYbNJUqXOJNoiAkDZ0YRBh@dpg-cfpdebo2i3mo4bq242jg-a/alura_space',
            conn_max_age=600
        )
    }
else:
    # Database para localhost
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurando as constantes das mensagens
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success',
}

# Configurações para Deploy
# Unless your site should be available over both SSL and non-SSL connections,
# you may want to either set this setting True or configure a load balancer
# or reverse-proxy server to redirect all connections to HTTPS.
SECURE_SSL_REDIRECT = False
# Using a secure-only session cookie makes it more difficult
# for network traffic sniffers to hijack user sessions.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True