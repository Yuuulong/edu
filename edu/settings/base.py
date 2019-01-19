import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 让程序在apps中找到app
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Application definition
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'organization',
    'operation',
    'xadmin',
    'crispy_forms',
    'captcha',
    'pure_pagination',
    # 'DjangoUeditor',
]
AUTH_USER_MODEL = "users.UserProfile"  # 重载
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 添加模板路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.media',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'edu.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 改为中文

TIME_ZONE = 'Asia/Shanghai'  # 改时区

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 改为本地时间，防止数据库时间统计出错

EMAIL_FROM = '329227939@qq.com'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 上传资源文件配置

STATIC_URL = '/static/'  # 配置静态文件路径
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')  # 上传资源文件配置,收集静态文件配置