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
        # InlinePanel('land_spot_info', label='Add Land Spot Info'),
        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('link_page'),
        ], heading='Add Assistance Button')
        ]
    
    parent_page_types = ['home.HomePage']
    subpage_types = ["land.SingleLandFeaturedDetails"]


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




class SingleLandFeaturedDetails(RichTextPageAbstract):
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
    yard = models.TextField(blank=True, null=True)
    size  = models.TextField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    land_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
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
        FieldPanel("location_image"),
        FieldPanel("plan_text"),
        FieldPanel("yard"),
        FieldPanel("size"),
        FieldPanel("heading"),
        FieldPanel("land_image"),
        FieldPanel("description"),
        FieldPanel("main_image"),
        InlinePanel('single_page_feature_images', label='Single Page Feature Images')

    ]

    parent_page_types = ['land.LandPage']
    subpage_types = []
    class Meta:
        verbose_name = 'Singel Feature Page'
        verbose_name_plural = 'Single Feature Pages'



    def update_context(self,context):
        lands = LandPage.objects.all()
        singlelands = SingleLandFeaturedDetails.objects.all()[:4]
        context.update({
            'lands': lands,
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


class  SinglePageFeaturedDetailPageImages(Orderable):
    page = ParentalKey(
        SingleLandFeaturedDetails,
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