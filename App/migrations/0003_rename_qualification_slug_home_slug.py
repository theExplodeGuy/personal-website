# Generated by Django 4.1.3 on 2022-11-12 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_home_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='qualification_slug',
            new_name='slug',
        ),
    ]
