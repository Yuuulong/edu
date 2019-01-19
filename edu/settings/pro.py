from .base import *
import os

SECRET_KEY = os.environ['SECRET_KEY_EDU']  # 将密码保存在本地环境变量，如果丢失可以重新生成
DEBUG = False
# 将异常邮件发送到邮箱
ADMINS = (('Antonio M', 'yuuuulong@gmai.com'), )

ALLOWED_HOSTS = ['*']

DATABASES_PASSWORD = os.environ['DATABASES_PASSWORD']  # 将数据库密码保存在本地环境
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edu_db',
        'USER': 'root',
        'PASSWORD': DATABASES_PASSWORD,
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
EMAIL_SUBJECT_PREFIX = '[菁航教育] '
EMAIL_USE_SSL = True  # 与SMTP服务器通信时，是否启动SSL链接(安全链接)
