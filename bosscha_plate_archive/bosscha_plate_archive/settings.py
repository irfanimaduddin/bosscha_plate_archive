import environ
import os

from .settings_base import *

# reading .env file - only in development
env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, 'PleasePutSecretInENV')
)
environ.Env.read_env()

# Paths inside the project
MEDIA_ROOT = os.path.join('media')
MEDIA_URL = "/media/"

# Secret, Debug and Host
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

# Database
use_sqlite = True
sqlite_db = env.db('SQLITE_URL', default='sqlite:////' + os.path.join(BASE_DIR, 'db.sqlite3'))

DATABASES = {
    'default': sqlite_db if use_sqlite else env.db() # read os.environ['DATABASE_URL']
}

TIME_INPUT_FORMAT = [
    '$I:%M:%S %p',
    '$I:%M %p',
    '$I %p',
    '%H:%M:%S',
    '%H:%M:%S.$f',
    '%H:%M',
]
    