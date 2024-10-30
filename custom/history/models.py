from django.db import models

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

class HistoriesPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    search = models.TextField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True,default="History of Harmony")
    short_heading = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    content_panels = RichTextPageAbstract.content_panels + [

        FieldPanel("heading"),
        FieldPanel("short_heading"),
        FieldPanel("short_description"),

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ["history.HistoryPage"]


    class Meta:
        verbose_name = 'Histories Page'
        verbose_name_plural = 'Histories Pages'



class  HistoryPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    date = models.DateField(blank=True, null=True)
    content_short_description = models.TextField(blank=True, null=True)
    content_full_description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel('date'),
        FieldPanel('image'),
        FieldPanel('content_short_description'),
        FieldPanel('content_full_description'),
    ]

    parent_page_types = ['history.HistoriesPage']
    subpage_types = []

    class Meta:
        verbose_name = 'History Page Content'
        verbose_name_plural = 'History Page Contents'







