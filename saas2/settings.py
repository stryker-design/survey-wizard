from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%c8*q1=7jqjr-zk_czoks7eq+n#bse7*!($r%+ot(wilk(*%%8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
   ]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# TAILWIND

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]


# STRIPE

STRIPE_TEST_PUBLISHABLE_KEY ='pk_test_51L4ltxHvQVNViNJTRaIt1p8bB8ocap09NdJzID1XZ57dCjg2lwMqwivDS8kJ5zP0FoKun43p68FBCDAlloY3iMfe001QL3KorY' # Public Key
STRIPE_TEST_SECRET_KEY ='sk_test_51L4ltxHvQVNViNJTRRyWCctAJeCjiV6LwTrF4AglAKVUqLxa1WavmP9SIHLlKplA5ekxs9viqfj5PWG7kWELD9zf00C4Iq5Zyj' 
STRIPE_LIVE_MODE = False  # Change to True in production

STRIPE_WEBHOOK_SECRET = "whsec_58608f171a98775c7ff14383a5f1379acc9f92215185862e3cdda2eb259780c3"

# FREE TRIAL OFFERING TEST
STRIPE_PRICE_ID_FREE = 'price_1LoE5nHvQVNViNJTu3AmMGD5'

# BASIC OFFERING TEST
STRIPE_PRICE_ID_BASIC = 'price_1LlvveHvQVNViNJT0Nbvf7Fa'

# PREMIUM OFFERING TEST
STRIPE_PRICE_ID = 'price_1Llvw9HvQVNViNJT8rDv38wy'


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
            'client_id': '722631368795-3tka9ss3ugkmm5qfehb5406ph9eholgu.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
    }
}

SITE_ID = 2

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = ''


# CLIENT_ID = '609942825212-e7nnmflthbnt3fe7lp4ethp3jrbcvgp9.apps.googleusercontent.com'
# CLIENT_SECRET_ID = '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'



# SAAS TEST AUTH (Google app name)
CLEINT_ID = '722631368795-3tka9ss3ugkmm5qfehb5406ph9eholgu.apps.googleusercontent.com'

CLIENT_SECRET = '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'

SOCIALACCOUNT_LOGIN_ON_GET=True


# SEND GRID RESET PASSWORD

SENDGRID_API_KEY = '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'

CONTACT_EMAIL = ''
ADMIN_EMAILS = 'stryker.web.design@gmail.com'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'stryker.web.agency@gmail.com'



