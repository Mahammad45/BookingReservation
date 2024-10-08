import os
import configparser
from pathlib import Path
from string import ascii_lowercase, digits

from .conf.config import *
from .conf.database import *


CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_FOLDER = os.path.normpath(os.path.join(BASE_DIR, 'secret'))
SECRET_FILE = os.path.normpath(os.path.join(BASE_DIR, 'secret/SECRET.key'))

try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
    

except IOError:
    try:
        from django.utils.crypto import get_random_string

        chars = ascii_lowercase + digits + '!@#$%^&*()-_=+'
        SECRET_KEY = get_random_string(50, chars)

        with open(SECRET_FILE, 'w') as f:
            f.write(SECRET_KEY)
    except IOError:
        raise Exception(f'Не удается открыть {SECRET_FILE}')


DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'rest_framework',
    # 'rest_framework.authtoken',

    'drf_yasg',

    'hotels.apps',
    'bookings.apps',
    'users.apps',
    'notifications.apps',
    'reviews.apps',
    'payments.apps',
    

] + DEFAULT_INSTALLED_APPS


MIDDLEWARE = [

] + DEFAULT_MIDDLEWARE


ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


LANGUAGE_CODE = CONFIG['Django']['LANGUAGE_CODE']

TIME_ZONE = CONFIG['Django']['TIME_ZONE']

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles/'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
