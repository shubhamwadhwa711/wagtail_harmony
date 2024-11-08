from django.db import models

# Create your models here.
# core/models.py

from wagtail.admin.panels import FieldPanel, MultiFieldPanel,InlinePanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey

from wagtail.fields import  StreamField
from wagtail.images.models import Image

from wagtail.models import Orderable
from wagtail.contrib.forms.models import (
    FORM_FIELD_CHOICES,
    AbstractEmailForm,
    AbstractFormField,
)



from django.template.response import TemplateResponse
##################################################################################################



class EventsPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    #show the latest event as an html
    heading = models.TextField(blank=True, null=True,default="EVENTS")
    button_text = models.TextField(blank=True, null=True,default ="Event Details")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
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
    bottom_button_text = models.TextField(blank=True, null=True,default ="Contact us")
    bottom_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [  
        FieldPanel("heading"),
        FieldPanel("button_text"),     
        FieldPanel("link_page"),
        MultiFieldPanel([
            FieldPanel('bottom_heading'),
            FieldPanel('bottom_image_one'),
            FieldPanel('bottom_image_two'),
            FieldPanel('bottom_button_text'),
            FieldPanel('bottom_link_page'),
        ], heading='Add Bottom Section'),

    ]


    parent_page_types = ['home.HomePage']
    subpage_types = [
        "events.EventPage",
    ]

    class Meta:
        verbose_name = 'Events Page'
        verbose_name_plural = 'Events Pages'



    def update_context(self,context):
        events = EventPage.objects.all()
        context.update({
            'events': events,
    
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




class EventPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    page_name = models.CharField(max_length=200,null=True,blank=True,default="EVENTS")
    heading = models.TextField(blank=True, null=True)
    event_bg_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    event_date = models.DateField(blank=True, null=True)
    event_details_heading = models.TextField(blank=True, null=True)
    event_short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    


    button_text = models.TextField(blank=True, null=True,default="Add to Calender")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    
    # event_full_description = models.TextField(blank=True, null=True)
    button_text_two = models.TextField(blank=True, null=True)
    link_page_two= models.ForeignKey(
        'wagtailcore.Page',
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
    bottom_button_text = models.TextField(blank=True, null=True,default ="Contact us")
    bottom_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("page_name"),
        FieldPanel("heading"),
        FieldPanel("event_bg_image"),
        FieldPanel("event_date"),
        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('link_page'),
        ], heading='Add Event Page Button'),
        FieldPanel("event_details_heading"),
        FieldPanel("event_short_description"),
        
        InlinePanel('event_page_images', label='Event Pages Images'),
        FieldPanel("description"),
        MultiFieldPanel([
            FieldPanel('button_text_two'),
            FieldPanel('link_page_two'),
        ], heading='Event Calender Button'),

        MultiFieldPanel([
            FieldPanel('bottom_heading'),
            FieldPanel('bottom_image_one'),
            FieldPanel('bottom_image_two'),
            FieldPanel('bottom_button_text'),
            FieldPanel('bottom_link_page'),
        ], heading='Add Bottom Section'),


    ]

    parent_page_types = ['events.EventsPage']
    subpage_types = []


    class Meta:
        verbose_name = 'Event Page'
        verbose_name_plural = 'Event Pages'


    # def update_context(self,context):
    #     events = EventPage.objects.all()
    #     context.update({
    #         'events': events,
    
    #     })
    #     return context

    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        context = self.get_context(request, *args, **kwargs)
        # context = self.update_context(default_context)
        return TemplateResponse(
            request,
            template,
            context,
        )




class  EventPageImages(Orderable):
    page = ParentalKey(
        EventPage,
        on_delete=models.CASCADE,
        related_name='event_page_images',
    )
    title = models.CharField(max_length=200,null=True,blank=True)
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
        verbose_name = 'Event Page Image'
        verbose_name_plural = 'Event Page Images'






