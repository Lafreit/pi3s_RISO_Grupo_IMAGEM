from django import template

register = template.Library()

@register.filter
def page_range(current_page, total_pages):
    try:
        current_page = int(current_page)
        total_pages = int(total_pages)
    except (ValueError, TypeError):
        return []

    start = max(current_page - 1, 1)
    end = min(current_page + 1, total_pages)
    return range(start, end + 1)
