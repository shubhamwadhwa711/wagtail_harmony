
from wagtail import blocks
richtext_blocks = []

class Noticeblock(blocks.StructBlock):
    notice = blocks.TextBlock()

    class Meta:
        template = "blocks/notice.html"
        icon = "placeholder"
        # group = "Home"

richtext_blocks += [("notice_block", Noticeblock())]

#blocks 