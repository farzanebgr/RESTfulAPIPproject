# Generated by Django 4.1 on 2022-08-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list_app', '0005_review_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avr_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_of_rating',
            field=models.IntegerField(default=0),
        ),
    ]