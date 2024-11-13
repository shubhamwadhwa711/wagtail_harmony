from core.conf.models import NavigationSettings

from django.conf import settings
from django.db import IntegrityError

def navigation_settings(request):
    """
    Provides the navigation settings.
    """
    try:
        return {"navigation_settings": NavigationSettings.for_request(request=request)}
    except (NavigationSettings.DoesNotExist, IntegrityError):
        return {"navigation_settings": None}