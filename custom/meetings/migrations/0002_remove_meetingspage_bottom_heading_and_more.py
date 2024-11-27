# Generated by Django 5.1.2 on 2024-11-27 08:28

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetings", "0001_initial"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="meetingspage",
            name="bottom_heading",
        ),
        migrations.RemoveField(
            model_name="meetingspage",
            name="bottom_image_one",
        ),
        migrations.RemoveField(
            model_name="meetingspage",
            name="bottom_image_two",
        ),
        migrations.AddField(
            model_name="meetingspage",
            name="footer_heading",
            field=models.TextField(
                blank=True, default="Share your story about Harmony", null=True
            ),
        ),
        migrations.CreateModel(
            name="Footerimages",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="page_footer_images",
                        to="meetings.meetingspage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]