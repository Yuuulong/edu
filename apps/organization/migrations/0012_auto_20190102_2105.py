# Generated by Django 2.0 on 2019-01-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0011_auto_20190102_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '面授'), ('gr', '网校'), ('gx', '其他')], default='pxjg', max_length=20, verbose_name='分校类别'),
        ),
    ]
