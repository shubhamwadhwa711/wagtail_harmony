from django.db import models

# Create your models here.
# core/models.py

from wagtail.admin.panels import FieldPanel, MultiFieldPanel,StreamValue,InlinePanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable, Site
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable
from django.template.response import TemplateResponse

##################################################################################################

class OurteamPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    name  =  models.TextField(blank=True, null=True,default="TOWN OFFICIALS")

    heading =  models.TextField(blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    sub_heading_one =  models.TextField(blank=True, null=True,default="Elected Officials")
    sub_heading_two =  models.TextField(blank=True, null=True,default="Volunteers / Support Staff")
    apply_heading =  models.TextField(blank=True, null=True,default="Become an elected Harmony official")
    button_text = models.TextField(blank=True, null=True,default="Apply Now")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    content_panels = RichTextPageAbstract.content_panels + [
        
        FieldPanel("name"),
        FieldPanel("heading"),
        FieldPanel("description"),
        FieldPanel("sub_heading_one"),
        FieldPanel("sub_heading_two"),
        FieldPanel("apply_heading"),
        InlinePanel('ourteam_page_person', label='Buginess Page Slide'),
        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('link_page'),
        ], heading='Add Assistance Button')
        

    ]
    parent_page_types = ['home.HomePage']
    subpage_types = []


    class Meta:
        verbose_name = 'Ourteam Page'
        verbose_name_plural = 'Ourteam Pages'

    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        context = self.get_context(request, *args, **kwargs)
        return TemplateResponse(
            request,
            template,
            context,
        )





class  OurteamPagePerson(Orderable):
    ROLE_CHOICES = [
        ('elected_official', 'Elected Official'),
        ('volunteer_support', 'Volunteer / Support Staff'),
    ]
   
    page = ParentalKey(
        OurteamPage,
        on_delete=models.CASCADE,
        related_name='ourteam_page_person',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    name =  models.TextField(blank=True, null=True)
    designation =  models.TextField(blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='volunteer_support',
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('name'),
        FieldPanel('role'),
        FieldPanel('designation'),
        FieldPanel('description'),
    ]
    class Meta:
        verbose_name = 'Ourteam Page Person'
        verbose_name_plural = 'Ourteam Page Persons'




    


