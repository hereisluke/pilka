# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-29 17:02
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('starts', models.TimeField(blank=True, null=True)),
                ('ends', models.TimeField(blank=True, null=True)),
                ('price', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('adress', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]