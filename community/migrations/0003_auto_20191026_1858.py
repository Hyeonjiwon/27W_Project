# Generated by Django 2.2.4 on 2019-10-26 09:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20191026_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
