# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-04 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181203_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('state', models.CharField(choices=[('new', 'New'), ('accepted', 'Accepted'), ('completed', 'Completed'), ('declined', 'Declined'), ('cancelled', 'Cancelled')], default='new', max_length=5)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
