# Generated by Django 4.2.4 on 2023-09-06 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='image',
            new_name='img',
        ),
    ]
