# Generated by Django 5.1.2 on 2024-10-28 07:58

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_homepage_county_text_homepage_heading_text_and_more"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="homepagelinks",
            options={
                "verbose_name": "Home Page Link",
                "verbose_name_plural": "Home Page Links",
            },
        ),
        migrations.AddField(
            model_name="homepage",
            name="history_heading",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="history_link_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="history_page_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="history_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="team_heading",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="team_link_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="team_page_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="team_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="TeamMember",
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
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("designation", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_member",
                        to="home.homepage",
                    ),
                ),
                (
                    "team_member_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Team Member",
                "verbose_name_plural": "Team Members",
            },
        ),
    ]
