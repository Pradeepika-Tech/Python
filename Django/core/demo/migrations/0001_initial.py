# Generated by Django 4.2.5 on 2023-09-15 08:24

import datetime
import demo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to=demo.models.user_directory_path)),
                ('image_caption', models.CharField(default='Photo by demo', max_length=100)),
                ('publish', models.DateTimeField(default=datetime.datetime(2023, 9, 15, 8, 24, 44, 458722, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
