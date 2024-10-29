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

class BusinessPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    business_heading =  models.TextField(blank=True, null=True)
    growth_data_text_one =  models.TextField(blank=True, null=True)
    growth_data_numbes_one =  models.TextField(blank=True, null=True)
    growth_data_text_two =  models.TextField(blank=True, null=True)
    growth_data_numbes_two =  models.TextField(blank=True, null=True)
    growth_data_text_three =  models.TextField(blank=True, null=True)
    growth_data_numbes_three =  models.TextField(blank=True, null=True)
    resource_heading = models.TextField(blank=True, null=True)
    #
    location_heading = models.TextField(blank=True, null=True)

    button_text = models.TextField(blank=True, null=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )


    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("body"),
        FieldPanel("business_heading"),
        InlinePanel('buginess_page_slide', label='Buginess Page Slide'),
        InlinePanel('buginess_page_criteria', label='Buginess Page Criteria'),

        MultiFieldPanel([
            FieldPanel('growth_data_text_one'),
            FieldPanel('growth_data_numbes_one'),
        ], heading='Growth Data One'),

        MultiFieldPanel([
            FieldPanel('growth_data_text_two'),
            FieldPanel('growth_data_numbes_two'),
        ], heading='Growth Data Two'),

        MultiFieldPanel([
            FieldPanel('growth_data_text_three'),
            FieldPanel('growth_data_numbes_three'),
        ], heading='Growth Data Two'),

        FieldPanel("resource_heading"),
        InlinePanel('buginess_page_faq', label='Buginess Page Faq'),
        FieldPanel("location_heading"),




        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('link_page'),
        ], heading='Add Assistance Button')
        

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []


    class Meta:
        verbose_name = 'Business Page'
        verbose_name_plural = 'Business Pages'



class  BusinessBGSlide(Orderable):
    page = ParentalKey(
        BusinessPage,
        on_delete=models.CASCADE,
        related_name='buginess_page_slide',
    )

    title = models.TextField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('heading'),
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = 'Business Slide'
        verbose_name_plural = 'Business Slides'


class  CriteriaType(Orderable):
    page = ParentalKey(
        BusinessPage,
        on_delete=models.CASCADE,
        related_name='buginess_page_criteria',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    heading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
   
    panels = [
        FieldPanel('heading'),
        FieldPanel('image'),
        FieldPanel('description'),
    ]
    class Meta:
        verbose_name = 'Criteria Type'
        verbose_name_plural = 'Criteria Types'




class  BusinessFaq(Orderable):
    page = ParentalKey(
        BusinessPage,
        on_delete=models.CASCADE,
        related_name='buginess_page_faq',
    )
    heading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
   
    panels = [
        FieldPanel('heading'),
        FieldPanel('description'),
    ]

    class Meta:
        verbose_name = 'Business Faq'
        verbose_name_plural = 'Business Faqs'






