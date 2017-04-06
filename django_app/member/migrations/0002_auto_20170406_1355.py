# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 04:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('openapi', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openapi.Performance'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myuser',
            name='bookmark_performance',
            field=models.ManyToManyField(blank=True, through='member.Bookmark', to='openapi.Performance'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together=set([('user', 'content')]),
        ),
    ]