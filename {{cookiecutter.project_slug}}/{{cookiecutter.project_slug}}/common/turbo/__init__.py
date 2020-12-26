# Django
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


def render_turbo_stream_to_string(template, context, action, target, **template_kwargs):
    content = render_to_string(template, context, **template_kwargs)
    start_tag = mark_safe(
        f'<turbo-stream target="{target}" action="{action}"><template>'
    )
    end_tag = mark_safe("</template></turbo-stream>")
    return start_tag + content + end_tag
