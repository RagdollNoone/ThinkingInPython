# Generated by Django 3.0.2 on 2020-02-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_model', '0003_auto_20200206_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meet',
            name='organizer',
        ),
        migrations.AddField(
            model_name='meet',
            name='organizer',
            field=models.ManyToManyField(to='base_model.User'),
        ),
    ]