# Generated by Django 5.0.4 on 2024-05-29 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='art',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.category'),
        ),
    ]