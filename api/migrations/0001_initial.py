# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from ..models import Book, Recipe, Ingredient, ScheduleEntry


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('description', models.CharField(max_length=200)),

            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('recipe', models.ForeignKey(Recipe)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entryDate', models.DateField()),
                ('breakfastEntry', models.ForeignKey(Recipe, related_name="breakfast")),
                ('lunchEntry', models.ForeignKey(Recipe, related_name="lunch")),
                ('dinnerEntry', models.ForeignKey(Recipe, related_name="dinner")),
            ],
        ),
    ]
