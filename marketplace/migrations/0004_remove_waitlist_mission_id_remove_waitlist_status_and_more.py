# Generated by Django 5.0.6 on 2024-05-31 10:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_delete_customuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waitlist',
            name='mission_id',
        ),
        migrations.RemoveField(
            model_name='waitlist',
            name='status',
        ),
        migrations.RemoveField(
            model_name='waitlist',
            name='submitted_at',
        ),
        migrations.RemoveField(
            model_name='waitlist',
            name='user_id',
        ),
        migrations.AddField(
            model_name='waitlist',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ApplyMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberApplied', models.IntegerField()),
                ('AleradyApplied', models.BooleanField()),
                ('mission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplace.mission')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
