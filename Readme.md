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
from django_settings import DjangoSettings, DjangoDatabases, DatabaseConfig

class DatabaseSettings(DjangoDatabases):
    default = DatabaseConfig(
        engine='django.db.backends.sqlite3',
        name= 'db.sqlite3'
    )

# Create settings instance
settings = DjangoSettings(
    debug=True,
    secret_key="your-secret-key-here",
    allowed_hosts=["localhost", "127.0.0.1"],
    databases=DatabaseSettings()
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
from django_settings import DatabaseConfig, DjangoDatabases
import os

class ProductionDatabases(DjangoDatabases):
    default = DatabaseConfig(
        engine='django.db.backends.postgresql',
        name=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )

settings = BaseSettings()
settings.debug = False
settings.secret_key = os.environ['SECRET_KEY']
settings.allowed_hosts = os.environ['ALLOWED_HOSTS'].split(',')
settings.databases = ProductionDatabases()
settings.register()
```

## Features

- **Type Safety**: Full type hints for all Django settings
- **IDE Support**: Autocomplete and validation in your IDE
- **Default Values**: Sensible defaults for all Django settings
- **Validation**: Dataclass validation ensures correct types
- **Backwards Compatible**: Works with existing Django projects
- **Custom settings**: Support custom/extra Django settings

## Configuration Examples

### Database Configuration

#### Using DatabaseConfig and DjangoDatabases

```python
from django_settings import DjangoSettings, DatabaseConfig, DjangoDatabases

# Define individual database configurations
class MyDatabases(DjangoDatabases):
    default = DatabaseConfig(
        engine='django.db.backends.postgresql',
        name='myproject',
        user='myuser',
        password='mypassword',
        host='localhost',
        port='5432'
    )
    
    users = DatabaseConfig(
        engine='django.db.backends.mysql',
        name='users_db',
        user='mysql_user',
        password='mysql_password',
        host='mysql.example.com',
        port='3306'
    )

settings = DjangoSettings(
    databases=MyDatabases()
)
```

#### Advanced Database Configuration

```python
# With additional options
class ProductionDatabases(DjangoDatabases):
    default = DatabaseConfig(
        engine='django.db.backends.postgresql',
        name='production_db',
        user='prod_user',
        password='secure_password',
        host='db.example.com',
        port='5432',
        options={
            'sslmode': 'require',
            'connect_timeout': 10,
        },
        conn_max_age=600,
        conn_health_checks=True,
        atomic_requests=True
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


### Extra Settings

```python
from django_settings import DjangoSettings, ExtraSettings

class CustomSettings(ExtraSettings):
    ipinfo_token = 'XXXXXXXXXX'


# Create settings instance
settings = DjangoSettings(
    debug=True,
    secret_key="your-secret-key-here",
    allowed_hosts=["localhost", "127.0.0.1"],
    ...,
    extra=CustomSettings()
)

# Register settings globally
settings.register()
```

## API Reference

### DjangoSettings Class

The main class that contains all Django settings as typed attributes.

#### Key Methods

- `register()`: Registers settings as module-level variables
- `to_dict`: Property that returns settings as a dictionary with uppercase keys

### DatabaseConfig Class

A dataclass for defining individual database configurations with type safety.

#### Attributes

- `engine`: Database backend engine
- `name`: Database name
- `user`: Database user
- `password`: Database password
- `host`: Database host
- `port`: Database port
- `options`: Additional database options
- `atomic_requests`: Enable atomic requests
- `conn_max_age`: Connection max age
- `conn_health_checks`: Enable connection health checks

### DjangoDatabases Class

A collection class for managing multiple database configurations.

#### Usage

```python
class MyDatabases(DjangoDatabases):
    default = DatabaseConfig(engine='django.db.backends.sqlite3')
    cache = DatabaseConfig(engine='django.db.backends.postgresql')
```

#### Accessing Settings

```python
# Lowercase attribute access
print(settings.debug)  # True

# Uppercase Django-style access
print(settings.DEBUG)  # True

# Dictionary access
settings_dict = settings.as_dict
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
from django_settings import DjangoSettings, DatabaseConfig, DjangoDatabases

class MyDatabases(DjangoDatabases):
    default = DatabaseConfig(
        engine='django.db.backends.sqlite3',
        name='db.sqlite3'
    )

settings = DjangoSettings(
    debug=True,
    secret_key='your-secret-key',
    allowed_hosts=['localhost'],
    databases=MyDatabases()
)

settings.register()
```

## Requirements

- Python 3.10+
- Django 3.2+

## License

MIT License