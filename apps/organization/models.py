from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市')
    desc = models.CharField(max_length=200, verbose_name='描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='分校名称')
    # 需要改成UEditorField
    desc = models.TextField(verbose_name='分校描述')
    tag = models.CharField(default="全国知名", max_length=10, verbose_name=u"分校标签")

    category = models.CharField(
        default='pxjg',
        verbose_name='分校类别',
        max_length=20,
        choices=(('pxjg', '面授'), ('gr', '网校'), ('gx', '其他')))
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(
        upload_to='org/%Y/%m', verbose_name='logo', max_length=100)
    address = models.CharField(max_length=150, verbose_name='分校地址')
    city = models.ForeignKey(
        CityDict, verbose_name='所在城市', on_delete=models.CASCADE)
    students = models.IntegerField(default=532, verbose_name='学习人数')
    course_nums = models.IntegerField(default=0, verbose_name='课程数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '连锁分校'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 获取连锁分校的教师数量
        return self.teacher_set.all().count()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(
        CourseOrg, verbose_name='所属分校', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='教师名')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='学位')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    points = models.CharField(max_length=120, verbose_name='教学特点')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    age = models.IntegerField(default=29, verbose_name='年龄')
    image = models.ImageField(
        default='',
        upload_to='teacher/%Y/%m',
        verbose_name='头像',
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
