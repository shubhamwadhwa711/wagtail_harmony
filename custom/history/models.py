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
from django.template.response import TemplateResponse
from django.db.models import Q
from modelcluster.models import ClusterableModel


##################################################################################################

class HistoriesPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    heading = models.TextField(blank=True, null=True,default="History of Harmony")

    bottom_heading = models.TextField(blank=True, null=True,default="Share your story about Harmony")
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
    bottom_button_text = models.TextField(blank=True, null=True,default ="Share Story")
    bottom_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )


    content_panels = RichTextPageAbstract.content_panels + [
            FieldPanel('heading'),
            InlinePanel('history_page_details', label='History Page Details'),
            MultiFieldPanel([
            FieldPanel('bottom_heading'),
            FieldPanel('bottom_image_one'),
            FieldPanel('bottom_image_two'),
            FieldPanel('bottom_button_text'),
            FieldPanel('bottom_link_page'),
        ], heading='Add Bottom Section'),

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = 'Histories Page'
        verbose_name_plural = 'Histories Pages'




    def update_context(self,context,search_query):
        histories = HistoryContent.objects.all()

        if search_query:
            histories = histories.filter(
                Q(content_short_description__icontains=search_query) |
                Q(content_full_description__icontains=search_query) |
                Q(date__icontains=search_query)  # Adjust fields as needed
            )
             # Fallback to HistoryDetails if no matches are found
            if not histories.exists():
                histories = HistoryDetails.objects.filter(
                    Q(history_year__icontains=search_query) |
                    Q(short_heading__icontains=search_query) |
                    Q(description__icontains=search_query)
                )


        context.update({
            'histories': histories,
            'search_query': search_query,
        
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


    # def serve(self,request,*args, **kwargs):
    #     request.is_preview = False
    #     template = self.get_template(request, *args, **kwargs)
    #     context = self.get_context(request, *args, **kwargs)
    #     # context = self.update_context(default_context)
       
    #     return TemplateResponse(
    #         request,
    #         template,
    #         context,
    #     )


class  HistoryDetails(Orderable,ClusterableModel):
    page = ParentalKey(
        HistoriesPage,
        on_delete=models.CASCADE,
        related_name='history_page_details',
    )
    history_year = models.CharField(max_length=200,null=True,blank=False)
    short_heading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
 
    panels = [
        FieldPanel("history_year"),
        FieldPanel('short_heading'),
        FieldPanel('description'),
        InlinePanel('history_contents', label='History Contents'),
    ]
    

class  HistoryContent(Orderable):
    page = ParentalKey(
        HistoryDetails,
        on_delete=models.CASCADE,
        related_name='history_contents',
    )
  
    date = models.DateField(blank=True, null=True)
    content_short_description = models.TextField(blank=True, null=True)
    content_full_description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    panels=[
        FieldPanel('date'),
        FieldPanel('image'),
        FieldPanel('content_short_description'),
        FieldPanel('content_full_description'),
    ]

   