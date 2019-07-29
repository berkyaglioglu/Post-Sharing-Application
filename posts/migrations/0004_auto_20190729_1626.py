# Generated by Django 2.0.6 on 2019-07-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190729_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='rate',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
