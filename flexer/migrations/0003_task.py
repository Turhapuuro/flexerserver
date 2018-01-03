# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0002_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('break_time', models.TimeField()),
                ('total_hours', models.TimeField()),
            ],
        ),
    ]