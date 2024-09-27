# Generated by Django 5.1.1 on 2024-09-27 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('english_title', models.CharField(max_length=255)),
                ('line', models.IntegerField()),
                ('address', models.TextField()),
                ('lat', models.CharField(max_length=50)),
                ('lang', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='information.station')),
            ],
        ),
    ]
