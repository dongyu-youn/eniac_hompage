# Generated by Django 2.2.5 on 2021-04-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doits', '0003_auto_20210422_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doit',
            name='link',
            field=models.URLField(max_length=70),
        ),
        migrations.AlterField(
            model_name='doit',
            name='개발자',
            field=models.CharField(max_length=10),
        ),
    ]
