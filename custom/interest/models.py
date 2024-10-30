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
from enum import Enum


class CategoryEnum(Enum):
    SCHOOLS = 'schools'
    PARKS = 'parks'
    TOWN_HALL = 'town_hall'
    PARKING_STREETS = 'parking_streets'

    @classmethod
    def choices(cls):
        return [(tag.value, tag.name.replace("_", " ").title()) for tag in cls]



class PointsOfInterest(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    text =models.TextField(blank=True, null=True,default="Land Location")
    small_land_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    interest_heading = models.TextField(blank=True, null=True)
    interest_description = models.TextField(blank=True, null=True)
    interest_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    category = models.CharField(
        max_length=50,
        choices=CategoryEnum.choices(),
        default=CategoryEnum.SCHOOLS.value,
        blank=True
    )
    
    content_panels = RichTextPageAbstract.content_panels + [
        
        FieldPanel("text"),
        FieldPanel("small_land_image"),
        FieldPanel("category"),
        MultiFieldPanel([
            FieldPanel('interest_heading'),
            FieldPanel('interest_description'),
            FieldPanel('interest_image'),
        ], heading='Add Interest Data '),

    ]
    parent_page_types = ['home.HomePage']
    subpage_types = []
    class Meta:
        verbose_name = 'Points Of Interest Page'
        verbose_name_plural = 'Points Of Interest Pages'






class SinglePointsOfInterest(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    text =models.TextField(blank=True, null=True,default="Land Location")
    small_land_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    category = models.CharField(
        max_length=50,
        choices=CategoryEnum.choices(),
        default=CategoryEnum.SCHOOLS.value,
        blank=True
    )
    back_button_text = models.TextField(blank=True, null=True)
    single_point_heading = models.TextField(blank=True, null=True)
    single_point_description = models.TextField(blank=True, null=True)
    single_point_description_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        
        FieldPanel("text"),
        FieldPanel("small_land_image"),
        FieldPanel("category"),
        MultiFieldPanel([
            FieldPanel('single_point_heading'),
            FieldPanel('single_point_description'),
            FieldPanel('single_point_description_image'),
        ], heading='Add Single Point Description Data '),
        InlinePanel("single_page_point_images", label="Single Page Point Images")

    ]

    parent_page_types = ['interest.PointsOfInterest']
    subpage_types = []
    class Meta:
        verbose_name = 'Single Points Of Interest Page'
        verbose_name_plural = 'Single Points Of Interest Pages'





class  SinglePointPageImages(Orderable):
    page = ParentalKey(
        SinglePointsOfInterest,
        on_delete=models.CASCADE,
        related_name='single_page_point_images',
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
        verbose_name = 'Single Point Page Image'
        verbose_name_plural = 'Single Point Page  Images'

















class SinglePageFeaturedDetail(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    land_location_text =models.TextField(blank=True, null=True,default="Land Location")
    small_land_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    plan_text =models.TextField(blank=True, null=True,default="Plan details") 
    yard = models.TextField(blank=True, null=True)
    size  = models.TextField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    #images
    description = models.TextField(blank=True, null=True)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    


    content_panels = RichTextPageAbstract.content_panels + [
        
        FieldPanel("land_location_text"),
        FieldPanel("small_land_image"),
        FieldPanel("plan_text"),
        FieldPanel("yard"),
        FieldPanel("size"),
        FieldPanel("heading"),
        FieldPanel("description"),
        FieldPanel("main_image"),
        InlinePanel('single_page_feature_images', label='Single Page Feature Images')

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []
    class Meta:
        verbose_name = 'Interest Page'
        verbose_name_plural = 'Interest Pages'

class  SinglePageFeaturedDetailPageImages(Orderable):
    page = ParentalKey(
        SinglePageFeaturedDetail,
        on_delete=models.CASCADE,
        related_name='single_page_feature_images',
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
        verbose_name = 'Single Page Featured Detail  Image'
        verbose_name_plural = 'Single Page Featured Detail Images'