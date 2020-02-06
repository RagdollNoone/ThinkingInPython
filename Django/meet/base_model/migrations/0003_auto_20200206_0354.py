# Generated by Django 3.0.2 on 2020-02-06 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_model', '0002_auto_20200206_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_model.User'),
        ),
        migrations.AlterField(
            model_name='meet',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_model.Room'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='meet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_model.Meet'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_model.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_model.Group'),
        ),
    ]
