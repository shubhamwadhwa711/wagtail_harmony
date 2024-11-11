from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_modeladmin.mixins import ThumbnailMixin

from .models import HistoryPage


# class HistoryPageModelAdmin(ThumbnailMixin, ModelAdmin):
#     model = HistoryPage
#     menu_label = 'Add History'
#     # menu_icon = 'news'
#     menu_order = 200
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     # list_display = ()
#     # search_fields = ('title',)
#     # list_filter = ()
#     # thumb_image_field_name = ''
#     # list_export = (
   
#     # )

# modeladmin_register(HistoryPageModelAdmin)