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



class MeetingTypeChoices(models.TextChoices):
    GOVERNMENT = "gov", "Gov. Meetings"
    SOCIETY = "society", "Society Meetings"
    RWA = "rwa", "Monthly RWA Meetings"

class MeetingPage(Page):
    # meeting_date = models.DateTimeField("Meeting Date and Time")
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    meeting_date = models.DateField("Meeting Date",null=True,blank=True)
    meeting_start_time = models.TimeField("Start Time",null=True,blank=True)
    meeting_end_time = models.TimeField("End Time",null=True,blank=True)
    meeting_description =models.TextField("Enter meeting AGENDA",null=True,blank=True)
   
    meeting_type = models.CharField(
        max_length=20,
        choices=MeetingTypeChoices.choices,
        default=MeetingTypeChoices.SOCIETY,
        
    )

  

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('meeting_date'),
        FieldPanel('meeting_start_time'),
        FieldPanel('meeting_end_time'),
        FieldPanel('meeting_type'),
        FieldPanel('meeting_description')

    ]

    
    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"
