# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-30 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180630_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='file',
        ),
        migrations.AddField(
            model_name='message',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/core/files/'),
        ),
    ]
