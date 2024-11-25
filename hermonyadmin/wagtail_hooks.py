from django.utils.html import format_html
from django.templatetags.static import static
from wagtail.admin.menu import (
    MenuItem
)
from wagtail import hooks


@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('hermonyadmin.css'))


@hooks.register("register_help_menu_item")
def register_contact_menu_item():
    return MenuItem(
        "Reach out to Gryphos for help or see the editor guide below for articles about Wagtail, the platform HarmonyCMS is built on.",
        "https://gryphoscreative.com/contact/",
        icon_name="help",
        order=900,
        attrs={"target": "_blank", "rel": "noreferrer"},
    )


@hooks.register("register_help_menu_item")
def register_email_menu_item():
    return MenuItem(
        "Email Gryphos",
        "mailto:hello@gryphoscreative.com",
        icon_name="help",
        order=1000,
        attrs={"target": "_blank", "rel": "noreferrer"},
    )
