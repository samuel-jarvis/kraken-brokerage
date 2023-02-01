# Generated by Django 2.1.1 on 2022-03-04 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='0', max_length=200)),
                ('phone', models.CharField(default='0', max_length=900)),
                ('country', models.CharField(default='0', max_length=900)),
                ('wallet', models.CharField(default='0', max_length=900)),
                ('address', models.TextField(max_length=1000)),
            ],
        ),
    ]
