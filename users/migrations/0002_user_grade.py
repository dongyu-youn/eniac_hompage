# Generated by Django 2.2.5 on 2021-03-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.CharField(blank=True, choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년')], max_length=20, null=True),
        ),
    ]
