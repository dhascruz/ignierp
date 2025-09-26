"""
Django settings for ignierp project.
"""

import os
from pathlib import Path

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# SECURITY
# --------------------------------------------------
SECRET_KEY = 'django-insecure-417zqa0@u=x9tz1y_l^ioqvhve(i&a!_me@xjh#ga6oku_aw_u'
DEBUG = True

ALLOWED_HOSTS = [
    'my.igniteict.com',
    'www.my.igniteict.com',
    '210.18.177.188',
    'localhost',
    '*'
]

CORS_ALLOW_ALL_ORIGINS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'corsheaders',
    'rest_framework',
    'user_sessions',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_email',
    'two_factor',
    'two_factor.plugins.phonenumber',
    'two_factor.plugins.email',
    'debug_toolbar',
    'bootstrapform',
    'whitenoise.runserver_nostatic',

    # Local apps
    'eschool',
    'users',
    'teachers',
]

# --------------------------------------------------
# AUTH / LOGIN
# --------------------------------------------------
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = '/login/'

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'django_otp.middleware.OTPMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'two_factor.middleware.threadlocals.ThreadLocals',
]

# --------------------------------------------------
# URLS & WSGI/ASGI
# --------------------------------------------------
ROOT_URLCONF = 'ignierp.urls'
WSGI_APPLICATION = 'ignierp.wsgi.application'
ASGI_APPLICATION = 'ignierp.asgi.application'

# --------------------------------------------------
# DATABASES
# --------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ignierp',
        'USER': 'myadmin',
        'PASSWORD': '453cur135',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'moodle': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moodle_igni',
        'USER': 'myadmin',
        'PASSWORD': '453cur135',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('ta', 'Tamil'),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------
# STATIC & MEDIA
# --------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --------------------------------------------------
# DEFAULTS
# --------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------
# MOODLE INTEGRATION
# --------------------------------------------------
MOODLE_BASE_URL = "https://staging.igniteict.com"
MOODLE_WS_TOKEN = "f7b2275d40d76bc3478eae17a791026f"
