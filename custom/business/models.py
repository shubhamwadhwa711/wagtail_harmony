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
# from  core.land.models import LandPage


class BusinessPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    business_heading =  models.TextField(blank=True, null=True,default="Why do Business in harmony")
    resource_heading = models.TextField(blank=True, null=True,default="Helpful Resources")
    feature_heading= models.TextField(blank=True, null=True,default="We found out the best spot for you to make money out of this land")
    feature_button_text = models.TextField(blank=True, null=True,default ="Share Story")
    feature_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )


    content_panels = RichTextPageAbstract.content_panels + [
        InlinePanel('buginess_page_slide', label='Buginess Page Slide'),
     
        MultiFieldPanel([
            FieldPanel('business_heading'),
            InlinePanel('buginess_page_criteria', label='Buginess Page Criteria'),
        ], heading='Page Criteria'),
        InlinePanel('buginess_growth', label='Buginess growth'),

       
        MultiFieldPanel([
            FieldPanel('resource_heading'),
            InlinePanel('buginess_page_faq', label='Buginess Page Faq'),
        ], heading='Buginess Faq'),

        MultiFieldPanel([
            FieldPanel('feature_heading'),
            FieldPanel('feature_button_text'),
            FieldPanel('feature_link_page'),
           

            InlinePanel('land_features_list', label='Land features List'),
        ], heading='Add Bottom Section'),

    ]
    parent_page_types = ['home.HomePage']
    subpage_types = ['business.SingleLandFeature']
    class Meta:
        verbose_name = 'Business Development Page'
        verbose_name_plural = 'Businesses Development Pages'
   

    def update_context(self,context):
        
        singlelands = SingleLandFeature.objects.all()
        context.update({
          
            'singlelands': singlelands
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
    

class  Growth(Orderable):
    page = ParentalKey(
        BusinessPage,
        on_delete=models.CASCADE,
        related_name='buginess_growth',
    )

    text = models.CharField(max_length=200, null=True,blank=True)
    number = models.CharField(max_length=200, null=True,blank=True)
    unit = models.CharField(max_length=200, null=True,blank=True)
 
    panels = [
        FieldPanel('text'),
        FieldPanel('number'),
        FieldPanel('unit'),
     
    ]




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


class  LandFreatures(Orderable):
    page = ParentalKey(
        BusinessPage,
        on_delete=models.CASCADE,
        related_name='land_features_list',
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
   
 

class SingleLandFeature(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    land_location_text =models.TextField(blank=True, null=True,default="Land Location")
    location_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    plan_text =models.TextField(blank=True, null=True,default="Plan details") 
  
    heading = models.TextField(blank=True, null=True)
    
    description = models.TextField(blank=True, null=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    
    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("land_location_text"),
        FieldPanel("location_image"),
        FieldPanel("plan_text"),
        InlinePanel('land_properties', label='Land Properties'),
        FieldPanel("heading"),
        InlinePanel('feature_land_images', label='Feature Page Images'),
        FieldPanel("description"),
        FieldPanel("featured_image"),

    ]

    parent_page_types = ['business.BusinessPage']
    subpage_types = []
    class Meta:
        verbose_name = 'Singel Feature Page'
        verbose_name_plural = 'Single Feature Pages'
    def update_context(self,context):
        singlelands = SingleLandFeature.objects.all()[:4]
        context.update({
           
            'singlelands': singlelands
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


class LandProperties(Orderable):
    page = ParentalKey(
        SingleLandFeature,
        on_delete=models.CASCADE,
        related_name='land_properties',
    )
    text = models.CharField(max_length=200,null=True,blank=True)
    panels = [
        FieldPanel('text'),
    ]


class  LandImages(Orderable):
    page = ParentalKey(
        SingleLandFeature,
        on_delete=models.CASCADE,
        related_name='feature_land_images',
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
