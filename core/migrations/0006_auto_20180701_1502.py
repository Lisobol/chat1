# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-01 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_pic',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/media/'),
        ),
    ]