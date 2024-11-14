from django.db import models

# Create your models here.
# core/models.py
from django.core.files.storage import FileSystemStorage


from core.richtext.models import RichTextPageAbstract
from blocks.richtext import richtext_blocks
from wagtail.models import Orderable
from wagtail.fields import  StreamField
from django.utils.translation import gettext_lazy as _

from django.template.response import TemplateResponse
import os
from django.conf import settings
from wagtail.contrib.forms.forms import FormBuilder
from django.forms import FileField,TimeField
from django.forms.widgets import ClearableFileInput, CheckboxSelectMultiple
from django.utils.html import format_html
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.forms.views import SubmissionsListView
from wagtail.admin.panels import FieldPanel, MultiFieldPanel,StreamValue,InlinePanel,FieldRowPanel
from modelcluster.fields import ParentalKey
from django import forms

###################


from wagtail.contrib.forms.models import (
    FORM_FIELD_CHOICES,
    AbstractEmailForm,
    AbstractFormField,
    AbstractFormField,
)
from django.forms import FileInput ,MultiValueField

class FormField(AbstractFormField):
    """
    Extended FormField to include custom field types.
    """

    FIELD_TYPE_CHOICES = list(FORM_FIELD_CHOICES) + [
        ('file', 'Upload File'),
        ('time', 'Time'),
        ('multiupload', 'Multiple Upload'),
    ]

    field_type = models.CharField(
        verbose_name="field type",
        max_length=16,
        choices=FIELD_TYPE_CHOICES
    )

    page = ParentalKey(
        "ContactPage", 
        related_name="form_fields", 
        on_delete=models.CASCADE
    )






class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class CustomFormBuilder(FormBuilder):
    """Custom FormBuilder for handling additional field types."""

    def create_file_field(self, field, options):
        """Single file upload field."""
        return FileField(**options)
    
    def create_time_field(self, field, options):
        """Time field creation."""
        return TimeField(**options)
    
    
    # FileField works for multiple files
    def create_multiupload_field(self, field, options):
        """Multiple file upload field with `multiple` attribute set."""
        return MultipleFileField(**options)
    

    
    def get_form_field(self, field):
        """Override form field retrieval."""
        options = self.get_field_options(field)
        field_type = field.field_type

        # Add a dynamic mapper for custom field
        if field_type == "file":
            return self.create_file_field(field, options)
        elif field_type == "time":
            return self.create_time_field(field, options)
        elif field_type == "multiupload":
            return self.create_multiupload_field(field, options)
        else:
            return super().get_form_field(field)


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
  
    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel("form_fields", heading="Form fields", label="Field"),
        InlinePanel('contactform_details', label='Add Contact form details'),
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
    
    parent_page_types = ['home.Homepage']  
    subpage_types = []
    form_builder = CustomFormBuilder

    
    submissions_list_view_class = CustomSubmissionsListView

    class Meta:
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Pages'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Automatically create default form fields if they don't already exist
        if not self.form_fields.exists():
            default_fields = [
                {"label": "First Name", "field_type": "singleline", "required": True},
                {"label": "Last Name", "field_type": "singleline", "required": True},
                {"label": "Email", "field_type": "email", "required": True},
                {"label": "Phone number", "field_type": "singleline", "required": True},
                {"label": "Event Date", "field_type": "date", "required": True},
                {"label": "Event Time", "field_type": "time", "required": True},
                {"label": "Event Description", "field_type": "multiline", "required": True},
                {"label": "Upload Event Featured Image", "field_type": "file", "required": True, },
                {"label": "Upload Event Featured Images", "field_type": "multiupload", "required": True,},
                {"label": "Event Price", "field_type": "radio", "required": True, "choices": "paid,free"},
                {"label": "Amount", "field_type": "dropdown", "required": False, "choices": "20,30,40"},
            ]
            
            for field_data in default_fields:
                FormField.objects.create(page=self, **field_data)











 

    def save_img_path(self,f):
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT))
        filename = fs.save(f'contacts/{f.name}', f)
        uploaded_file_url = fs.url(filename)
        return uploaded_file_url


    def process_form_submission(self, form):
        cleaned_data = form.cleaned_data
        try:
        
            for name, field in form.fields.items():
                if isinstance(field, FileField):
                    image_file_data = cleaned_data.get(name)
                    if image_file_data:

                        image_file_data = image_file_data if isinstance(image_file_data, list) else [image_file_data]
                        cleaned_data[name] = [self.save_img_path(f) for f in image_file_data]
                    else:
                       
                        del cleaned_data[name]

            # Save form submission to database
            submission = self.get_submission_class().objects.create(
                form_data=cleaned_data,
                page=self,
            )
            if self.to_address:
                self.send_mail(form)

            return submission

        except Exception as e:
            print(f"Error processing form submission: {e}")
            return None

            
            

        
    def serve(self,request,*args, **kwargs):
            request.is_preview = False
            template = self.get_template(request, *args, **kwargs)
            context = self.get_context(request, *args, **kwargs)
           
            # context = self.update_context(default_context)
            if request.method == 'POST':
                form = self.get_form(request.POST, request.FILES, page=self)
                if form.is_valid():
                    self.process_form_submission(form)
                    context['form'] = self.get_form(page=self)
                   
                else:
                    print(form.errors)
                    context['form'] = self.get_form(page=self)

            context['form'] = self.get_form(page=self)
        
            return TemplateResponse(
                request,
                template,
                context,
            )

    

class  ConactDetails(Orderable):
    page = ParentalKey(
        ContactPage,
        on_delete=models.CASCADE,
        related_name='contactform_details',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    contact_form_heading = models.TextField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    contact_heading = models.CharField(max_length=20,blank=True, null=True,default="Quick Contact")
    contact_number  = models.CharField(max_length=20,blank=True, null=True)
    contact_address  = models.TextField(blank=True, null=True)

    panels =  [
        FieldPanel('contact_form_heading'),
        FieldPanel('heading'),
        FieldPanel('description'),
        MultiFieldPanel([
            FieldPanel('contact_heading'),
            FieldPanel('contact_number'),
            FieldPanel('contact_address'),
            
        ], heading='Add Form Details'),

    ]



    
