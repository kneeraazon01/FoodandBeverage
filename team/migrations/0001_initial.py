# Generated by Django 3.0 on 2019-12-16 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]