# Generated by Django 2.2.5 on 2021-04-15 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('open_source', '0002_remove_opensourcereview_opensourcereview_indicated_host'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('code', models.TextField(default='1')),
                ('error', models.TextField(default='1')),
                ('explain_situation', models.TextField(default='1')),
                ('OpenSource_Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='open_source.OpenSource')),
                ('OpenSource_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
