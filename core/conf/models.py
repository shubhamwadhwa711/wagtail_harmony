from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)
from django.db import models

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel

from .blocks import DropdownElement, NavigationElement

from wagtail.fields import StreamField

@register_setting
class NavigationSettings(BaseSiteSetting):
    favicon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    footer_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    footer_seal = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    hamburger = StreamField(
        [
            ("element", NavigationElement()),
            ("dropdown", DropdownElement()),
        ],
        blank=True,
        null=True,
        use_json_field=True,
    )
    footer = StreamField(
        [("element", NavigationElement())], blank=True, null=True, use_json_field=True
    )

    class Meta:
        verbose_name = "Navigation"
        verbose_name_plural = "Navigation"
