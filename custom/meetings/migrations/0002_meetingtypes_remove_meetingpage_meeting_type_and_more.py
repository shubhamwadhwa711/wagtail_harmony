# Generated by Django 5.1.2 on 2024-11-25 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MeetingTypes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name="meetingpage",
            name="meeting_type",
        ),
        migrations.AddField(
            model_name="meetingpage",
            name="meeting",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="meetings",
                to="meetings.meetingtypes",
            ),
        ),
    ]
