# Generated by Django 2.2.5 on 2021-04-30 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0002_languagetype_language_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languagetype',
            name='language_genre',
        ),
    ]
