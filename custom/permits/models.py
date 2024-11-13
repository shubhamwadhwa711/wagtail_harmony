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
#form
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
from wagtail.admin.panels import FieldPanel, MultiFieldPanel,InlinePanel,FieldRowPanel
from django.contrib import messages

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
        verbose_name = 'Business Permits'
        verbose_name_plural = 'Businesses Permits'



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



class FormField(AbstractFormField):
    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        choices=list(FORM_FIELD_CHOICES) + [('file', 'Upload File')]
    )
    page = ParentalKey("PermitPage", related_name="form_fields", on_delete=models.CASCADE)



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
    





class PermitPage(RichTextPageAbstract,AbstractEmailForm):
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

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("heading"),
        FieldPanel("description"),
        MultiFieldPanel([
            FieldPanel("permit_button_text"),
            FieldPanel("permit_link_page"),
        ],heading="Apply Now Button"),
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

    parent_page_types = ['permits.PermitsPage']
    subpage_types = []
    form_builder = CustomFormBuilder
    submissions_list_view_class = CustomSubmissionsListView


    class Meta:
        verbose_name = 'Permit Page'
        verbose_name_plural = 'Permit Pages'



    def serve(self,request,*args, **kwargs):
        request.is_preview = False
        template = self.get_template(request, *args, **kwargs)
        context= self.get_context(request, *args, **kwargs)
        search_query = request.GET.get('search', '')
        # context = self.update_context(default_context,search_query)

        if request.method == 'POST':
            form = self.get_form(request.POST, request.FILES, page=self)
            if form.is_valid():
               self.process_form_submission(form)
               context['form'] = self.get_form(page=self)
               messages.success(request, "Form submitted successfully!")

        else:
            context['form'] = self.get_form(page=self)

        return TemplateResponse(
            request,
            template,
            context,
        )
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.form_fields.exists():
            default_fields = [
                {"label": "First Name", "field_type": "singleline"},
                {"label": "Last Name", "field_type": "singleline"},
                {"label": "Email", "field_type": "email"},
                {"label": "Phone number", "field_type": "singleline"},
                {"label": "Choose a Business type", "field_type": "dropdown", "choices": "Businuess1,Businuess2,Businuess3"},
                {"label": "Choose Category", "field_type": "dropdown", "choices": "category1,category2,category3"},
                {"label": "Message", "field_type": "multiline"},
            ]
            for field_data in default_fields:
                FormField.objects.create(page=self, required=True, **field_data)
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
    




