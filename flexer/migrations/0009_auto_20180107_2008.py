# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0008_auto_20180107_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(),
        ),
    ]