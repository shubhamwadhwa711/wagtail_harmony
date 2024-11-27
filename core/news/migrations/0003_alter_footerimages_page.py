# Generated by Django 5.1.2 on 2024-11-27 08:00

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_rename_bottom_link_page_newspage_footer_link_page_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footerimages",
            name="page",
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="page_footer_images",
                to="news.newspage",
            ),
        ),
    ]
