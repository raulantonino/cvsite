import os
from pathlib import Path


def _load_environment_selector():
    env_path = Path(__file__).resolve().parent.parent.parent / '.env'
    if not env_path.exists():
        return

    try:
        from dotenv import load_dotenv
    except ImportError:
        load_dotenv = None

    if load_dotenv is not None:
        load_dotenv(env_path, override=False)
        return

    for raw_line in env_path.read_text(encoding='utf-8').splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue

        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_environment_selector()

environment = os.environ.get('DJANGO_ENV', 'development').strip().lower()

if environment == 'production':
    from .production import *  # noqa: F401,F403
else:
    from .development import *  # noqa: F401,F403
