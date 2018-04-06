# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0002_auto_20180406_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40, verbose_name='Product')),
                ('reference', models.CharField(max_length=40, verbose_name='SKU')),
                ('Type', models.CharField(choices=[('product', 'Stockable'), ('consu', 'Consumable'), ('service', 'Service')], default='product', max_length=50)),
                ('quantity', models.FloatField(verbose_name='Quantity')),
            ],
        ),
    ]
