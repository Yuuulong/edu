# Generated by Django 2.0 on 2018-12-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20181226_2034'),
        ('courses', '0002_auto_20181225_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete='models.CASCADE', to='organization.CourseOrg', verbose_name='连锁分校'),
        ),
    ]
