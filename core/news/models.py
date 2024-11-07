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
from django.template.response import TemplateResponse


##################################################################################################




class NewsPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    name = models.TextField(blank=True, null=True,default="NEWS")
   
    button_text = models.TextField(blank=True, null=True,default ="Read more")
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
    bottom_button_text = models.TextField(blank=True, null=True,default ="Read more")
    bottom_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    
    content_panels = RichTextPageAbstract.content_panels + [
        # 
        FieldPanel("name"),
        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('link_page'),
        ], heading='Add Read more  Button'),

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
        "news.NewsDetailPage",
    ]

    class Meta:
        verbose_name = 'News Page'
        verbose_name_plural = 'News Pages'


    def update_context(self,context):
        news_details = NewsDetailPage.objects.all()
        context.update({
            'news_details': news_details,
           
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
     


class NewsDetailPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    name = models.TextField(blank=True, null=True,default="LATEST NEWS")
    date = models.DateField(null=True,blank=True)
    heading = models.TextField(blank=True, null=True)
    any_headline_heading = models.TextField(blank=True, null=True)
    any_headline_sort_description = models.TextField(blank=True, null=True)

    main_headline_text = models.TextField(blank=True, null=True)
    main_headline_description = models.TextField(blank=True, null=True)
    main_headline_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    # event_date = models.DateField(blank=True, null=True)

    button_text = models.TextField(blank=True, null=True,default ="Read more")
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
        FieldPanel("date"),
        FieldPanel("any_headline_heading"),
        FieldPanel("any_headline_sort_description"),
        InlinePanel('news_page_images', label='News Page Images'),
     
        MultiFieldPanel([
            FieldPanel('main_headline_text'),
            FieldPanel('main_headline_description'),
            FieldPanel('main_headline_image'),
        ], heading='Add Main headline content'),
       

    ]

    parent_page_types = ['news.NewsPage']
    subpage_types = []

    class Meta:
        verbose_name = 'News Detail Page'
        verbose_name_plural = 'News Detail Page'







class  NewsPageImages(Orderable):
    image_title = models.TextField(blank=True, null=True)
    page = ParentalKey(
        NewsDetailPage,
        on_delete=models.CASCADE,
        related_name='news_page_images',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    panels = [
        FieldPanel("image_title"),
        FieldPanel('image'),
    ]
    class Meta:
        verbose_name = 'News Page Images'
        verbose_name_plural = 'News Page Images'






