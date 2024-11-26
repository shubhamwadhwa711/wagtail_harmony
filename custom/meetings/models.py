from django.db import models

# Create your models here.
# core/models.py
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Page
from wagtail.fields import  StreamField
from django.template.response import TemplateResponse
from datetime import date
from django.db.models import Q


class MeetingTypes(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name  # Makes it easier to identify objects in the admin



class MeetingsPage(Page):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    meeting_text = models.CharField(max_length=200,null=True,blank=True,default="All Meetings")

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

    content_panels = RichTextPageAbstract.content_panels + [
        FieldPanel("meeting_text"),
        MultiFieldPanel([
            FieldPanel('bottom_heading'),
            FieldPanel('bottom_image_one'),
            FieldPanel('bottom_image_two'),
            # FieldPanel('bottom_link_page'),
        ], heading='Add Bottom Section'),
    ]
    parent_page_types = ['home.HomePage']
    subpage_types = [
        "meetings.MeetingPage",
    ]

    class Meta:
        verbose_name = 'Meetings Page'
        verbose_name_plural = 'Meeting Pages'

   

    def update_context(self, context, request):
        today = date.today()
        search_query = request.GET.get('search', '')
        meetings = MeetingPage.objects.all()
       
        # Get filter parameters from request
        selected_meeting_types = request.GET.getlist('meeting_types')
        filter_option = request.GET.get('filter', 'all')
        event_text = "All Meetings"
        
     
        # Defaults to 'all' if no filter is provided
        if filter_option == 'upcoming':
            meetings = meetings.filter(meeting_date__gte=today)
            event_text = "Upcoming Event"
        elif filter_option == 'past':
            meetings = meetings.filter(meeting_date__lt=today)
            event_text = "Past"
        elif filter_option.isdigit():  # Check if it's a year
            meetings = meetings.filter(meeting_date__year=int(filter_option))
            event_text = "2023"
    
        if selected_meeting_types:
            meetings = meetings.filter(meeting__id__in=selected_meeting_types)

        if search_query:
            meetings = meetings.filter(
                Q(meeting_description=search_query) 
            )

      
        meeting_types = MeetingTypes.objects.all()

        # Update context
        context.update({
            'meetings': meetings.distinct(),  # Ensure no duplicates in queryset
            'meeting_types': meeting_types,
            'filter_option': filter_option, 
            'event_text': event_text, # To identify the active filter in the template
        })
        return context

 

    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        default_context = self.get_context(request, *args, **kwargs)
        context = self.update_context(default_context,request)
        return TemplateResponse(
            request,
            template,
            context,
        )
    
     

    
  



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
    meeting = models.ForeignKey(
        'meetings.MeetingTypes',  # Reference the `MeetingTypes` model
        on_delete=models.SET_NULL,  # Allows null values if the type is deleted
        null=True,
        blank=True,
        related_name='meetings',  # Optional: to access related MeetingPages from MeetingTypes
    )

  

    content_panels = Page.content_panels + [
        FieldPanel('meeting_date'),
        FieldPanel('meeting_start_time'),
        FieldPanel('meeting_end_time'),
        FieldPanel('meeting'),
        FieldPanel('meeting_description')

    ]

    parent_page_types = ['meetings.MeetingsPage']
  

    
    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"
