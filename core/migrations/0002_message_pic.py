# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-30 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='pic',
            field=models.ImageField(default='/static/core/noavatar.jpg', upload_to='static/core/img/'),
        ),
    ]
