"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 1.10.6.
For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import json
import os

DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# 사용자가 업로드한 파일들을 관리할 폴더의 경로를 지정
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 정적파일을 관리할 폴더 경로 지정
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# 정적 파일을 모아서 서빙할 폴더 경로 지정 테스트시 server 관련 에러 날 경우 반드시 추가해야 함
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Config files
CONF_DIR = os.path.join(ROOT_DIR, '.conf-secret')
CONFIG_FILE_COMMON = os.path.join(CONF_DIR, 'settings_common.json')
config = json.loads(open(CONFIG_FILE_COMMON).read())
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['django']['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # OAuth
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',

    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 1
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # open api
    'openapi',

    # rest 관련

    'rest_framework',
    'rest_auth',
    'rest_framework.authtoken',

    'member.apps.MemberConfig',
    'performance.apps.PerformanceConfig',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    # OAuth
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # OAuth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# AWS설정입니다. (최영민)
AWS_ACCESS_KEY_ID = config['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config['aws']['s3_storage_bucket_name']

# S3를 쓰기 위한 설정입니다.(최영민)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# postgre sql을 쓰기 위한 설정입니다. (최영민)
DATABASES = {
      'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config['database']['name'],
            'USER': config['database']['user'],
            'PASSWORD': config['database']['password'],
            'HOST': 'localhost',
            'PORT': '5432',
      }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'member.MyUser'
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

]
SITE_ID = 1

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# Facebook
FB_APP_ID = config['facebook']['app_id']
FB_SECRET_CODE = config['facebook']['secret_code']
FB_APP_ACCESS_TOKEN = FB_APP_ID + '|' + FB_SECRET_CODE

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}
