# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 12:54
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20161112_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
