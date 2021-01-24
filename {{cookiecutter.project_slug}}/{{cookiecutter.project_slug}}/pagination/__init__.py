# Django
from django.conf import settings
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _


def paginate(
    request,
    queryset,
    page_size=settings.DEFAULT_PAGE_SIZE,
    param="page",
    allow_empty=True,
    orphans=0,
):

    paginator = Paginator(
        queryset, page_size, allow_empty_first_page=allow_empty, orphans=orphans
    )
    try:
        return paginator.page(int(request.GET.get(param, 1)))
    except (ValueError, InvalidPage):
        raise Http404(_("Invalid page"))


def get_pagination_context(request, queryset, **pagination_kwargs):
    page = paginate(request, queryset, **pagination_kwargs)
    return {
        "page_obj": page,
        "paginator": page.paginator,
        "object_list": page.object_list,
        "is_paginated": page.has_other_pages(),
    }


def render_paginated_queryset(
    request, queryset, template_name, context=None, **pagination_kwargs
):
    context = {
        **(context or {}),
        **get_pagination_context(request, queryset, **pagination_kwargs),
    }
    return TemplateResponse(request, template_name, context)
