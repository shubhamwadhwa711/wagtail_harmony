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
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable, Page
from modelcluster.fields import ParentalKey
from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from django.template.response import TemplateResponse

class EmergencyPage(RichTextPageAbstract):
    heading = models.TextField(blank=True, null=True, default="All Emergency Services")

    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("heading"),
        
        InlinePanel("emergency_contents", label="Emergency Services Content")
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = 'Emergency Page'
        verbose_name_plural = 'Emergency Pages'



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


class EmergencyPageContent(Orderable):
    page = ParentalKey(EmergencyPage, on_delete=models.CASCADE, related_name="emergency_contents")
    service_sidebar_name = models.TextField(blank=True, null=True)
    service_name_heading = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    call_text = models.TextField(blank=True, null=True, default="Call")
    mobile_number = models.TextField(blank=True, null=True)
    email_text = models.TextField(blank=True, null=True, default="Email")
    email = models.TextField(blank=True, null=True)
    heading_two = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    button_name = models.TextField(blank=True, null=True,default="READ MORE")
    button_text = models.TextField(blank=True, null=True)
    
    panels = [
        FieldPanel("service_sidebar_name"),
        FieldPanel("service_name_heading"),
        FieldPanel("short_description"),
        MultiFieldPanel([
            FieldPanel('call_text'),
            FieldPanel('mobile_number'),
        ], heading='Add Call'),
        MultiFieldPanel([
            FieldPanel('email_text'),
            FieldPanel('email'),
        ], heading='Add Email'),
        FieldPanel("heading_two"),
        FieldPanel("description"),
        FieldPanel("image"),
        MultiFieldPanel([
            FieldPanel('button_name'),
            FieldPanel('button_text'),
        ], heading='Read More Button'),
    ]

    class Meta:
        verbose_name = 'Emergency Content'
        verbose_name_plural = 'Emergency Contents'
