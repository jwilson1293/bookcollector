# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-06 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0021_auto_20170906_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, to='bookcollection.Tag'),
        ),
    ]
