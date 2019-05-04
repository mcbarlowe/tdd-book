from django.test import TestCase
#resolve is Django's internal function to resolve URL's
#and find what view function they map to
from django.urls import resolve
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # checking that resolve of the root returns home_page
        # which will be stored in lists/views.py
        found = resolve('/')
        self.assertEqual(found.func, home_page)
