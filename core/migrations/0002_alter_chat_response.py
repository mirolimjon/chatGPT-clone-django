# Generated by Django 4.2.3 on 2023-07-08 05:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='response',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
