# Generated by Django 3.1.1 on 2020-09-25 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_is_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='is_published',
            new_name='is_forSale',
        ),
    ]
