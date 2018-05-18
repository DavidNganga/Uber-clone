# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-18 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=30)),
                ('number_plate', models.CharField(max_length=30)),
                ('seat_numbers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='driver.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.IntegerField()),
                ('latitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='pickup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='driver.Pickup'),
        ),
        migrations.AddField(
            model_name='driver',
            name='tags',
            field=models.ManyToManyField(to='driver.tags'),
        ),
    ]
