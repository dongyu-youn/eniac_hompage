# Generated by Django 2.2.5 on 2021-04-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0002_study_image'),
        ('open_source', '0002_remove_opensourcereview_opensourcereview_indicated_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='opensource',
            name='code_Language',
            field=models.ManyToManyField(related_name='code_language', to='studies.LanguageType'),
        ),
    ]