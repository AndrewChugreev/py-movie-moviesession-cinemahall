# Generated by Django 4.0.2 on 2024-11-01 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_alter_movie_actors_alter_movie_genres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='seat_in_row',
            new_name='seats_in_row',
        ),
    ]
