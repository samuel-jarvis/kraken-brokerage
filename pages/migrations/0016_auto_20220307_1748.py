# Generated by Django 2.1.1 on 2022-03-07 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20220307_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='notification_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='Heading',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='Message',
            new_name='message',
        ),
    ]