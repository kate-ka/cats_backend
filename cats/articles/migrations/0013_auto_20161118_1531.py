# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20161118_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='articles.Choice'),
        ),
    ]
