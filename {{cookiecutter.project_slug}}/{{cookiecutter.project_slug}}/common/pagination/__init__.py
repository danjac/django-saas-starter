# Django
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
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


def get_paginated_context(page):
    return {
        "page_obj": page,
        "is_paginated": page.has_other_pages(),
        "object_list": page.object_list,
        "paginator": page.paginator,
    }
