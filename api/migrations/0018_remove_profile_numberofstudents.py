# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-25 17:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20190618_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='numberofstudents',
        ),
    ]
