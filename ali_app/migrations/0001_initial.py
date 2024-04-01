# Generated by Django 4.1.13 on 2024-03-27 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=255, verbose_name='Title')),
                ('desc', models.TextField(max_length=1000, verbose_name='Description')),
                ('image', models.CharField(max_length=500, verbose_name='Reference')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date')),
            ],
        ),
    ]