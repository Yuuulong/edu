# Generated by Django 2.0 on 2018-12-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='desc',
            field=models.TextField(verbose_name='课程描述'),
        ),
    ]
