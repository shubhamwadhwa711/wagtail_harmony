from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_modeladmin.mixins import ThumbnailMixin

from .models import NewsPage ,NewsDetailPage


# class NewsDetailPageModelAdmin(ThumbnailMixin, ModelAdmin):
#     model = NewsDetailPage
#     menu_label = 'Add news'
#     # menu_icon = 'news'
#     menu_order = 200
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     # list_display = ('',)
#     # search_fields = ('title',)
#     # list_filter = ("title")
#     # thumb_image_field_name = ''
#     # list_export = (
    
#     # )

# modeladmin_register(NewsDetailPageModelAdmin)
