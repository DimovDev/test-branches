# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 00:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_product', '0004_auto_20181025_0026'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='allproduct',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='allproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='allproduct',
            name='location',
        ),
        migrations.RemoveField(
            model_name='allproduct',
            name='owner',
        ),
        migrations.DeleteModel(
            name='AllProduct',
        ),
    ]