# Generated by Django 4.0.4 on 2022-06-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0006_userlist_songs_link_alter_userlist_play_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='play_list',
            field=models.CharField(blank=True, max_length=115, verbose_name='play list'),
        ),
    ]
