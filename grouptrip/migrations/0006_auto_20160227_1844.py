# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grouptrip', '0005_auto_20160227_1818'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TripPreferences',
            new_name='TripPreference',
        ),
    ]
