# Generated by Django 5.1.2 on 2024-11-27 09:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("business", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="businesspage",
            name="growth_data_number_one",
        ),
        migrations.RemoveField(
            model_name="businesspage",
            name="growth_data_number_three",
        ),
        migrations.RemoveField(
            model_name="businesspage",
            name="growth_data_number_two",
        ),
        migrations.RemoveField(
            model_name="businesspage",
            name="growth_data_text_one",
        ),
        migrations.RemoveField(
            model_name="businesspage",
            name="growth_data_text_three",
        ),
        migrations.RemoveField(
            model_name="businesspage",
            name="growth_data_text_two",
        ),
    ]