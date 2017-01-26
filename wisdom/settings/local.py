# settings/local.py
"""
If you use virtualenvwrapper add this line to your postactivate script
export DJANGO_SETTINGS_MODULE=wisdom.settings.local
"""

from .base import *  # noqa: F403

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_cybf+c!g@4g=^t(01ag_(99^m0nq8pev9nqb_zvz=ju*dc8$i'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}
