# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-02 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagementSystem', '0007_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='association',
            old_name='associationName',
            new_name='associationID',
        ),
    ]
