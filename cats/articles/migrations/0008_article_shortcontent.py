# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 18:44
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20161114_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='shortContent',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
