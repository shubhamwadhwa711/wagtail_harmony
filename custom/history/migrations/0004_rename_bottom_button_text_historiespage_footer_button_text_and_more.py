# Generated by Django 5.1.2 on 2024-11-27 04:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0003_historypage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="historiespage",
            old_name="bottom_button_text",
            new_name="footer_button_text",
        ),
        migrations.RenameField(
            model_name="historiespage",
            old_name="bottom_heading",
            new_name="footer_heading",
        ),
        migrations.RenameField(
            model_name="historiespage",
            old_name="bottom_link_page",
            new_name="footer_link_page",
        ),
    ]