# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0014_auto_20180114_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='business_id',
            field=models.CharField(default='1234567-8', max_length=30),
            preserve_default=False,
        ),
    ]
