# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-29 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nextids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nextids_id', models.CharField(max_length=200)),
                ('nextids_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
