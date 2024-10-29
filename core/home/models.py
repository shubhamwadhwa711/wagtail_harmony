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

##################################################################################################

class HomePage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    notice = models.TextField(blank=True, null=True)
    county_text = models.TextField(blank=True, null=True)
    heading_text = models.TextField(blank=True, null=True)
    home_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    quick_links_text = models.TextField(blank=True, null=True)
    page_links_bgimage = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    # News
    read_page_text = models.TextField(blank=True, null=True)
    read_more_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    # Upcoming
    upcoming_event_text = models.TextField(blank=True, null=True)
    more_event_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    # History
    history_heading = models.TextField(blank=True, null=True)
    history_text = models.TextField(blank=True, null=True)
    history_page_text = models.TextField(blank=True, null=True)
    history_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    # Team
    team_heading = models.TextField(blank=True, null=True)
    team_text = models.TextField(blank=True, null=True)
    team_page_text = models.TextField(blank=True, null=True)
    team_link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel('notice'),
        FieldPanel('county_text'),
        FieldPanel('heading_text'),
        FieldPanel('home_image'),
        FieldPanel('page_links_bgimage'),
        
        MultiFieldPanel([
            FieldPanel('quick_links_text'),
            InlinePanel('home_page_links', label='Home Page Quick Links'),
        ], heading='Attach Quick Links'),

        MultiFieldPanel([
            FieldPanel('read_page_text'),
            FieldPanel('read_more_link_page'),
        ], heading='Attach Latest News'),
        
        MultiFieldPanel([
            FieldPanel('upcoming_event_text'),
            FieldPanel('more_event_link_page'),
        ], heading='Attach More Event Page'),

        MultiFieldPanel([
            FieldPanel('history_heading'),
            FieldPanel('history_text'),
            FieldPanel('history_page_text'),
            FieldPanel('history_link_page'),
        ], heading='Home Page History'),

        MultiFieldPanel([
            FieldPanel('team_heading'),
            FieldPanel('team_text'),
            FieldPanel('team_page_text'),
            FieldPanel('team_link_page'),
            InlinePanel('team_member', label='Team Member'),
        ], heading='Home Page Team'),
    ]


    


class HomePageLinks(Orderable):
    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name='home_page_links',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    link_text = models.TextField(blank=True, null=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('link_text'),
        FieldPanel('link_page'),
    ]

    class Meta:
        verbose_name = 'Home Page Link'
        verbose_name_plural = 'Home Page Links'


class TeamMember(Orderable):
    page = ParentalKey(HomePage, related_name='team_member')
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    team_member_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('designation'),
        FieldPanel('description'),
        FieldPanel('team_member_image'),
    ]

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
