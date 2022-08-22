
"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gto(ng2vaa_z7en3_%w4c!i5ibzlycp6oim8+)rolj*yjvn14c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','15.207.109.170','test.saneobserver.ai']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'rest_framework',
    'corsheaders',
    "storages",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'build')
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     "default": {      
        
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'saneobserver_database',
#         'USER': 'shivamayyubraj',
#         'PASSWORD': 'developedbyamosta',
#         'HOST': 'database-1.cbzl07gxnei8.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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



AUTH_USER_MODEL = 'accounts.User'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
  
     os.path.join(BASE_DIR, 'build/static'),
     
     os.path.join(BASE_DIR, 'build/assets'),

]




# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ================================================================

AWS_ACCESS_KEY_ID = 'AKIAV7WPUE5IJU7OE5OZ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sanes3bucket'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME ="ap-south-1" 
AWS_S3_HOST = "s3. ap-south-1.amazonaws.com"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_HOST = 'sg2plcpnl0135.prod.sin2.secureserver.net'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'do-not-reply@humhai.in'
DEFAULT_FROM_EMAIL = 'do-not-reply@humhai.in'
EMAIL_HOST_PASSWORD = 'Amostapass@$123'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False



# testing
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

#final test
