# Generated by Django 5.0.6 on 2024-05-30 15:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_alter_art_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='artId',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
