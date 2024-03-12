# Generated by Django 4.2.1 on 2024-03-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='watch_movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=20)),
                ('director_name', models.CharField(max_length=30)),
                ('platform_name', models.CharField(max_length=50)),
                ('story_line', models.CharField(max_length=120)),
                ('release_year', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='watch_platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=50)),
                ('Platform_url', models.URLField(unique=True)),
            ],
        ),
    ]