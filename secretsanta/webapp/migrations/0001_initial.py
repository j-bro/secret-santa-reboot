# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 00:56
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
            name='Draw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateField()),
                ('activated_date', models.DateField(null=True)),
                ('price_cap', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GiftList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_list', models.TextField(default='')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_lists', to='webapp.Exchange')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_lists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manages', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='person_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exchange',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchanges', to='webapp.PersonGroup'),
        ),
        migrations.AddField(
            model_name='draw',
            name='exchange',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draws', to='webapp.Exchange'),
        ),
        migrations.AddField(
            model_name='draw',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='draw',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
