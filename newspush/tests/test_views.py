from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip

class NewsAcquisitionViewTest(TestCase):
    def test_can_fetch_news_list_by_time(self):
        pass

    def test_can_fetch_news_list_by_academic(self):
        pass

    def test_can_fetch_news_list_by_search_keys(self):
        pass

    def test_can_fetch_specific_news(self):
        pass

class CommentsViewTest(TestCase):
    def test_can_commit_comment_by_news_id(self):
        pass

    def test_can_fetch_comment_by_news_id(self):
        pass

class NoticesViewTest(TestCase):
    def test_can_fetch_notices_list_by_time(self):
        pass

class DataUpdateViewTest(TestCase):
    def test_can_receive_a_new_data(self):
        pass
