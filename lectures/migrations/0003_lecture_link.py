# Generated by Django 2.2.5 on 2021-04-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_auto_20210424_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='link',
            field=models.URLField(default='1', max_length=70),
        ),
    ]