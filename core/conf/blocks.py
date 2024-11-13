from wagtail import blocks
from wagtail.blocks import StructValue
from wagtail.images.blocks import ImageChooserBlock


# class NavigationElementValue(StructValue):
#     def href(self):
#         if self.get("url"):
#             return self.get("url")
#         elif self.get("page"):
#             return self.get("page").url
#         else:
#             return "#"



# class NavigationPage(blocks.StructBlock):
#     title = blocks.CharBlock()
#     page = blocks.PageChooserBlock(required=False)
#     url = blocks.URLBlock(label="URL", required=False)

# class NavigationElement(blocks.StructBlock):
#     icon_image = ImageChooserBlock(required=False)
#     category  = blocks.CharBlock()
#     children = blocks.StreamBlock([("navpages", NavigationPage())], default=[])



#     class Meta:
#         icon = "placeholder"
#         value_class = NavigationElementValue


# class DropdownElement(blocks.StructBlock):
#     title = blocks.CharBlock()
#     children = blocks.StreamBlock([("element", NavigationElement())], default=[])

#     class Meta:
#         icon = "placeholder"
    


from wagtail import blocks
from wagtail.blocks import StructValue
from wagtail.images.blocks import ImageChooserBlock


class NavigationElementValue(StructValue):
    def href(self):
        if self.get("url"):
            return self.get("url")
        elif self.get("page"):
            return self.get("page").url
        return "#"  # Default fallback


class NavigationPage(blocks.StructBlock):
    title = blocks.CharBlock()
    page = blocks.PageChooserBlock(required=False)
    # url = blocks.URLBlock(label="URL", required=False)

    class Meta:
        icon = "link"


class NavigationElement(blocks.StructBlock):
    icon_image = ImageChooserBlock(required=False)
    category = blocks.CharBlock()
    children = blocks.StreamBlock(
        [("navpages", NavigationPage())], required=False
    )

    class Meta:
        icon = "placeholder"
        value_class = NavigationElementValue


class DropdownElement(blocks.StructBlock):
    title = blocks.CharBlock()
    children = blocks.StreamBlock(
        [("element", NavigationElement())], required=False
    )

    class Meta:
        icon = "placeholder"











# class NavigationElement(blocks.StructBlock):
#     icon_image = ImageChooserBlock(required=False)
#     category  = blocks.CharBlock()
#     title = blocks.CharBlock()
#     page = blocks.PageChooserBlock(required=False)
#     url = blocks.URLBlock(label="URL", required=False)

#     class Meta:
#         icon = "placeholder"
#         value_class = NavigationElementValue
