"""
Django settings for french_ping_calculator project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'ping.ulakanakulot.me',
]

USE_I18N = True

DATABASES = {}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'calculator',
    'crispy_forms',
    'crispy_forms_foundation'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'french_ping_calculator.urls'

WSGI_APPLICATION = 'french_ping_calculator.wsgi.application'


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

STATIC_ROOT = BASE_DIR + '/static/'

CRISPY_TEMPLATE_PACK = "foundation-5"

try:
    import local_settings
except ImportError:
    print """
    -------------------------------------------------------------------------
    You need to create a local_settings.py file which needs to contain at least
    database connection information.
    Copy local_settings_example.py to local_settings.py and edit it.
    -------------------------------------------------------------------------
    """
    import sys
    sys.exit(1)
else:
    import re
    for attr in dir(local_settings):
        # Remove stuff from lists that begin with "MINUS_".
        match = re.search('^MINUS_(\w+)', attr)
        if match:
            name = match.group(1)
            value = getattr(local_settings, attr)
            globals()[name] = tuple([x for x in globals()[name] if x not in value])
            continue

        # Append to lists any symbols that begin with "EXTRA_".
        match = re.search('^EXTRA_(\w+)', attr)
        if match:
            name = match.group(1)
            value = getattr(local_settings, attr)
            try:
                globals()[name] += value
            except KeyError:
                globals()[name] = value
            continue

        # Insert at the beginning to lists any symbols that begin with "INSERT_".
        match = re.search('^INSERT_(\w+)', attr)
        if match:
            name = match.group(1)
            value = getattr(local_settings, attr)
            try:
                globals()[name] = value + globals()[name]
            except KeyError:
                globals()[name] = value
            continue

        # Import any symbols that begin with A-Z.
        if re.search('^[A-Z]', attr):
            globals()[attr] = getattr(local_settings, attr)
