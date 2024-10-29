from django.db import models

# Create your models here.
# core/models.py

from wagtail.admin.panels import FieldPanel, MultiFieldPanel,StreamValue,InlinePanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable, Site
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable, Page
from modelcluster.fields import ParentalKey
from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks

class EmergencyPage(RichTextPageAbstract):
    heading = models.TextField(blank=True, null=True, default="All Emergency Services")

    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("heading"),
        FieldPanel("body"),
        InlinePanel("emergency_contents", label="Emergency Services Content")
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = 'Emergency Page'
        verbose_name_plural = 'Emergency Pages'


class EmergencyPageContent(Orderable):
    page = ParentalKey(EmergencyPage, on_delete=models.CASCADE, related_name="emergency_contents")
    name = models.TextField(blank=True, null=True, default="All Emergency Services")
    short_description = models.TextField(blank=True, null=True, default="All Emergency Services")
    call_text = models.TextField(blank=True, null=True, default="Call")
    mobile_number = models.TextField(blank=True, null=True)
    email_text = models.TextField(blank=True, null=True, default="Email")
    email = models.TextField(blank=True, null=True)
    heading_two = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    button_name = models.TextField(blank=True, null=True)
    button_text = models.TextField(blank=True, null=True)
    
    panels = [
        FieldPanel("name"),
        FieldPanel("short_description"),
        MultiFieldPanel([
            FieldPanel('call_text'),
            FieldPanel('mobile_number'),
        ], heading='Add Call'),
        MultiFieldPanel([
            FieldPanel('email_text'),
            FieldPanel('email'),
        ], heading='Add Email'),
        FieldPanel("heading_two"),
        FieldPanel("description"),
        FieldPanel("image"),
        MultiFieldPanel([
            FieldPanel('button_name'),
            FieldPanel('button_text'),
        ], heading='Read More Button'),
    ]

    class Meta:
        verbose_name = 'Emergency Content'
        verbose_name_plural = 'Emergency Contents'


# class EmergencyPage(RichTextPageAbstract):
#     body = StreamField(
#         richtext_blocks,
#         use_json_field=True,
#         blank=True,
#     )
#     heading = models.TextField(blank=True, null=True,default="All Emergency Services")
#     name = models.TextField(blank=True, null=True,default="All Emergency Services")
#     content_panels = RichTextPageAbstract.content_panels + [
#         FieldPanel("body"),
#         FieldPanel("heading"),
#         FieldPanel("name"),
     

#     ]

#     parent_page_types = ['home.HomePage']
#     subpage_types = []


#     class Meta:
#         verbose_name = 'Emergency Page'
#         verbose_name_plural = 'Emergency Pages'






# class EmergencyPageContent(RichTextPageAbstract):
#     body = StreamField(
#         richtext_blocks,
#         use_json_field=True,
#         blank=True,
#     )
#     name = models.TextField(blank=True, null=True,default="All Emergency Services")
#     short_description = models.TextField(blank=True, null=True,default="All Emergency Services")

#     call_text = models.TextField(blank=True, null=True,default="Call")
#     mobile_number = models.TextField(blank=True, null=True)
#     email_text = models.TextField(blank=True, null=True,default="Email")
#     email = models.TextField(blank=True, null=True)
#     heading_two = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         on_delete=models.SET_NULL,
#         related_name='+',
#         blank=True,
#         null=True,
#     )

#     button_name = models.TextField(blank=True, null=True)
#     button_text = models.TextField(blank=True, null=True)
    

#     content_panels = RichTextPageAbstract.content_panels + [
#         FieldPanel("body"),
#         FieldPanel("name"),
#         FieldPanel("short_description"),
#         MultiFieldPanel([
#             FieldPanel('call_text'),
#             FieldPanel('mobile_number'),
#         ], heading='Add Call'),

#         MultiFieldPanel([
#             FieldPanel('email_text'),
#             FieldPanel('email'),
#         ], heading='Add Email'),
#         FieldPanel("heading_two"),
#         FieldPanel("description"),
#         FieldPanel("image"),

#         MultiFieldPanel([
#             FieldPanel('button_name'),
#             FieldPanel('button_text'),
#         ], heading='Read More Button'),

#     ]

#     parent_page_types = ['home.HomePage']
#     subpage_types = []


#     class Meta:
#         verbose_name = 'Emergency contenet Page'
#         verbose_name_plural = 'Emergency content Pages'
