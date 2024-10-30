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
from wagtail.images.models import Image
from wagtail.blocks import RichTextBlock
from wagtail.models import Orderable

##################################################################################################

class ElectionPage(RichTextPageAbstract):
    notice_text = models.TextField(blank=True, null=True)
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    # title = models.TextField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    heading_one = models.TextField(blank=True, null=True)
    sub_heading_one = models.TextField(blank=True, null=True)


    # event_date = models.DateField(blank=True, null=True)

    button_text_one = models.TextField(blank=True, null=True)
    link_page_one = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    heading_two =  models.TextField(blank=True, null=True)


    button_text_two = models.TextField(blank=True, null=True)
    link_page_two = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )


    # event_short_heading = models.TextField(blank=True, null=True)
    # event_short_description = models.TextField(blank=True, null=True)
    # event_full_description = models.TextField(blank=True, null=True)

    # button_text_two = models.TextField(blank=True, null=True)
    # link_page_two= models.ForeignKey(
    #     'wagtailcore.Page',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     blank=True,
    #     null=True,
    # )

    content_panels = RichTextPageAbstract.content_panels + [
        
        FieldPanel("notice_text"),
        
        FieldPanel("heading"),
        FieldPanel("description"),
        FieldPanel("heading_one"),
        FieldPanel("sub_heading_one"),
    
        MultiFieldPanel([
            FieldPanel('button_text_one'),
            FieldPanel('link_page_one'),
        ], heading='Add Position  Button Page'),

       
        InlinePanel('election_page_person', label='Election Page Person'),
        FieldPanel("heading_two"),

        MultiFieldPanel([
            FieldPanel('button_text_two'),
            FieldPanel('link_page_two'),
        ], heading='Add Ballot Page '),

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = 'Election Page'
        verbose_name_plural = 'Elections Page'



class  ElectionPagePerson(Orderable):
   
    page = ParentalKey(
        ElectionPage,
        on_delete=models.CASCADE,
        related_name='election_page_person',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    name =  models.TextField(blank=True, null=True)
    designation =  models.TextField(blank=True, null=True)
    description =  models.TextField(blank=True, null=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('name'),
        FieldPanel('designation'),
        FieldPanel('description'),
    ]
    class Meta:
        verbose_name = 'Election Page Person'
        verbose_name_plural = 'Election Page Persons'






