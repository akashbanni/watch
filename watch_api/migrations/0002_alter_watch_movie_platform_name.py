# Generated by Django 4.2.1 on 2024-03-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch_movie',
            name='platform_name',
            field=models.CharField(default='Netflix', max_length=50),
        ),
    ]
