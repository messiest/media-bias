# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('search_term', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('party', models.TextField(blank=True, null=True)),
                ('search_terms', models.TextField(blank=True, null=True)),
                ('election_year', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('retweets', models.IntegerField(blank=True, null=True)),
                ('favorites', models.IntegerField(blank=True, null=True)),
                ('hashtags', models.IntegerField(blank=True, null=True)),
                ('tweet_json', jsonfield.fields.JSONField(default=dict)),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TwitterData.Search')),
            ],
        ),
        migrations.AddField(
            model_name='search',
            name='senator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TwitterData.Senator'),
        ),
    ]