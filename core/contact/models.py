from django.db import models

# Create your models here.
# core/models.py



from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable, Site

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.images.models import Image
from wagtail.blocks import RichTextBlock
from wagtail.models import Orderable

from wagtail.contrib.forms.models import (
    FORM_FIELD_CHOICES,
    AbstractEmailForm,
    AbstractFormField,
)
from wagtail.contrib.forms.forms import FormBuilder
from django.forms import FileField
from django.utils.html import format_html
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.forms.views import SubmissionsListView
from wagtail.admin.panels import FieldPanel, MultiFieldPanel,StreamValue,InlinePanel,FieldRowPanel
from modelcluster.fields import ParentalKey
###################






class ContactsPage(RichTextPageAbstract):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
 
   
    content_panels = RichTextPageAbstract.content_panels + [
       
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ["contact.ContactPage"]

    class Meta:
        verbose_name = 'Contacts Page'
        verbose_name_plural = 'Contacts Pages'






class FormField(AbstractFormField):
    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        choices=list(FORM_FIELD_CHOICES) + [('file', 'Upload File')]
    )
    page = ParentalKey("ContactPage", related_name="form_fields", on_delete=models.CASCADE)



class CustomFormBuilder(FormBuilder):
    def create_file_field(self, field, options):
        return FileField(**options)


class CustomSubmissionsListView(SubmissionsListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.is_export:
            field_types = ['submission_date'] + [field.field_type for field in self.form_page.get_form_fields()]
            data_rows = context['data_rows']

            for data_row in data_rows:
                fields = data_row['fields']

                for idx, (value, field_type) in enumerate(zip(fields, field_types)):
                    if field_type == 'file' and value:
                        filename = value.split('/')[-1]
                        fields[idx] = format_html(
                            "<a href='{}'>{}</a>",
                            value,
                            filename
                        )

        return context



class ContactPage(RichTextPageAbstract,AbstractEmailForm):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )
    contact_form_name = models.TextField(blank=True, null=True)

    # contact_type = models.CharField(max_length=20, choices=ContactType.choices,
    #                                 default= ContactType.HOST_EVENT)
    heading = models.TextField(blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    
    contact_heading = models.CharField(max_length=20,blank=True, null=True,default="Quick Contact")
    contact_number  = models.CharField(max_length=20,blank=True, null=True)
    contact_address  = models.TextField(blank=True, null=True)
  
    parent_page_types = ['contact.HomePage']
    subpage_types = []
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('contact_form_name'),
        FieldPanel("heading"),
        FieldPanel("description"),
        MultiFieldPanel([
            FieldPanel("contact_heading"),
            FieldPanel("contact_number"),
            FieldPanel("contact_address"),
        ],heading='Add Contact Details'),
        InlinePanel("form_fields", heading="Form fields", label="Field"),
        FormSubmissionsPanel(),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]
    
    parent_page_types = ['contact.ContactsPage']  
    subpage_types = []
    form_builder = CustomFormBuilder
    submissions_list_view_class = [CustomSubmissionsListView]

    class Meta:
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Pages'
     
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Automatically create default form fields if they don't already exist
        if not  self.form_fields.exists():
            FormField.objects.create(
                page=self,
                label="First Name",
                field_type="singleline",
                required=True,
            )

            FormField.objects.create(
                page=self,
                label="Last Name",
                field_type="singleline",
                required=True,
            )

            FormField.objects.create(
                page=self,
                label="Email",
                field_type="email",
                required=True,
            )
            FormField.objects.create(
                page=self,
                label="Phone number",
                field_type="singleline",
                required=True,
            )

            FormField.objects.create(
                page=self,
                label="Event Date",
                field_type="date",
                required=True,
                )
            
            FormField.objects.create(
                page=self,
                label="Event Time",
                field_type="time",
                required=True,
                )



            FormField.objects.create(
                page=self,
                label="Event Description",
                field_type="multiline",
                required=True,
                )
            

            FormField.objects.create(
                page=self,
                label="Upload Event Featured Image",
                help_text = "",
                field_type="file",
                required=True,
            )

            FormField.objects.create(
                page=self,
                label="Upload Event Featured Image",
                help_text = "Add Event Images(Upto 5 Images)",
                field_type="file",
                required=True,
                
            )


            



    

# FORM_FIELD_CHOICES = (
#     ("singleline", _("Single line text")),
#     ("multiline", _("Multi-line text")),
#     ("email", _("Email")),
#     ("number", _("Number")),
#     ("url", _("URL")),
#     ("checkbox", _("Checkbox")),
#     ("checkboxes", _("Checkboxes")),
#     ("dropdown", _("Drop down")),
#     ("multiselect", _("Multiple select")),
#     ("radio", _("Radio buttons")),
#     ("date", _("Date")),
#     ("datetime", _("Date/time")),
#     ("hidden", _("Hidden field")),
# )





#             FormField.objects.create(
#                 page=self,
#                 label="Your Location",
#                 field_type="dropdown",
#                 required=True,
#                 choices="North Carolina,Texas")
          
#             FormField.objects.create(
#                 page=self,
#                 label="Attach Design",
#                 help_text = "Optional, max file size of 20 MB",
#                 field_type="file",
#                 required=True,
#             )

#             FormField.objects.create(
#                 page=self,
#                 label="What's important to you in your custom home?",
#                 field_type="multiline",
#                 required=True,
#             )
    





# class ContactType(models.TextChoices):
#     HOST_EVENT = "host_event", "Host an Event or Other"
#     SHARE_HISTORY = "share_history", "Share History Story"
#     DEVELOP_HARMONY = "develop_harmony", "Develop in Harmony"
