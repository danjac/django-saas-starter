# Third Party Libraries
from allauth.socialaccount import views as socialaccount_views

from {{cookiecutter.project_slug}}.common.turbo.mixins import TurboStreamFormMixin


class SignupView(TurboStreamFormMixin, socialaccount_views.SignupView):
    turbo_stream_target = "signup-form"
    turbo_stream_template = "socialaccount/_signup.html"


signup = SignupView.as_view()
