# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-08 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
