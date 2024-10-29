from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.images.blocks import ImageChooserBlock


richtext_blocks = []


home_blocks = richtext_blocks.copy()

class ButtonValue(blocks.StructValue):
    @property
    def href(self):
        if self.get("page"):
            return self.get("page").url
        elif self.get("url"):
            return self.get("url")
        else:
            return "#"
        

class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock()

    type = blocks.ChoiceBlock(
        choices=[
            ("btn-dark", "Dark"),
            ("btn-light", "Light"),
            ("btn-link", "Link"),
            ("btn-primary", "Primary"),
            ("btn-secondary", "Secondary"),
        ],
        default="btn-primary",
    )

    page = blocks.PageChooserBlock(required=False)
    url = blocks.URLBlock(label="URL", required=False)

    class Meta:
        template = ""
        icon = "placeholder"
        value_class = ButtonValue
        group = "Standard"


richtext_blocks += [("button", ButtonBlock())]

class HomeHeroBlock(blocks.StructBlock):
    title = blocks.TextBlock()
    text = blocks.TextBlock()
    button = ButtonBlock()
    image = ImageChooserBlock()

    class Meta:
        template = ""
        icon = "placeholder"
        group = "Home"