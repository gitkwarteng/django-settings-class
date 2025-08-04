import inspect
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple, Type

from django_settings.base import BaseDjangoSettings, BaseSettingsCollection, BaseExtraSettings


@dataclass
class DatabaseConfig(BaseDjangoSettings):
    """
    A complete settings class for representing a Django database configurations.
    This should be used in conjunction with `DjangoDatabases` class to define database settings.
    """
    engine: str = ''
    name: Any = ''
    user: str = ''
    password: str = ''
    host: str = ''
    port: str = ''
    options: Dict[str, Any] = field(default_factory=dict)
    atomic_requests: bool = False
    autocommit: bool = True
    conn_max_age: int = 0
    conn_health_checks: bool = False
    time_zone: str = None
    disable_server_side_cursors: bool = False
    test: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DjangoDatabases(BaseSettingsCollection):
    """
    A class for declaring Django Database settings.
    Each property maps to a key in the Django settings dictionary.

    Inherit this class in your settings file and override the default property
    to provide your default database settings.
    """
    default = DatabaseConfig(engine='django.db.backends.sqlite3', name='db.sqlite3')



@dataclass
class ExtraSettings(BaseExtraSettings):
    """
    A class for declaring extra settings that you want to add to your Django settings.

    Inherit this class and add as many settings as you like as properties.

    >>> class MyCustomSettings(ExtraSettings):
    >>>     aws_access_key_id: str = 'xxxxxxxxx'
    >>>     aws_secret_access_key: str = 'xxxxxxxx'
    """
    pass


@dataclass
class DjangoSettings(BaseDjangoSettings):
    """Main Django settings class"""
    # CORE
    debug: bool = True
    debug_propagate_exceptions: bool = False
    admins: List[Tuple[str, str]] = None
    internal_ips: List[str] = None
    allowed_hosts: List[str] = None
    time_zone: str = "UTC"
    use_tz: bool = True
    language_code: str = "en-us"
    languages: List[Tuple[str, str]] = None
    languages_bidi: List[str] = None
    use_i18n: bool = True
    locale_paths: List[str] = None

    # Language Cookie Settings
    language_cookie_name: str = "django_language"
    language_cookie_age: Optional[int] = None
    language_cookie_domain: Optional[str] = None
    language_cookie_path: str = "/"
    language_cookie_secure: bool = False
    language_cookie_httponly: bool = False
    language_cookie_samesite: Optional[str] = None

    # Management
    managers: List[Tuple[str, str]] = None
    default_charset: str = "utf-8"
    server_email: str = "root@localhost"

    # Database
    databases: DjangoDatabases = None
    database_routers: List[str] = None

    # Email
    email_backend: str = "django.core.mail.backends.smtp.EmailBackend"
    email_host: str = "localhost"
    email_port: int = 25
    email_use_localtime: bool = False
    email_host_user: str = ""
    email_host_password: str = ""
    email_use_tls: bool = False
    email_use_ssl: bool = False
    email_ssl_certfile: Optional[str] = None
    email_ssl_keyfile: Optional[str] = None
    email_timeout: Optional[int] = None
    default_from_email: str = "webmaster@localhost"
    email_subject_prefix: str = "[Django] "

    # Apps and Templates
    installed_apps: List[str] = None
    templates: List[Dict[str, Any]] = None
    template_dirs: List[Any] = None
    form_renderer: str = "django.forms.renderers.DjangoTemplates"
    forms_urlfield_assume_https: bool = False

    # URL Configuration
    append_slash: bool = True
    prepend_www: bool = False
    force_script_name: Optional[str] = None
    disallowed_user_agents: List[Any] = None
    absolute_url_overrides: Dict[str, Any] = None
    ignorable_404_urls: List[Any] = None

    # Security
    secret_key: str = ""
    secret_key_fallbacks: List[str] = None

    # Storage
    storages: Dict[str, Dict[str, str]] = None
    media_root: Optional[Any] = ""
    media_url: str = "/media/"
    static_root: Optional[Any] = None
    static_url: Optional[str] = '/static/'

    # File Uploads
    file_upload_handlers: List[str] = None
    file_upload_max_memory_size: int = 2621440
    data_upload_max_memory_size: int = 2621440
    data_upload_max_number_fields: int = 1000
    data_upload_max_number_files: int = 100
    file_upload_temp_dir: Optional[str] = None
    file_upload_permissions: int = 0o644
    file_upload_directory_permissions: Optional[int] = None

    # Formatting
    format_module_path: Optional[str] = None
    date_format: str = "N j, Y"
    datetime_format: str = "N j, Y, P"
    time_format: str = "P"
    year_month_format: str = "F Y"
    month_day_format: str = "F j"
    short_date_format: str = "m/d/Y"
    short_datetime_format: str = "m/d/Y P"
    date_input_formats: List[str] = None
    time_input_formats: List[str] = None
    datetime_input_formats: List[str] = None
    first_day_of_week: int = 0
    decimal_separator: str = "."
    use_thousand_separator: bool = False
    number_grouping: int = 0
    thousand_separator: str = ","

    # Database Tablespaces
    default_tablespace: str = ""
    default_index_tablespace: str = ""
    default_auto_field: str = "django.db.models.BigAutoField"

    # Security Headers
    x_frame_options: str = "DENY"
    use_x_forwarded_host: bool = False
    use_x_forwarded_port: bool = False
    wsgi_application: Optional[str] = None
    secure_proxy_ssl_header: Optional[Tuple[str, str]] = None

    # Middleware
    middleware: List[str] = None

    # Sessions
    session_cache_alias: str = "default"
    session_cookie_name: str = "sessionid"
    session_cookie_age: int = 60 * 60 * 24 * 7 * 2
    session_cookie_domain: Optional[str] = None
    session_cookie_secure: bool = False
    session_cookie_path: str = "/"
    session_cookie_httponly: bool = True
    session_cookie_samesite: str = "Lax"
    session_save_every_request: bool = False
    session_expire_at_browser_close: bool = False
    session_engine: str = "django.contrib.sessions.backends.db"
    session_file_path: Optional[str] = None
    session_serializer: str = "django.contrib.sessions.serializers.JSONSerializer"

    # Cache
    caches: Dict[str, Dict[str, str]] = None
    cache_middleware_key_prefix: str = ""
    cache_middleware_seconds: int = 600
    cache_middleware_alias: str = "default"

    # Authentication
    auth_user_model: str = "auth.User"
    authentication_backends: List[str] = None
    login_url: str = "/accounts/login/"
    login_redirect_url: str = "/accounts/profile/"
    logout_redirect_url: Optional[str] = None
    password_reset_timeout: int = 60 * 60 * 24 * 3
    password_hashers: List[str] = None
    auth_password_validators: List[Dict[str, Any]] = None

    # Signing
    signing_backend: str = "django.core.signing.TimestampSigner"

    # CSRF
    csrf_failure_view: str = "django.views.csrf.csrf_failure"
    csrf_cookie_name: str = "csrftoken"
    csrf_cookie_age: int = 60 * 60 * 24 * 7 * 52
    csrf_cookie_domain: Optional[str] = None
    csrf_cookie_path: str = "/"
    csrf_cookie_secure: bool = False
    csrf_cookie_httponly: bool = False
    csrf_cookie_samesite: str = "Lax"
    csrf_header_name: str = "HTTP_X_CSRFTOKEN"
    csrf_trusted_origins: List[str] = None
    csrf_use_sessions: bool = False

    # Messages
    message_storage: str = "django.contrib.messages.storage.fallback.FallbackStorage"

    # Logging
    logging_config: str = "logging.config.dictConfig"
    logging: Dict[str, Any] = None
    default_exception_reporter: str = "django.views.debug.ExceptionReporter"
    default_exception_reporter_filter: str = "django.views.debug.SafeExceptionReporterFilter"

    # Testing
    test_runner: str = "django.test.runner.DiscoverRunner"
    test_non_serialized_apps: List[str] = None

    # Fixtures
    fixture_dirs: List[str] = None

    # Static Files
    staticfiles_dirs: List[str] = None
    staticfiles_finders: List[str] = None

    # Migrations
    migration_modules: Dict[str, str] = None

    # System Checks
    silenced_system_checks: List[str] = None

    # Security Middleware
    secure_content_type_nosniff: bool = True
    secure_cross_origin_opener_policy: str = "same-origin"
    secure_hsts_include_subdomains: bool = False
    secure_hsts_preload: bool = False
    secure_hsts_seconds: int = 0
    secure_redirect_exempt: List[str] = None
    secure_referrer_policy: str = "same-origin"
    secure_ssl_host: Optional[str] = None
    secure_ssl_redirect: bool = False

    root_urlconf:str = ''

    # Extra settings
    extra: ExtraSettings = None

    def __post_init__(self):
        # Initialize None fields with appropriate default values
        if self.installed_apps is None:
            self.installed_apps = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles'
            ]
        if self.templates is None:
            self.templates = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': self.template_dirs or [],
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': [
                            'django.template.context_processors.request',
                            'django.contrib.auth.context_processors.auth',
                            'django.contrib.messages.context_processors.messages',
                        ],
                    },
                },
            ]
        if self.disallowed_user_agents is None:
            self.disallowed_user_agents = []
        if self.absolute_url_overrides is None:
            self.absolute_url_overrides = {}
        if self.ignorable_404_urls is None:
            self.ignorable_404_urls = []
        if self.secret_key_fallbacks is None:
            self.secret_key_fallbacks = []
        if self.storages is None:
            self.storages = {
                "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
                "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"}
            }
        if self.middleware is None:
            self.middleware = [
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ]
        if self.caches is None:
            self.caches = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
        if self.authentication_backends is None:
            self.authentication_backends = ["django.contrib.auth.backends.ModelBackend"]
        if self.password_hashers is None:
            self.password_hashers = [
                "django.contrib.auth.hashers.PBKDF2PasswordHasher",
                "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
                "django.contrib.auth.hashers.Argon2PasswordHasher",
                "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
                "django.contrib.auth.hashers.ScryptPasswordHasher"
            ]
        if self.auth_password_validators is None:
            self.auth_password_validators = [
                {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
                {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
                {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
                {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
            ]
        if self.staticfiles_finders is None:
            self.staticfiles_finders = [
                "django.contrib.staticfiles.finders.FileSystemFinder",
                "django.contrib.staticfiles.finders.AppDirectoriesFinder"
            ]

    def __dir__(self):
        """Return Django-style uppercase attribute names for dir() calls."""

        # Also include regular dataclass attributes and methods
        regular_attrs = object.__dir__(self)

        # upper case data class attributes
        for attr in regular_attrs:
            if attr in self.__dataclass_fields__:
                regular_attrs[regular_attrs.index(attr)] = attr.upper()

        # Combine and sort them
        return sorted(set(regular_attrs))

    def __getattr__(self, name):
        """Allow access to Django settings using uppercase names."""
        django_dict = self.as_dict
        if name in django_dict:
            return django_dict[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def register(self):
        """
        Register the Django specific settings in the globals registry.
        """
        caller_frame = inspect.currentframe().f_back
        module = inspect.getmodule(caller_frame)

        # Inject validated fields as module-level variables
        for field_name, field_value in self.as_dict.items():
            setattr(module, field_name, field_value)
