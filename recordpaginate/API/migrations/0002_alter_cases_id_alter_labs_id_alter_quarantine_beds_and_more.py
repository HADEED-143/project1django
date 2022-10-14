# Generated by Django 4.1.2 on 2022-10-12 04:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='labs',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='quarantine',
            name='beds',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='quarantine',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='summery',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
