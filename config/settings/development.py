from .base import *  # noqa: F401,F403
from .base import _env_bool, _env_list


DEBUG = _env_bool('DEBUG', True)
ALLOWED_HOSTS = _env_list('ALLOWED_HOSTS', ['localhost', '127.0.0.1'])


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
