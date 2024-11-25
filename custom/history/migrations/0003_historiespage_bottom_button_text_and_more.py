# Generated by Django 5.1.2 on 2024-11-25 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0002_remove_historiespage_bottom_button_text_and_more"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="historiespage",
            name="bottom_button_text",
            field=models.TextField(blank=True, default="Share Story", null=True),
        ),
        migrations.AddField(
            model_name="historiespage",
            name="bottom_heading",
            field=models.TextField(
                blank=True, default="Share your story about Harmony", null=True
            ),
        ),
        migrations.AddField(
            model_name="historiespage",
            name="bottom_image_one",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="historiespage",
            name="bottom_image_two",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="historiespage",
            name="bottom_link_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
    ]