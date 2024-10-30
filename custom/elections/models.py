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





class ElectionsPage(RichTextPageAbstract):
    notice_text = models.TextField(blank=True, null=True)
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
 
    heading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    heading_one = models.TextField(blank=True, null=True)
    sub_heading_one = models.TextField(blank=True, null=True)
    button_text_one = models.TextField(blank=True, null=True,default="Run for Position")
    link_page_one = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    heading_two =  models.TextField(blank=True, null=True)
    button_text_two = models.TextField(blank=True, null=True,default="Get on Ballot")
    link_page_two = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
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
        FieldPanel("heading_two"),
        MultiFieldPanel([
            FieldPanel('button_text_two'),
            FieldPanel('link_page_two'),
        ], heading='Add Ballot Page '),

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ["elections.SingleElectionPage"]

    class Meta:
        verbose_name = 'Election Pages'
        verbose_name_plural = 'Election Pages'



class SingleElectionPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    heading = models.TextField(blank=True, null=True)
    party_name =  models.TextField(blank=True, null=True)
    position_title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    result_declare_heading = models.TextField(blank=True, null=True)

    parent_page_types = ['elections.ElectionsPage']
    subpage_types = []
    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("heading"),
        FieldPanel("party_name"),
        FieldPanel("position_title"),
        FieldPanel("description"),
        FieldPanel("result_declare_heading"),
        InlinePanel('election_page_person', label='Election Page Person'),
    ]


    parent_page_types = ['home.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = 'SingleElectionPage'
        verbose_name_plural = 'Single Election Page'
    

class  ElectionPagePerson(Orderable):
    page = ParentalKey(
        SingleElectionPage,
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






