from .base import *


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {},
    'accounts': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'accounts.db.sqlite3',
        'USER': 'user',
        'PASSWORD': 'password',
    },
    'qna': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'qna.db.sqlite3',
        'USER': 'user',
        'PASSWORD': 'password',
    },
    'articles': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'article.db.sqlite3',
        'USER': 'user',
        'PASSWORD': 'password',
    },
    'community': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'community.db.sqlite3',
        'USER': 'user',
        'PASSWORD': 'password',
    },
    'freetalk': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'freetalk.db.sqlite3',
        'USER': 'user',
        'PASSWORD': 'password',
    },
}
