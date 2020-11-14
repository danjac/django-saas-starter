# Copyright (c) 2020 by Dan Jacob
# SPDX-License-Identifier: AGPL-3.0-or-later

# Django
from django.core.exceptions import ValidationError

# Third Party Libraries
import pytest

# Local
from ..validators import validate_mentions


class TestValidateMentions:
    def test_none(self):
        validate_mentions(None)

    def test_empty(self):
        validate_mentions("")

    def test_valid_single_tag(self):
        validate_mentions("@danjc")

    def test_invalid_single_tag(self):
        with pytest.raises(ValidationError):
            validate_mentions("danjac")

    def test_valid_single_tag_with_spaces(self):
        validate_mentions("   @danjac    ")

    def test_multiple_tags(self):
        validate_mentions("@danjac @demo @other")

    def test_invalid_tag_in_many(self):
        with pytest.raises(ValidationError):
            validate_mentions("@danjac demo @other")
