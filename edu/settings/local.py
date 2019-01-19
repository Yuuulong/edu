from . base import *
import os

SECRET_KEY = os.environ['SECRET_KEY_EDU']
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edu_db',
        'USER': 'root',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '329227939@qq.com'
EMAIL_FROM = '329227939@qq.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_SUBJECT_PREFIX = '[黄宇龙的博客] '
EMAIL_USE_SSL = True  # 与SMTP服务器通信时，是否启动SSL链接(安全链接)
