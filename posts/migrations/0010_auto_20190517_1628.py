# Generated by Django 2.0.6 on 2019-05-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20190517_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=1200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='ingredients',
            field=models.TextField(max_length=1200, verbose_name='Ingredients'),
        ),
    ]