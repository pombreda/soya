"""
Django settings for soya project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vv1*=h1969h3i+p12sa6=9)f&$xc)%&d*@2eqossm&f4^0(z#c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

DEBUG_PROPAGATE_EXCEPTIONS = False

ALLOWED_HOSTS = []


# Application definition

try:
    from installed_apps_local import INSTALLED_APPS as INSTALLED_APPS_LOCAL
except ImportError:
    INSTALLED_APPS_LOCAL = ()


INSTALLED_APPS = (
    'saya_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'mptt',
    'bootstrap3',
    'resumable',
    'soya',
    'debug_toolbar',
    'django_pdb',
    'administration',
    'authentification',
    'permissions_groups',
    'regular_users_interface',
    'sections',
    'upload_video',
    'video',
) + INSTALLED_APPS_LOCAL

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_pdb.middleware.PdbMiddleware',
)

ROOT_URLCONF = 'soya.urls'

import hamlpy

hamlpy.nodes.TagNode.self_closing["recursetree"] = "endrecursetree"

TEMPLATE_LOADERS = (
    'hamlpy.template.loaders.HamlPyFilesystemLoader',
    'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

WSGI_APPLICATION = 'soya.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_REDIRECT_URL = '/'

FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'chuncks')

# not 100% good, should be in ResumableUploadView
if not os.path.exists(os.path.join(BASE_DIR, "chuncks")):
    os.makedirs(os.path.join(BASE_DIR, "chuncks"))

try:
    from settings_local import *
except ImportError:
    pass
