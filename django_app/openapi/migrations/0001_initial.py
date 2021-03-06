# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 04:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('place', models.CharField(max_length=100, null=True)),
                ('realm_name', models.CharField(max_length=50, null=True)),
                ('area', models.CharField(max_length=10, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('ticket_url', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('thumbnail', models.CharField(max_length=200, null=True)),
                ('gps_x', models.CharField(max_length=30, null=True)),
                ('gps_y', models.CharField(max_length=30, null=True)),
                ('place_url', models.CharField(max_length=200, null=True)),
                ('place_addr', models.CharField(max_length=100, null=True)),
                ('place_seq', models.CharField(max_length=10, null=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='performance_set', to='openapi.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='performance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', to='openapi.Performance'),
        ),
    ]
