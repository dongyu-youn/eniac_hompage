# Generated by Django 2.2.5 on 2021-04-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='error',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='explain_situation',
            field=models.TextField(),
        ),
    ]