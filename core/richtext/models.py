from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

# from blocks.richtext import richtext_blocks
richtext_blocks = []

# from .utils import og_image


class RichTextPageAbstract(Page):
    body = StreamField(
        richtext_blocks,
        use_json_field=True,
        blank=True,
    )

    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Cover image for this page, used in listings and at the top of the page'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('cover_image'),
    ]
    promote_panels.pop(1)  # Remove the 'For site menus' item

    settings_panels = Page.settings_panels + [
        FieldPanel('first_published_at'),
    ]

    search_feilds = Page.search_fields + [
        index.SearchField('body'),
    ]

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     super_save = super().save(*args, **kwargs)
    #     og_image(self.full_url, force=True)
    #     return super_save


class RichTextPage(RichTextPageAbstract):
    parent_page_types = ['home.HomePage',]
    subpage_types = []

    class Meta:
        verbose_name = 'Rich Text Page'
        verbose_name_plural = 'Rich Text Pages'
