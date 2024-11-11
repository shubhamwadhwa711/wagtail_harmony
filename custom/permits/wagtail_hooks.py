from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_modeladmin.mixins import ThumbnailMixin

from .models import PermitPage


# class PermitPageModelAdmin(ThumbnailMixin, ModelAdmin):
#     model = PermitPage
#     menu_label = 'Add Permits'
#     # menu_icon = ""
#     menu_order = 200
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     # list_display = ()
#     # search_fields = ('title',)
#     # list_filter = ()
#     # thumb_image_field_name = ''
#     # list_export = (
   
   
#     # )

# modeladmin_register(PermitPageModelAdmin)