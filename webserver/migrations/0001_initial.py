# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-07 08:04
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
            name='cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('power', models.CharField(max_length=20, verbose_name='\u6743\u9650')),
            ],
            options={
                'db_table': 'cabinet',
            },
        ),
        migrations.CreateModel(
            name='hostinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255, verbose_name='\u4e3b\u673a\u540d')),
                ('IP', models.CharField(max_length=50, verbose_name='IP\u5730\u5740')),
                ('Mem', models.IntegerField(verbose_name='\u5185\u5b58')),
                ('CPU', models.CharField(max_length=255, verbose_name='cpu')),
                ('CPUS', models.IntegerField(verbose_name='cpus')),
                ('OS', models.CharField(max_length=255, verbose_name='os')),
                ('virtual1', models.CharField(max_length=255, verbose_name='virtual')),
                ('status', models.CharField(max_length=50, verbose_name='\u72b6\u6001')),
            ],
        ),
        migrations.CreateModel(
            name='monitorMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostid', models.IntegerField(verbose_name='\u76d1\u63a7\u4e3b\u673aID')),
                ('avai', models.CharField(max_length=20, verbose_name='\u7a7a\u95f2\u5185\u5b58')),
                ('total', models.CharField(max_length=20, verbose_name='\u603b\u5185\u5b58')),
                ('ratio', models.CharField(max_length=20, verbose_name='\u4f7f\u7528\u7387')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('pid', models.IntegerField(verbose_name='pid')),
                ('module_letter', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='webserver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='\u624b\u673a')),
                ('user_role', models.CharField(max_length=40, verbose_name='\u89d2\u8272')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
            ],
        ),
    ]
