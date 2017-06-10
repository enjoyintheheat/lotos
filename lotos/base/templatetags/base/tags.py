from django import template
from django.shortcuts import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def highlight_active(context, url):
    url = reverse(url)
    path = context['request'].path
    return "class=active" if url == path else ''
