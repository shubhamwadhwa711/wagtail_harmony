# Generated by Django 5.1.2 on 2024-11-27 11:38

import django.db.models.deletion
import modelcluster.fields
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
            name="EmergencyPage",
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
                    "heading",
                    models.TextField(
                        blank=True, default="All Emergency Services", null=True
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
                    "cover_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Cover image for this page, used in listings and at the top of the page",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Emergency service Page",
                "verbose_name_plural": "Emergency service Pages",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="EmergencyPageContent",
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
                ("service_sidebar_name", models.TextField(blank=True, null=True)),
                ("service_name_heading", models.TextField(blank=True, null=True)),
                ("short_description", models.TextField(blank=True, null=True)),
                ("call_text", models.TextField(blank=True, default="Call", null=True)),
                ("mobile_number", models.TextField(blank=True, null=True)),
                (
                    "email_text",
                    models.TextField(blank=True, default="Email", null=True),
                ),
                ("email", models.TextField(blank=True, null=True)),
                ("heading_two", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "button_name",
                    models.TextField(blank=True, default="READ MORE", null=True),
                ),
                ("button_text", models.TextField(blank=True, null=True)),
                (
                    "icon_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
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
                        related_name="emergency_contents",
                        to="emergency.emergencypage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Emergency Content",
                "verbose_name_plural": "Emergency Contents",
            },
        ),
    ]
