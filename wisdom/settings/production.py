# settings/production.py
"""
If you use heroku set this constant in your configuration
DJANGO_SETTINGS_MODULE=wisdom.settings.production
"""

import dj_database_url
from .base import *  # noqa: F403
from os import environ


# Function to get environment variables value if they exist.
def env(e, d):
    if e in environ:
        return environ[e]
    else:
        return d


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', '')

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# Update database configuration with $DATABASE_URL.

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)  # noqa: F405

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Apps
PRODUCTION_APPS = [
    'storages',
]

INSTALLED_APPS += PRODUCTION_APPS  # noqa: F405

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# AWS
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', '')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', '')
AWS_QUERYSTRING_AUTH = False

# MEDIA
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://wisdombox.s3.amazonaws.com/media/'
DEFAULT_FILE_STORAGE = 'utils.custom_storages.MediaStorage'
