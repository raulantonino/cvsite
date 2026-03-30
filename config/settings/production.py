import os

from .base import *  # noqa: F401,F403
from .base import _env_list

try:
    import dj_database_url
except ImportError:
    dj_database_url = None


DEBUG = False
render_external_hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME', '').strip()

allowed_hosts = _env_list('ALLOWED_HOSTS', [])
if render_external_hostname and render_external_hostname not in allowed_hosts:
    allowed_hosts.append(render_external_hostname)
ALLOWED_HOSTS = allowed_hosts

csrf_trusted_origins = _env_list('CSRF_TRUSTED_ORIGINS', [])
if render_external_hostname:
    render_origin = f'https://{render_external_hostname}'
    if render_origin not in csrf_trusted_origins:
        csrf_trusted_origins.append(render_origin)
CSRF_TRUSTED_ORIGINS = csrf_trusted_origins

postgres_env_vars = ('DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST')
postgres_configured = all(os.environ.get(name) for name in postgres_env_vars)
database_url = os.environ.get('DATABASE_URL', '').strip()

if database_url and dj_database_url is not None:
    DATABASES = {
        'default': dj_database_url.parse(
            database_url,
            conn_max_age=600,
            ssl_require=True,
        )
    }
elif postgres_configured:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': os.environ.get('DB_PORT', '5432'),
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'sslmode': os.environ.get('DB_SSLMODE', 'require'),
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / os.environ.get('SQLITE_NAME', 'db.sqlite3'),
        }
    }




SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
