# Generated by Django 5.0.6 on 2024-06-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_alter_applymission_aleradyapplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]