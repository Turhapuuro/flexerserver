# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0017_auto_20180114_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='total_hours',
        ),
    ]