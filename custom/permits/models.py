from django.db import models

# Create your models here.

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





class PermitsPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    #show the latest event as an html

    heading = models.TextField(blank=True, null=True,default="Permits")
    content_panels = RichTextPageAbstract.content_panels + [   
        FieldPanel("heading"),
            
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        "permits.PermitPage",
    ]

    class Meta:
        verbose_name = 'Permits Page'
        verbose_name_plural = 'Permits Pages'




class PermitPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    heading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("heading"),
        FieldPanel("description"),
    ]

    parent_page_types = ['permits.PermitsPage']
    subpage_types = []


    class Meta:
        verbose_name = 'Permit Page'
        verbose_name_plural = 'Permit Pages'


