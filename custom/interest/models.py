from django.db import models

# Create your models here.
# core/models.py

from wagtail.admin.panels import FieldPanel, MultiFieldPanel,InlinePanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from modelcluster.fields import ParentalKey
from wagtail.fields import StreamField
from wagtail.models import Orderable
from django.template.response import TemplateResponse
from taggit.models import  TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager


class PointsOfInterest(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    text =models.TextField(blank=True, null=True,default="Drop the pin to see location")

    footer_heading = models.TextField(blank=True, null=True,default="Submit your fun photo at any point of interested")
    footer_button_text = models.TextField(blank=True, null=True,default ="Share Story")
    footer_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        
        FieldPanel("text"),
        # FieldPanel("small_land_image"),
        # FieldPanel("category"),
     
        MultiFieldPanel([
            FieldPanel('footer_heading'),
            FieldPanel('footer_button_text'),
            FieldPanel('footer_link_page'),
            InlinePanel('page_footer_images', label='Footer Images'),
        ], heading='Add Bottom Section'),
    ]
    parent_page_types = ['home.HomePage']
    subpage_types = ["interest.SinglePointsOfInterest"]
    class Meta:
        verbose_name = 'Points Of Interest Page'
        verbose_name_plural = 'Points Of Interest Pages'


    def update_context(self,context,request):
        # interests = SinglePointsOfInterest.objects.all()
        selected_tag = request.GET.get('tag')
        if selected_tag:
            interests = SinglePointsOfInterest.objects.filter(tags__name__iexact=selected_tag).distinct()
        else:
            interests = SinglePointsOfInterest.objects.all()
        context.update({
            "interests": interests,
            "tags":  SinglePointsOfInterest.tags.all() 
        })
        return context

    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        default_context = self.get_context(request, *args, **kwargs)
        context = self.update_context(default_context,request)
       
        return TemplateResponse(
            request,
            template,
            context,
        )


class  Footerimages(Orderable):
    page = ParentalKey(
        PointsOfInterest,
        on_delete=models.CASCADE,
        related_name='page_footer_images',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel('image')    
    ]
    


class InterestTags(TaggedItemBase):
    content_object = ParentalKey(
        "SinglePointsOfInterest", on_delete=models.CASCADE, related_name="tagged_items"
    )

                   
class SinglePointsOfInterest(RichTextPageAbstract):
    tags = ClusterTaggableManager(through=InterestTags, blank=True)
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


    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("text"),
        FieldPanel("small_land_image"),
        FieldPanel('tags'),

        MultiFieldPanel([
            FieldPanel('single_point_heading'),
            FieldPanel('single_point_description'),
            FieldPanel('single_point_description_image'),
        ], heading='Add Single Point Description Data '),
        InlinePanel("single_page_point_images", label="Single Page Point Images"),
    
    ]

    parent_page_types = ['interest.PointsOfInterest']
    subpage_types = []
    class Meta:
        verbose_name = 'Single Points Of Interest Page'
        verbose_name_plural = 'Single Points Of Interest Pages'

    def update_context(self,context,request):
        context.update({
            "tags":  SinglePointsOfInterest.tags.all() ,
            "is_child" : True if   self.get_parent()  else False
            

        })
        return context
    
    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        default_context = self.get_context(request, *args, **kwargs)
        context = self.update_context(default_context,request)
       
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


