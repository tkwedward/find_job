# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 22:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20170617_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_detail',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 17, 15, 7, 41, 951825)),
        ),
    ]
