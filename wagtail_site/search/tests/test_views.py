from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse


class SearchTestCase(TestCase):
    def test_search_page_loads(self):
        res = self.client.get(reverse("search"))
        self.assertContains(res, "Search", status_code=HTTPStatus.OK)
