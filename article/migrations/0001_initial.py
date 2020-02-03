# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-11 21:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id_article', models.AutoField(primary_key=True, serialize=False)),
                ('unique_id_article', models.PositiveIntegerField(serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('content', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('is_visible_for_quests', models.BooleanField(default=True))
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='parent_article',
            field=models.ForeignKey(null=True, to='article.Article'),
        ),

        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=70)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('last_login_at', models.DateField(null=True)),
                ('is_blocked', models.BooleanField(default=False))
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.User'),
        ),
    ]