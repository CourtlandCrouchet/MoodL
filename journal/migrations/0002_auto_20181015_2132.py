# Generated by Django 2.1.1 on 2018-10-15 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Entries',
        ),
    ]