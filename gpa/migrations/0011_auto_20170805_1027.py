# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-05 04:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpa', '0010_auto_20170805_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='index',
            new_name='user',
        ),
    ]
