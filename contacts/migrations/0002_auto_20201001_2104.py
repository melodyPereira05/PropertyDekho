# Generated by Django 3.1.1 on 2020-10-01 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='property',
            new_name='property_name',
        ),
    ]
