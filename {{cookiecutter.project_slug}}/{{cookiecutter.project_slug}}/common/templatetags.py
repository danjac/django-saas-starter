import collections
import re

# Django
from django import template
from django.shortcuts import resolve_url

register = template.Library()

ActiveLink = collections.namedtuple("Link", "url match exact")


@register.simple_tag(takes_context=True)
def active_link(context, url_name, *args, **kwargs):
    url = resolve_url(url_name, *args, **kwargs)
    if context["request"].path == url:
        return ActiveLink(url, True, True)
    elif context["request"].path.startswith(url):
        return ActiveLink(url, True, False)
    return ActiveLink(url, False, False)


@register.simple_tag(takes_context=True)
def active_link_regex(context, pattern, url_name, *args, **kwargs):
    url = resolve_url(url_name, *args, **kwargs)

    if context["request"].path == url:
        return ActiveLink(url, True, True)

    if re.compile(pattern).match(context["request"].path):
        return ActiveLink(url, True, False)

    return ActiveLink(url, False, False)
