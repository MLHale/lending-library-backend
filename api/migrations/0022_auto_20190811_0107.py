# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-11 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190702_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default=b'Aaron', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default=b'Vigal', max_length=1000),
            preserve_default=False,
        ),
    ]
