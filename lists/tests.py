from django.test import TestCase
#resolve is Django's internal function to resolve URL's
#and find what view function they map to
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        # creates an HttpRequest object which is what Django sees
        # when a user's browser asks for a page
        # pass the HttpRequest object to our home_page view which
        # returns a response which is instance of class HttpResponse
#instead of manually creating an HTTPRequests self.client.get with the URL
#creates it
        response = self.client.get('/')

#this is the test method that the Django TestCase class prviodes us to let us
#check what template was used to render a response
        self.assertTemplateUsed(response, 'home.html')
