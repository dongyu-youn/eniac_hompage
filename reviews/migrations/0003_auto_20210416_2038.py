# Generated by Django 2.2.5 on 2021-04-16 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210416_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='OpenSource_Room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='open_source.OpenSource'),
        ),
        migrations.AlterField(
            model_name='review',
            name='OpenSource_host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
