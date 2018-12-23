from .models import Course, Lesson, Video, CourseResource
import xadmin


class CourseAdmin(object):
    list_display = [
        'name', 'desc', 'detail', 'degree', 'learn_times', 'students'
    ]
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']  # 后台搜索
    list_filter = [
        'name', 'desc', 'detail', 'degree', 'learn_times', 'students'
    ]  # 筛选


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']  # 后台搜索
    list_filter = ['course__name', 'name', 'add_time']  # 筛选,course__name字段


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']  # 后台搜索
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name' 'download']  # 后台搜索
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

