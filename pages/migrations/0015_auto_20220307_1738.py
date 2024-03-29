# Generated by Django 2.1.1 on 2022-03-07 17:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0014_auto_20220306_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(default='Profit Earned', max_length=100)),
                ('Message', models.TextField(default='0', max_length=200)),
                ('notification_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(default='Add Details', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
