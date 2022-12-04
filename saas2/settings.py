
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ''


DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #  APPS
    'core',
    'users',
    'surveys',
    'blog',

    # TAILWIND
    'tailwind',
    'theme',
    'django_browser_reload',

    # CRISPY FORMS
    'crispy_forms',
    'crispy_tailwind',

    # AUTHENTICATION
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # REST FRAMEWORK
    'rest_framework',

    # CK EDITOR
    'ckeditor',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',


    # TAILWIND
    "django_browser_reload.middleware.BrowserReloadMiddleware",

]

ROOT_URLCONF = 'saas2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'saas2.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# STATIC
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
   ]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# TAILWIND
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

# STRIPE
STRIPE_TEST_PUBLISHABLE_KEY ='' # Public Key
STRIPE_TEST_SECRET_KEY ='' 
STRIPE_LIVE_MODE = False  # Change to True in production

STRIPE_WEBHOOK_SECRET = ""

# FREE TRIAL OFFERING TEST
STRIPE_PRICE_ID_FREE = ''

# BASIC OFFERING TEST
STRIPE_PRICE_ID_BASIC = ''

# PREMIUM OFFERING TEST
STRIPE_PRICE_ID = ''


# CRISY FORMS
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"


# AUTHENTICATION
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        },
    }
}

SITE_ID = 2
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = ''

# SAAS TEST AUTH (Google app name)
CLEINT_ID = ''
CLIENT_SECRET = ''
SOCIALACCOUNT_LOGIN_ON_GET=True


# SEND GRID RESET PASSWORD
SENDGRID_API_KEY = ''

CONTACT_EMAIL = ''
ADMIN_EMAILS = ''

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = ''



