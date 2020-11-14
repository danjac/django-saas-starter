# Copyright (c) 2020 by Dan Jacob
# SPDX-License-Identifier: AGPL-3.0-or-later

# Django
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.utils.translation import gettext_lazy as _

# Localhub
from localhub.common.forms import FormHelper
from localhub.common.forms.widgets import BaseTypeaheadInput, ClearableImageInput

# Local
from .app_settings import MENTIONS_TYPEAHEAD_CONFIG
from .validators import validate_mentions

User = get_user_model()


class MentionsTypeaheadInput(BaseTypeaheadInput):
    typeahead_configs = [MENTIONS_TYPEAHEAD_CONFIG]


class MentionsField(forms.CharField):
    widget = MentionsTypeaheadInput
    default_validators = [validate_mentions]


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = User


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "bio",
            "language",
            "default_timezone",
            "send_email_notifications",
            "activity_stream_filters",
            "show_sensitive_content",
            "show_external_images",
            "show_embedded_content",
        )
        widgets = {
            "notification_preferences": forms.CheckboxSelectMultiple,
            "activity_stream_filters": forms.CheckboxSelectMultiple,
            "avatar": ClearableImageInput,
        }

        labels = {
            "send_email_notifications": _(
                "Send me an email when I receive a new Message or Notification"
            ),
            "show_external_images": _(
                "Show external images embedded in Markdown and OpenGraph content"
            ),
            "show_sensitive_content": _(
                "Show sensitive content by default in public feeds"
            ),
            "show_embedded_content": _(
                "Show embedded content such as Youtube videos and tweets"
            ),
            "default_timezone": _("Timezone"),
        }

        help_texts = {
            "activity_stream_filters": _(
                "Filters only apply to other people's activities, not your own. "
                "Filters are mutually exclusive and may cancel each other out."
            ),
            "show_sensitive_content": _(
                "You can remove sensitive content completely from your feeds by "
                "blocking the relevant tags."
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fieldsets = FormHelper(
            self,
            (
                None,
                (
                    "name",
                    "avatar",
                    "language",
                    "default_timezone",
                    "send_email_notifications",
                    "bio",
                ),
            ),
            (
                _("Content Preferences"),
                (
                    "show_sensitive_content",
                    "show_external_images",
                    "show_embedded_content",
                    "activity_stream_filters",
                ),
            ),
        )
