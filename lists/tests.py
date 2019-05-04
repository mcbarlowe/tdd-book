from django.test import TestCase
#resolve is Django's internal function to resolve URL's
#and find what view function they map to
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # checking that resolve of the root returns home_page
        # which will be stored in lists/views.py
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # creates an HttpRequest object which is what Django sees
        # when a user's browser asks for a page
        request = HttpRequest()
        # pass the HttpRequest object to our home_page view which
        # returns a response which is instance of class HttpResponse
        response = home_page(request)
        # extract reponse which is stored in raw bytes and decode
        # it in utf8
        html = response.content.decode('utf8')
        # check to see if the page starts with <html> tag and that
        # the <title> tag has To-Do lists inside it and page ends with <html>
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)

        self.assertTrue(html.endswith('</html>'))
