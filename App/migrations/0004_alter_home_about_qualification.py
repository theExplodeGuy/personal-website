# Generated by Django 4.1.3 on 2022-11-18 21:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_qualification_slug_home_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='about_qualification',
            field=ckeditor.fields.RichTextField(),
        ),
    ]