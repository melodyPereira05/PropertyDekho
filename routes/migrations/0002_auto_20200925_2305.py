# Generated by Django 3.1.1 on 2020-09-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testemonial',
            name='rating',
            field=models.CharField(max_length=5),
        ),
    ]
