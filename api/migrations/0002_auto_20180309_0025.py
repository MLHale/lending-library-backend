# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
