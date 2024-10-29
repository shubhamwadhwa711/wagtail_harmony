import hashlib
import io
import threading

from django import template
from django.core.files.storage import default_storage
from django.utils.html import format_html
from django.utils import timezone

# from gryphoncms.chromium import generate_screenshot_from_url

# register = template.Library()


# def og_image(url, force=False):
#     if not url:
#         return ""

#     filename = hashlib.md5(url.encode("utf-8")).hexdigest()
#     filename = f"og_images/{filename}.png"

#     if not default_storage.exists(filename) or force:
#         # save a quick file to prevent infinite loop
#         default_storage.save(filename, io.BytesIO())
#         generate_screenshot_from_url(url, filename)

#     # get full url including domain
#     url = default_storage.url(filename)
#     return format_html('<meta property="og:image" content="{}">', url)
