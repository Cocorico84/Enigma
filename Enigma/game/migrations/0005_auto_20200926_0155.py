# Generated by Django 3.1.1 on 2020-09-25 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20200926_0148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='victim',
            old_name='autopsia',
            new_name='medical_file',
        ),
    ]