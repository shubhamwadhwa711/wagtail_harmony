# Generated by Django 5.1.2 on 2024-11-13 10:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("business", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="businesspage",
            options={
                "verbose_name": "Business Development Page",
                "verbose_name_plural": "Businesses Development Pages",
            },
        ),
    ]
