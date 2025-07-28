# Django Settings Class

A type-safe, dataclass-based approach to Django settings configuration that provides better IDE support, validation, and maintainability.

## Installation

```bash
pip install django-settings
```

## Quick Start

### Basic Usage

```python
# settings.py
from django_settings import DjangoSettings

# Create settings instance
settings = DjangoSettings(
    debug=True,
    secret_key="your-secret-key-here",
    allowed_hosts=["localhost", "127.0.0.1"],
    databases={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
)

# Register settings globally
settings.register()
```

### Environment-Specific Configuration

```python
# settings/base.py
from django_settings import DjangoSettings

class BaseSettings(DjangoSettings):
    def __init__(self):
        super().__init__(
            debug=False,
            secret_key="base-secret-key",
            installed_apps=[
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'myapp',
            ],
            middleware=[
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ]
        )

# settings/development.py
from .base import BaseSettings

settings = BaseSettings()
settings.debug = True
settings.allowed_hosts = ["localhost", "127.0.0.1"]
settings.register()

# settings/production.py
from .base import BaseSettings
import os

settings = BaseSettings()
settings.debug = False
settings.secret_key = os.environ['SECRET_KEY']
settings.allowed_hosts = os.environ['ALLOWED_HOSTS'].split(',')
settings.databases = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}
settings.register()
```

## Features

- **Type Safety**: Full type hints for all Django settings
- **IDE Support**: Autocomplete and validation in your IDE
- **Default Values**: Sensible defaults for all Django settings
- **Validation**: Dataclass validation ensures correct types
- **Backwards Compatible**: Works with existing Django projects

## Configuration Examples

### Database Configuration

```python
settings = DjangoSettings(
    databases={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'myproject',
            'USER': 'myuser',
            'PASSWORD': 'mypassword',
            'HOST': 'localhost',
            'PORT': '5432',
        },
        'users': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'users_db',
            'USER': 'mysql_user',
            'PASSWORD': 'mysql_password',
            'HOST': 'mysql.example.com',
            'PORT': '3306',
        }
    }
)
```

### Email Configuration

```python
settings = DjangoSettings(
    email_backend='django.core.mail.backends.smtp.EmailBackend',
    email_host='smtp.gmail.com',
    email_port=587,
    email_use_tls=True,
    email_host_user='your-email@gmail.com',
    email_host_password='your-app-password',
    default_from_email='your-email@gmail.com'
)
```

### Cache Configuration

```python
settings = DjangoSettings(
    caches={
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
        },
        'sessions': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/2',
        }
    }
)
```

### Security Settings

```python
settings = DjangoSettings(
    debug=False,
    allowed_hosts=['yourdomain.com', 'www.yourdomain.com'],
    secure_ssl_redirect=True,
    secure_hsts_seconds=31536000,
    secure_hsts_include_subdomains=True,
    secure_hsts_preload=True,
    secure_content_type_nosniff=True,
    session_cookie_secure=True,
    csrf_cookie_secure=True,
    x_frame_options='DENY'
)
```

## API Reference

### DjangoSettings Class

The main class that contains all Django settings as typed attributes.

#### Key Methods

- `register()`: Registers settings as module-level variables
- `to_dict`: Property that returns settings as a dictionary with uppercase keys

#### Accessing Settings

```python
# Lowercase attribute access
print(settings.debug)  # True

# Uppercase Django-style access
print(settings.DEBUG)  # True

# Dictionary access
settings_dict = settings.to_dict
print(settings_dict['DEBUG'])  # True
```

## Migration from Traditional Settings

### Before (traditional settings.py)

```python
DEBUG = True
SECRET_KEY = 'your-secret-key'
ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ...
]
```

### After (with django-settings)

```python
from django_settings import DjangoSettings

settings = DjangoSettings(
    debug=True,
    secret_key='your-secret-key',
    allowed_hosts=['localhost'],
    databases={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
)

settings.register()
```

## Requirements

- Python 3.10+
- Django 3.2+

## License

MIT License