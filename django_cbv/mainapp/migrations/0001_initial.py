# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-24 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Your name', max_length=30)),
                ('job', models.CharField(default='your Job', max_length=30)),
            ],
        ),
    ]
