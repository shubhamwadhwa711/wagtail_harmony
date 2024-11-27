from django.db import models

# Create your models here.
# core/models.py

from wagtail.admin.panels import FieldPanel, MultiFieldPanel,InlinePanel
from datetime import datetime, timedelta
from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.fields import StreamField
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
        # 
        FieldPanel("name"),
        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('link_page'),
        ], heading='Add Read more  Button'),
        MultiFieldPanel([
                FieldPanel('footer_heading'),
                FieldPanel('footer_button_text'),
                FieldPanel('footer_link_page'),
                InlinePanel('page_footer_images', label='Footer Images'),
            ], heading='Add Bottom Section'),   
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        "news.NewsDetailPage",
    ]

    class Meta:
        verbose_name = 'News Page'
        verbose_name_plural = 'News Pages'

    def update_context(self, context):
        today = datetime.now().date()
        ninety_days_ago = today - timedelta(days=90)
        first_day_of_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        last_day_of_last_month = first_day_of_last_month.replace(day=1) + timedelta(days=31)
        start_of_2024 = datetime(today.year, 1, 1).date()

        all_news = NewsDetailPage.objects.all().order_by('-date')
        last_90_days_news = NewsDetailPage.objects.filter(date__gte=ninety_days_ago).order_by('-date')
        last_month_news = NewsDetailPage.objects.filter(date__range=(first_day_of_last_month, last_day_of_last_month)).order_by('-date')
        news_2024 = NewsDetailPage.objects.filter(date__year=2024).order_by('-date')

        context.update({
            'all_news': all_news,
            'last_90_days_news': last_90_days_news,
            'last_month_news': last_month_news,
            'news_2024': news_2024,
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

class  Footerimages(Orderable):
    page = ParentalKey(
        NewsPage,
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



class NewsDetailPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    news_bg_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
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

  
    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("news_bg_image"),
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






