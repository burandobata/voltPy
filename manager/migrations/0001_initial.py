# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 14:12
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
            name='CurveBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderInFile', models.IntegerField()),
                ('name', models.TextField()),
                ('comment', models.TextField()),
                ('params', jsonfield.fields.JSONField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CurveCalibrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.TextField()),
                ('method', models.TextField()),
                ('result', models.FloatField()),
                ('resultStdDev', models.FloatField()),
                ('corrCoeff', models.FloatField()),
                ('vector', jsonfield.fields.JSONField()),
                ('fitEquation', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='CurveFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('fileDate', models.DateField()),
                ('uploadDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CurveIndexing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('potential_min', models.FloatField()),
                ('potential_max', models.FloatField()),
                ('potential_step', models.FloatField()),
                ('time_min', models.FloatField()),
                ('time_max', models.FloatField()),
                ('time_step', models.FloatField()),
                ('current_min', models.FloatField()),
                ('current_max', models.FloatField()),
                ('current_range', models.FloatField()),
                ('probingRate', models.IntegerField()),
                ('curveBasic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.CurveBasic')),
            ],
        ),
        migrations.CreateModel(
            name='CurveVectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.TextField()),
                ('method', models.TextField()),
                ('time', jsonfield.fields.JSONField()),
                ('potential', jsonfield.fields.JSONField()),
                ('current', jsonfield.fields.JSONField()),
                ('concentration', jsonfield.fields.JSONField()),
                ('concentrationUnits', jsonfield.fields.JSONField()),
                ('probingData', jsonfield.fields.JSONField()),
                ('curve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.CurveBasic')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('groups', models.ManyToManyField(to='manager.Group')),
            ],
        ),
        migrations.AddField(
            model_name='curvefile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.User'),
        ),
        migrations.AddField(
            model_name='curvecalibrations',
            name='curves',
            field=models.ManyToManyField(to='manager.CurveVectors'),
        ),
        migrations.AddField(
            model_name='curvebasic',
            name='curveFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.CurveFile'),
        ),
    ]
