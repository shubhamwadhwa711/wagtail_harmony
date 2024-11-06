from django.db import models

# Create your models here.
# core/models.py

from wagtail.admin.panels import FieldPanel, MultiFieldPanel,InlinePanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey

from wagtail.fields import  StreamField
from wagtail.images.models import Image

from wagtail.models import Orderable
from wagtail.contrib.forms.models import (
    FORM_FIELD_CHOICES,
    AbstractEmailForm,
    AbstractFormField,
)

##################################################################################################



class EventsPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    #show the latest event as an html

    heading = models.TextField(blank=True, null=True,default="EVENTS")
    content_panels = RichTextPageAbstract.content_panels + [       

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        "events.EventPage",
    ]

    class Meta:
        verbose_name = 'Events Page'
        verbose_name_plural = 'Events Pages'





class EventPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    page_name = models.CharField(max_length=200,null=True,blank=True,default="EVENTS")
    heading = models.TextField(blank=True, null=True)
    event_bg_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )


    description = models.TextField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)

    button_text = models.TextField(blank=True, null=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    event_short_heading = models.TextField(blank=True, null=True)
    event_short_description = models.TextField(blank=True, null=True)
    event_full_description = models.TextField(blank=True, null=True)

    button_text_two = models.TextField(blank=True, null=True)
    link_page_two= models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        
        FieldPanel("heading"),
        FieldPanel("event_bg_image"),
        # FieldPanel("description"),
        FieldPanel("event_date"),
        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('link_page'),
        ], heading='Add Event Page Button'),
        FieldPanel("event_short_heading"),
        FieldPanel("event_short_description"),
        InlinePanel('event_page_images', label='Event Pages Images'),
        FieldPanel("event_full_description"),
        MultiFieldPanel([
            FieldPanel('button_text_two'),
            FieldPanel('link_page_two'),
        ], heading='Buttom Add Event Page Button'),

    ]

    parent_page_types = ['events.EventsPage']
    subpage_types = []


    class Meta:
        verbose_name = 'Event Page'
        verbose_name_plural = 'Event Pages'



class  EventPageImages(Orderable):
    page = ParentalKey(
        EventPage,
        on_delete=models.CASCADE,
        related_name='event_page_images',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    panels = [
        FieldPanel('image'),
    ]
    class Meta:
        verbose_name = 'Event Page Image'
        verbose_name_plural = 'Event Page Images'






