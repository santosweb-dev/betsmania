# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 19:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=126, verbose_name='Code')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Value')),
                ('match_type', models.CharField(max_length=100, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='BetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Value')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('code', models.CharField(blank=True, max_length=126, null=True, verbose_name='Code')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='bet_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apostas.BetGroup', verbose_name='Bet group'),
        ),
    ]