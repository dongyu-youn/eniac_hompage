# Generated by Django 2.2.5 on 2021-04-30 00:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 0, 58, 18, 262216, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
