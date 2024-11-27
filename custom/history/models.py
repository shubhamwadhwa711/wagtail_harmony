from django.db import models


from wagtail.admin.panels import FieldPanel, MultiFieldPanel,InlinePanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.fields import  StreamField
from django.template.response import TemplateResponse
from django.db.models import Q
from modelcluster.models import ClusterableModel
from taggit.models import  TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager

class HistoriesPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    heading = models.TextField(blank=True, null=True,default="History of Harmony")
    footer_heading = models.TextField(blank=True, null=True,default="Share your story about Harmony")
    footer_button_text = models.TextField(blank=True, null=True,default ="Share Story")
    footer_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
            FieldPanel('heading'),
            MultiFieldPanel([
            FieldPanel('footer_heading'),
            FieldPanel('footer_button_text'),
            FieldPanel('footer_link_page'),
            InlinePanel('page_footer_images', label='Footer Images'),
        ], heading='Add Bottom Section'),

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['history.HistoryPage']

    class Meta:
        verbose_name = 'Histories Page'
        verbose_name_plural = 'Histories Pages'


    def update_context(self, context, search_query,request):
            selected_tag = request.GET.get('tag')
            if not selected_tag:
                selected_tag = HistoryPage.tags.order_by("name").first().slug
            histories = HistoryPage.objects.filter(tags__slug__iexact=selected_tag).distinct()
            if search_query:
                histories = histories.filter(
                    Q(short_description__icontains=search_query) |
                    Q(full_description__icontains=search_query) |
                    Q(date__icontains=search_query)  # Adjust fields as needed
                )

            context.update({
                "histories": histories,
                "tags": HistoryPage.tags.all().order_by("name"),
                "selceted_tag": selected_tag,
            })
            return context
    


    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        default_context = self.get_context(request, *args, **kwargs)
        search_query = request.GET.get('search', '')
        context = self.update_context(default_context,search_query,request)
        return TemplateResponse(
            request,
            template,
            context,
        )

class  Footerimages(Orderable):
    page = ParentalKey(
        HistoriesPage,
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

class HistoryTags(TaggedItemBase):
    content_object = ParentalKey(
        "HistoryPage", on_delete=models.CASCADE, related_name="tagged_items"
    )

class  HistoryPage(RichTextPageAbstract):
    date = models.DateField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    tags = ClusterTaggableManager(through=HistoryTags, blank=True)
 
    content_panels = RichTextPageAbstract.content_panels +[
        FieldPanel('date'),
        FieldPanel('image'),
        FieldPanel('short_description'),
        FieldPanel('full_description'),
        FieldPanel('tags'),

    ]
    parent_page_types = ['history.HistoriesPage']
    subpage_types = []

    class Meta:
        verbose_name = 'History Page'
        verbose_name_plural = 'History Pages'


    
    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        context = self.get_context(request, *args, **kwargs)
        # search_query = request.GET.get('search', '')
        # context = self.update_context(default_context,search_query,request)
        return TemplateResponse(
            request,
            template,
            context,
        )
    
