from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_modeladmin.mixins import ThumbnailMixin

from .models import SingleElectionPage,Party,PartyPosition


class SingleElectionPageModelAdmin(ThumbnailMixin, ModelAdmin):
    model = SingleElectionPage
    menu_label = 'Add Single Election'
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

modeladmin_register(SingleElectionPageModelAdmin)




class PartyModelAdmin(ModelAdmin):
    model = Party
    menu_label = 'Parties'
    menu_icon = 'group'  # Choose an icon that suits, or customize with your choice
    menu_order = 300  # Adjust the order if needed
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('party_name',)  # Display fields in list view
    search_fields = ('party_name',)  # Allow search by party name

# Register the PartyPosition model in Wagtail admin
class PartyPositionModelAdmin(ModelAdmin):
    model = PartyPosition
    menu_label = 'Party Positions'
    menu_icon = 'user'  # Choose an icon that suits
    menu_order = 301  # Adjust the order if needed
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('party_position',)  # Display fields in list view
    search_fields = ('party_position',)  # Allow search by position name

# Register both models
modeladmin_register(PartyModelAdmin)
modeladmin_register(PartyPositionModelAdmin)