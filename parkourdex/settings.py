"""
Django settings for parkourdex project.

"""
from confy import env, database, cache
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )


# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

SECRET_KEY = env( 'SECRET_KEY' )
DEBUG = env( 'DEBUG' )

if not DEBUG:
    ALLOWED_HOSTS = env( 'ALLOWED_HOSTS', '' ).split( ',' )
else:
    ALLOWED_HOSTS = ['*']

DEFAULT_FROM_EMAIL = env( 'DEFAULT_FROM_EMAIL' )

# Application definition

INSTALLED_APPS = [
    'parkourdex',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'locations',
    'frontend',
    'corsheaders',    
    'simple_history',
    'rest_framework',
    'rest_framework_gis',
    'django_extensions',
    'django_registration',
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
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'parkourdex.urls'

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

WSGI_APPLICATION = 'parkourdex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': database.config()
}
CACHES = {'default': cache.config()}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = ('parkourdex.auth.Backend',)

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
   'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'parkourdex': {
            'handlers': ['console'],
            'level': 'INFO'
        },
    }
}


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-au'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_WHITELIST = []
if '*' not in ALLOWED_HOSTS:
    CORS_ORIGIN_WHITELIST = [host for host in ALLOWED_HOSTS]  

if DEBUG:
    CORS_ORIGIN_WHITELIST += [
        'http://localhost:8000',
        'http://localhost:8080',
        'http://127.0.0.1:8000',
        'http://127.0.0.1:8080',
    ]
CORS_ALLOW_CREDENTIALS = True

# django_registration expiry
ACCOUNT_ACTIVATION_DAYS = 7

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join( BASE_DIR, 'staticroot' )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}
