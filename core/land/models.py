from django.db import models

# Create your models here.
# core/models.py

from wagtail.admin.panels import FieldPanel, MultiFieldPanel,InlinePanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable, Site
from modelcluster.fields import ParentalKey
from wagtail.fields import  StreamField
from wagtail.models import Orderable
from django.template.response import TemplateResponse

##################################################################################################

class LandPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    heading  =models.TextField(null=True,blank=True)
    button_text = models.TextField(blank=True, null=True,default="Get Assistance")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("heading"),
        InlinePanel('land_spot_feature', label='Add Land Spot Feature'),
        InlinePanel('land_spot_info', label='Add Land Spot Info'),
        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('link_page'),
        ], heading='Add Assistance Button')
        ]
    
    parent_page_types = ['home.HomePage']
    subpage_types = []


    class Meta:
        verbose_name = 'Lands Index Page'
        verbose_name_plural = 'Lands  Index Pages'


    

class  Spotfeature(Orderable):
    page = ParentalKey(
        LandPage,
        on_delete=models.CASCADE,
        related_name='land_spot_feature',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    text = models.CharField(max_length=200,blank=True, null=True)

    panels = [
        FieldPanel('text'),
        FieldPanel('image')
     
    ]
    class Meta:
        verbose_name = 'Spot feature'
        verbose_name_plural = 'Spot features'


class  LandSpot(Orderable):
    page = ParentalKey(
        LandPage,
        on_delete=models.CASCADE,
        related_name='land_spot_info',
    )
    title = models.CharField(max_length=50,blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = 'Land Spot Slide'
        verbose_name_plural = 'Land Spots Slides'


