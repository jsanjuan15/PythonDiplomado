# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-26 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_lista', models.CharField(max_length=200, unique=True)),
                ('fecha_lista', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_tarea', models.CharField(max_length=200, unique=True)),
                ('estado_tarea', models.BooleanField(default=False)),
                ('descripcion_tarea', models.TextField(blank=True, help_text='Describe la Tarea')),
                ('fecha_creacion_tarea', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion_tarea', models.DateTimeField(auto_now=True)),
                ('id_lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.Lista')),
            ],
        ),
    ]