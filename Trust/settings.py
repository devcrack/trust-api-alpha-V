"""
Django settings for Trust project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fufb92c$)q10^1iro##kqj$!zn*&+wt8q*52qqa^o9%(%h0oyb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "52.14.35.17"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Packages and Libraries
    'rest_framework',
    'knox',
    'djoser',
    'corsheaders',
    # Own Applications
    'User.apps.UserConfig',
    'PricesDiscount.apps.PricesdiscountConfig',
    'ServiceArea.apps.ServiceareaConfig',
    'Addresses.apps.AddressesConfig',
    'Gelocation.apps.GelocationConfig',
    'Clients.apps.ClientsConfig',
    'GasCompany.apps.GascompanyConfig',
    'TankerTruck.apps.TankertruckConfig',
    'Events.apps.EventsConfig',
    'OrderServices.apps.OrderservicesConfig',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Agregando Django CORS Midleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Trust.urls'

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

WSGI_APPLICATION = 'Trust.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


###########################################
#####   Configuracion NO DEFAULT  ########
###########################################
AUTH_USER_MODEL = 'User.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),

}

REST_KNOX = {
    'AUTH_TOKEN_CHARACTER_LENGTH': 32,
    'TOKEN_TTL': None  # Aqui indicamos que tenga una caducidad.
}

# Configuracion Django CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = ('http://localhost:8000',)
CORS_ORIGIN_REGEX_WHITELIST = ('http://localhost:8000',)



# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Temporal Config
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 





