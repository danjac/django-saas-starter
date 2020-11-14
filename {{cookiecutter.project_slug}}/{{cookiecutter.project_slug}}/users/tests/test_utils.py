# Copyright (c) 2020 by Dan Jacob
# SPDX-License-Identifier: AGPL-3.0-or-later


# Local
from ..utils import extract_mentions, linkify_mentions, user_display


class TestUserDisplay:
    def test_user_display_with_name(self, user_model):
        user = user_model(name="Test Person")
        assert user_display(user) == "Test Person"

    def test_user_display_no_name(self, user_model):
        user = user_model(username="tester")
        assert user_display(user) == "tester"


class TestLinkifyMentions:
    def test_linkify(self):
        content = "hello @danjac"
        replaced = linkify_mentions(content)
        assert 'href="/people/danjac/"' in replaced

    def test_linkify_unicode(self):
        content = "hello @kesämies"
        replaced = linkify_mentions(content)
        assert 'href="/people/kesamies/"' in replaced


class TestExtractMentions:
    def test_extract(self):
        content = "hello @danjac and @weegill and @kesämies and @someone-else!"
        assert extract_mentions(content) == {
            "danjac",
            "weegill",
            "kesämies",
            "someone-else",
        }
