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

class HistoryPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    heading = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    content_panels = RichTextPageAbstract.content_panels + [
        
        FieldPanel("heading"),
        FieldPanel("short_description"),
        FieldPanel("full_description"),
        InlinePanel('history_page_content', label='Event Pages Images'),
   

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []


    class Meta:
        verbose_name = 'History Page'
        verbose_name_plural = 'History Pages'






class  HistoryPageContent(Orderable):
    date = models.DateField(blank=True, null=True)
    page = ParentalKey(
        HistoryPage,
        on_delete=models.CASCADE,
        related_name='history_page_content',
    )
    content_short_description = models.TextField(blank=True, null=True)
    content_full_description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    panels = [
        FieldPanel('date'),
        FieldPanel('image'),
        FieldPanel('content_short_description'),
        FieldPanel('content_full_description'),
    ]
    class Meta:
        verbose_name = 'History Page Content'
        verbose_name_plural = 'History Page Contents'







