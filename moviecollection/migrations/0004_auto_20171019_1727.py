# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-19 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecollection', '0003_auto_20171019_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(blank=True, to='moviecollection.Tag'),
        ),
    ]
