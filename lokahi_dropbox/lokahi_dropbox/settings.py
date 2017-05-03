"""
Django settings for lokahi_dropbox project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPOSITORY_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p*n75e!!d3(s3lf!)swc%*e79xq@pnw#vmv2$)vtvb9mtq*ddd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Password hashers

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Project apps
    'frontend',
    'messaging',
    'groups',
    'wall_post',
    'reports',
    'search',
    'site_manager',
    # Mist styling apps
    'bootstrapform',
    'bootstrap3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # Custom Login Middleware (comment if testing other pages...)
    # 'lokahi_dropbox.middleware.login_middleware.RequireLoginMiddleware'
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

ROOT_URLCONF = 'lokahi_dropbox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lokahi_dropbox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Heroku saves the day?
# POSTGRES_URL = "HEROKU_POSTGRESQL_PURPLE_URL"

DATABASES = {
    # Use the following for Heroku
    # 'default': dj_database_url.config(default=os.environ[POSTGRES_URL])
    # Use the following if local development
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lokahi_dropbox',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "frontend/static")

# MEDIA FILES (Files uploaded during web app use)
MEDIA_URL = '/reportFiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'reportFiles')

# Fixture files (JSON)
# https://docs.djangoproject.com/en/1.8/howto/initial-data/#id1

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

# STATICFILES_DIRS = (
# '/Users/danielbrown/Desktop/project/cs3240-s17-team21/lokahi_dropbox/frontend/static',
# )

# For login middleware (comment if testing...)
LOGIN_REQUIRED_URLS = (
    r'^/home/.*$',
    r'^/messaging/.*',
    r'^/groups/.*',
    r'^/wall/.*',
    r'^/reports/.*',
    r'^/manage_site/.*',
)

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'^$',
    r'^register/.*$'
    r'^logout/$'
    r'^/accounts/login/?next=.*/$',
)
