# Generated by Django 2.1.1 on 2022-03-03 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='country',
        ),
    ]