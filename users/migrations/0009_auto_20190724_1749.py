# Generated by Django 2.0.6 on 2019-07-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190724_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=6),
        ),
    ]
