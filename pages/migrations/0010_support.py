# Generated by Django 2.1.1 on 2022-03-04 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20220304_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='0', max_length=200)),
                ('title', models.CharField(default='0', max_length=900)),
                ('message', models.TextField(max_length=1000)),
                ('support_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]