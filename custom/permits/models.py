from django.db import models

# Create your models here.

from wagtail.admin.panels import FieldPanel, MultiFieldPanel,StreamValue,InlinePanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable, Site
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from django.template.response import TemplateResponse


##################################################################################################




class PermitsPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    #show the latest event as an html

    heading = models.TextField(blank=True, null=True,default="Permits")
    content_panels = RichTextPageAbstract.content_panels + [   
        FieldPanel("heading"),
            
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        "permits.PermitPage",
    ]

    class Meta:
        verbose_name = 'Permits Page'
        verbose_name_plural = 'Permits Pages'



    def update_context(self,context,search_query):
        permits = PermitPage.objects.all()
        # if search_query:
        #     histories = histories.filter(
        #         Q(content_short_description__icontains=search_query) |
        #         Q(content_full_description__icontains=search_query) |
        #         Q(date__icontains=search_query)  # Adjust fields as needed
        #     )
        context.update({
            'permits': permits,
            # 'search_query': search_query,
           
        })
        return context

    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        default_context = self.get_context(request, *args, **kwargs)
        search_query = request.GET.get('search', '')
        context = self.update_context(default_context,search_query)

        return TemplateResponse(
            request,
            template,
            context,
        )




class PermitPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    heading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    permit_button_text = models.TextField(blank=True, null=True,default ="Apply Now")
    permit_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("heading"),
        FieldPanel("description"),
        MultiFieldPanel([
            FieldPanel("permit_button_text"),
            FieldPanel("permit_link_page"),
        ],heading="Apply Now Button")

    ]

    parent_page_types = ['permits.PermitsPage']
    subpage_types = []


    class Meta:
        verbose_name = 'Permit Page'
        verbose_name_plural = 'Permit Pages'



    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        context= self.get_context(request, *args, **kwargs)
        search_query = request.GET.get('search', '')
        # context = self.update_context(default_context,search_query)

        return TemplateResponse(
            request,
            template,
            context,
        )


