# Generated by Django 2.0.6 on 2018-10-15 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormModel',
            new_name='Recipe',
        ),
    ]