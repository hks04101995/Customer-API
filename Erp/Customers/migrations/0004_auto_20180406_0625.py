# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_productproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='productproduct',
            name='price',
            field=models.FloatField(default='1.0', verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='productproduct',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
    ]
