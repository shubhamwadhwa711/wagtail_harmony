from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)
from django.db import models
from .blocks import  NavigationElement,FooterSection,  SocialSection
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
    header_logo_page_link = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=False,
        null=True,
    )

    footer_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    footer_logo_page_link = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=False,
        null=True,
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
            # ("dropdown", DropdownElement()),
        ],
        blank=True,
        null=True,
        use_json_field=True,
    )
    
    footer = StreamField(
        [("element", FooterSection())], blank=True, null=True, use_json_field=True
    )

    social_link = StreamField(
        [("element", SocialSection())], blank=True, null=True, use_json_field=True
    )

  

    office_address = models.CharField(max_length=200,blank=True, null=True)
    phone_number = models.CharField(max_length=200,blank=True, null=True)



    class Meta:
        verbose_name = "Navigation"
        verbose_name_plural = "Navigation"
