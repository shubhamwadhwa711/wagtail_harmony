# Generated by Django 5.1.2 on 2024-11-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0002_rename_bottom_link_page_eventspage_footer_link_page_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventspage",
            name="footer_heading",
            field=models.TextField(
                blank=True, default="Do you want to hold an even in Harmony?", null=True
            ),
        ),
    ]
