# Generated by Django 3.1.1 on 2020-09-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='num_prop',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
