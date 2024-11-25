from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_modeladmin.mixins import ThumbnailMixin

from .models import MeetingPage,MeetingTypes


class MeetingPageModelAdmin(ThumbnailMixin, ModelAdmin):
    model = MeetingPage
    menu_label = 'Meetings'
    # menu_icon = 'news'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    # list_display = ()
    # search_fields = ('title',)
    # list_filter = ()
    # thumb_image_field_name = ''
    # list_export = (
   
    # )

modeladmin_register(MeetingPageModelAdmin)




class MeetingTypesModelAdmin(ModelAdmin):
    model = MeetingTypes
    menu_label = 'Meetings Types'
    menu_icon = 'group'  # Choose an icon that suits, or customize with your choice
    menu_order = 300  # Adjust the order if needed
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('id','name',)  # Display fields in list view
    search_fields = ('name',)  # Allow search by party name