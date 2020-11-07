# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-07 00:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201107_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='timmingtask',
            name='taskiphonenum',
            field=models.IntegerField(default=1, max_length=8, verbose_name='任务设备的数量'),
        ),
        migrations.AddField(
            model_name='timmingtask',
            name='taskiphonetype',
            field=models.CharField(default='android', max_length=8, verbose_name='任务设备类型'),
        ),
        migrations.AlterField(
            model_name='functionallofic',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 7, 8, 24, 53, 895745), verbose_name='更新时间'),
        ),
    ]