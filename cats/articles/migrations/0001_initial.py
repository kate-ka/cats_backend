# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 16:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='articles_uploads/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(default=datetime.datetime(2016, 11, 12, 16, 8, 35, 977559, tzinfo=utc))),
                ('is_featured', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
