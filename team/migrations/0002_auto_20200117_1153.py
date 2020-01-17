# Generated by Django 2.1 on 2020-01-17 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='description',
        ),
        migrations.RemoveField(
            model_name='team',
            name='post_date',
        ),
        migrations.AddField(
            model_name='team',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='team',
            name='position',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
