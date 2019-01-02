# Generated by Django 2.0 on 2018-12-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20181225_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训分校'), ('gr', '个人'), ('gx', '高校')], default='pxjg', max_length=20, verbose_name='分校类别'),
        ),
    ]
