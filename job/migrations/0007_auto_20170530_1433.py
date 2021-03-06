# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 21:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_detail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_detail',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 30, 14, 33, 32, 597523)),
        ),
        migrations.AlterField(
            model_name='job_detail',
            name='working_hour',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19),
        ),
    ]
