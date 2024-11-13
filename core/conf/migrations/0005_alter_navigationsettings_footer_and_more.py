# Generated by Django 5.1.2 on 2024-11-13 11:48

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("conf", "0004_alter_navigationsettings_footer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navigationsettings",
            name="footer",
            field=wagtail.fields.StreamField(
                [("element", 6)],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.images.blocks.ImageChooserBlock",
                        (),
                        {"required": False},
                    ),
                    1: ("wagtail.blocks.CharBlock", (), {}),
                    2: ("wagtail.blocks.PageChooserBlock", (), {"required": False}),
                    3: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "URL", "required": False},
                    ),
                    4: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 1), ("page", 2), ("url", 3)]],
                        {},
                    ),
                    5: (
                        "wagtail.blocks.StreamBlock",
                        [[("navpages", 4)]],
                        {"required": False},
                    ),
                    6: (
                        "wagtail.blocks.StructBlock",
                        [[("icon_image", 0), ("category", 1), ("children", 5)]],
                        {},
                    ),
                },
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="navigationsettings",
            name="hamburger",
            field=wagtail.fields.StreamField(
                [("element", 6), ("dropdown", 8)],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.images.blocks.ImageChooserBlock",
                        (),
                        {"required": False},
                    ),
                    1: ("wagtail.blocks.CharBlock", (), {}),
                    2: ("wagtail.blocks.PageChooserBlock", (), {"required": False}),
                    3: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "URL", "required": False},
                    ),
                    4: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 1), ("page", 2), ("url", 3)]],
                        {},
                    ),
                    5: (
                        "wagtail.blocks.StreamBlock",
                        [[("navpages", 4)]],
                        {"required": False},
                    ),
                    6: (
                        "wagtail.blocks.StructBlock",
                        [[("icon_image", 0), ("category", 1), ("children", 5)]],
                        {},
                    ),
                    7: (
                        "wagtail.blocks.StreamBlock",
                        [[("element", 6)]],
                        {"required": False},
                    ),
                    8: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 1), ("children", 7)]],
                        {},
                    ),
                },
                null=True,
            ),
        ),
    ]
