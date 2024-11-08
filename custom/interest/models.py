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
from django.template.response import TemplateResponse


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
    text =models.TextField(blank=True, null=True,default="Drop the pin to see location")
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
        null=True,
        blank=False
    )

    bottom_heading = models.TextField(blank=True, null=True)
    bottom_image_one = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    bottom_image_two = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    bottom_button_text = models.TextField(blank=True, null=True,default ="Submit your photo")
    bottom_link_page = models.ForeignKey(
        'wagtailcore.Page',
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
            FieldPanel('bottom_heading'),
            FieldPanel('bottom_image_one'),
            FieldPanel('bottom_image_two'),
            FieldPanel('bottom_button_text'),
            FieldPanel('bottom_link_page'),
        ], heading='Add Bottom Section'),
    ]
    parent_page_types = ['home.HomePage']
    subpage_types = ["interest.SinglePointsOfInterest"]
    class Meta:
        verbose_name = 'Points Of Interest Page'
        verbose_name_plural = 'Points Of Interest Pages'


    def update_context(self,context):
        interests = SinglePointsOfInterest.objects.all()
        context.update({
            'interests': interests,
            'all_categories': CategoryEnum.choices(),
    
        })
        return context

    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        default_context = self.get_context(request, *args, **kwargs)
        context = self.update_context(default_context)
       
        return TemplateResponse(
            request,
            template,
            context,
        )



class SinglePointsOfInterest(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    text =models.TextField(blank=True, null=True,default="Drop the pin to see location")
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
    back_button_text = models.TextField(blank=True, null=True,default="Back to Points of Interest")
    single_point_heading = models.TextField(blank=True, null=True)
    single_point_description = models.TextField(blank=True, null=True)
    single_point_description_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    single_land_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )


    bottom_heading = models.TextField(blank=True, null=True)
    bottom_image_one = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    bottom_image_two = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    bottom_button_text = models.TextField(blank=True, null=True,default ="Submit your photo")
    bottom_link_page = models.ForeignKey(
        'wagtailcore.Page',
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
        FieldPanel("single_land_image"),
        InlinePanel("single_page_point_images", label="Single Page Point Images"),
        MultiFieldPanel([
            FieldPanel('bottom_heading'),
            FieldPanel('bottom_image_one'),
            FieldPanel('bottom_image_two'),
            FieldPanel('bottom_button_text'),
            FieldPanel('bottom_link_page'),
        ], heading='Add Bottom Section'),

    ]

    parent_page_types = ['interest.PointsOfInterest']
    subpage_types = []
    class Meta:
        verbose_name = 'Single Points Of Interest Page'
        verbose_name_plural = 'Single Points Of Interest Pages'

    
    def update_context(self,context):
        context.update({
            'all_categories': CategoryEnum.choices(),
    
        })
        return context

    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        default_context = self.get_context(request, *args, **kwargs)
        context = self.update_context(default_context)
       
        return TemplateResponse(
            request,
            template,
            context,
        )



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
    land_location_text =models.TextField(blank=True, null=True,default="Land Drop the pin to see location")
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