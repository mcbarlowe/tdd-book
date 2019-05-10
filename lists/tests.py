from django.test import TestCase
#resolve is Django's internal function to resolve URL's
#and find what view function they map to
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item

# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_home_template(self):
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

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


