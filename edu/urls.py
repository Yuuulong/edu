"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView  # 通用视图，处理静态文件
from django.views.static import serve
from users.views import (ActiveUserView, ForgetPwdView, LoginView, LogoutView,
                         ModifyPwdView, RegisterView, ResetView)
from organization.views import OrgView
from edu.settings import MEDIA_ROOT
# from users.views import IndexView

urlpatterns = [
    url(r'xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^logout/$', LogoutView.as_view(), name="logout"),

    url('^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'active/(?P<active_code>.*)/$',
        ActiveUserView.as_view(),
        name='user_active'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 连锁分校url配置
    url(r'^org/', include(('organization.urls', 'organization'), namespace='org')),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 课程相关url配置

    url(r'^course/', include(('courses.urls', 'courses'), namespace='course')),

    # 讲师相关url配置
    url(r'^users/', include(('users.urls', 'users'), namespace="users")),

    # 富文本相关url
    # url(r'^ueditor/', include(('DjangoUeditor.urls', 'ueditor'), namespace="ueditor")),

]

# 全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
