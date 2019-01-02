import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True  # 开启主题
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '菁航教育后台管理系统'
    site_footer = '菁航教育'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']  # 后台搜索
    list_filter = ['code', 'email', 'send_type', 'send_time']  # 筛选


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']  # 后台搜索
    list_filter = ['title', 'image', 'url', 'index', 'add_time']  # 筛选


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
