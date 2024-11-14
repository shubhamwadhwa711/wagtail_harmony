# Generated by Django 5.1.2 on 2024-11-12 03:28

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="MeetingPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [("button", 4)],
                        blank=True,
                        block_lookup={
                            0: ("wagtail.blocks.CharBlock", (), {}),
                            1: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("btn-dark", "Dark"),
                                        ("btn-light", "Light"),
                                        ("btn-link", "Link"),
                                        ("btn-primary", "Primary"),
                                        ("btn-secondary", "Secondary"),
                                    ]
                                },
                            ),
                            2: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            3: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "URL", "required": False},
                            ),
                            4: (
                                "wagtail.blocks.StructBlock",
                                [[("text", 0), ("type", 1), ("page", 2), ("url", 3)]],
                                {},
                            ),
                        },
                    ),
                ),
                (
                    "meeting_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Meeting Date"
                    ),
                ),
                (
                    "meeting_start_time",
                    models.TimeField(blank=True, null=True, verbose_name="Start Time"),
                ),
                (
                    "meeting_end_time",
                    models.TimeField(blank=True, null=True, verbose_name="End Time"),
                ),
                (
                    "meeting_description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Enter meeting AGENDA"
                    ),
                ),
                (
                    "meeting_type",
                    models.CharField(
                        choices=[
                            ("gov", "Gov. Meetings"),
                            ("society", "Society Meetings"),
                            ("rwa", "Monthly RWA Meetings"),
                        ],
                        default="society",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "Meeting",
                "verbose_name_plural": "Meetings",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MeetingsPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [("button", 4)],
                        blank=True,
                        block_lookup={
                            0: ("wagtail.blocks.CharBlock", (), {}),
                            1: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("btn-dark", "Dark"),
                                        ("btn-light", "Light"),
                                        ("btn-link", "Link"),
                                        ("btn-primary", "Primary"),
                                        ("btn-secondary", "Secondary"),
                                    ]
                                },
                            ),
                            2: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            3: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "URL", "required": False},
                            ),
                            4: (
                                "wagtail.blocks.StructBlock",
                                [[("text", 0), ("type", 1), ("page", 2), ("url", 3)]],
                                {},
                            ),
                        },
                    ),
                ),
                (
                    "meeting_text",
                    models.CharField(
                        blank=True, default="All Meetings", max_length=200, null=True
                    ),
                ),
                (
                    "meeting_type",
                    models.CharField(
                        choices=[
                            ("gov", "Gov. Meetings"),
                            ("society", "Society Meetings"),
                            ("rwa", "Monthly RWA Meetings"),
                        ],
                        default="society",
                        max_length=20,
                    ),
                ),
                ("bottom_heading", models.TextField(blank=True, null=True)),
                (
                    "bottom_image_one",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "bottom_image_two",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "bottom_link_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "Meetings Page",
                "verbose_name_plural": "Meeting Pages",
            },
            bases=("wagtailcore.page",),
        ),
    ]