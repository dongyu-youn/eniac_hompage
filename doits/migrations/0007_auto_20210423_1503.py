# Generated by Django 2.2.5 on 2021-04-23 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doits', '0006_auto_20210423_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doit',
            old_name='explanation',
            new_name='explain',
        ),
    ]