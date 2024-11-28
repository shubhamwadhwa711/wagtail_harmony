from django import template
from datetime import date
from django.db.models import Q
from django.core.paginator import Paginator
register = template.Library()

@register.simple_tag
def filter_by_date(queryset, date_field, filter_option):

    today = date.today()
    filter_kwargs = {}

    if filter_option == 'past':
        filter_kwargs[f"{date_field}__lt"] = today
    else:
        filter_kwargs[f"{date_field}__gte"] = today

    return queryset.filter(**filter_kwargs)





def get_pagination(request,queryset):
    paginator = Paginator(queryset, 10)  # Show 10 meetings per page
    page_number = request.GET.get('page')  # Get the current page number from the query params
    page_obj = paginator.get_page(page_number) 
    return page_obj


