# Generated by Django 3.1.1 on 2020-09-27 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20200927_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crime_details',
            name='autopsia',
        ),
    ]
