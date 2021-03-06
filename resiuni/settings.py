"""
Django settings for resiuni project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '81m6(o(q^nka=xkk7jif)s)p^s83!5a3n%h+!g^4j-v_w*r5ar'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),

)

ALLOWED_HOSTS = []

#####------this is a modificaton to public to facebook

#TEMPLATE_CONTEXT_PROCESSORS = (
#   'django.contrib.auth.context_processors.auth',
#   'django.core.context_processors.debug',
#   'django.core.context_processors.i18n',
#   'django.core.context_processors.media',
#   'django.core.context_processors.static',
#   'django.core.context_processors.tz',
#   'django.contrib.messages.context_processors.messages',
#   'social.apps.django_app.context_processors.backends',
#   'social.apps.django_app.context_processors.login_redirect',
#)

#AUTHENTICATION_BACKENDS = (
#   'social.backends.facebook.FacebookOAuth2',
#   'social.backends.google.GoogleOAuth2',
#   'social.backends.twitter.TwitterOAuth',
#   'django.contrib.auth.backends.ModelBackend',
#)

#LOGIN_REDIRECT_URL = '/'
#SOCIAL_AUTH_FACEBOOK_KEY = '????'
#SOCIAL_AUTH_FACEBOOK_SECRET = '???'

#--------------------------------------------------


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'residencias',
    'thirdauth',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'resiuni.urls'

WSGI_APPLICATION = 'resiuni.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#admin user = root, pass = root

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'resiuni',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),

)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

MEDIA_URL = '/media/'