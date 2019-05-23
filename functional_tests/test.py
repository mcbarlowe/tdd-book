'''Tests for our list website'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    # setUp methods of test classes are executed before each test
    def setUp(self):
        self.browser = webdriver.Firefox()

    # tearDown methods run after each test method
    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            #do the test as normal if it works then return
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            #if there's an exception wait a short amount of time and then
            #try the test again while the difference between times is less
            # than max wait
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    # all test method names start with the actual word test
    def test_can_start_a_list_and_retrieve_it_later(self):

        # gets homepage
        self.browser.get(self.live_server_url)

        # assertIn is a method from unittest class that checks to see if
        # the first item is in the second. assertNotIn checks the opposite
# this checks that To-Do is in the page title and header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

#find_element_by_tag_name, find_element_by_id and find_elements_by_tag_name
#are methods from Selenium to examine web pages. find_element_... returns an
#element and raises an exception if it can't find it, find_elements_... returns
#a list of elements found in the website which may be empty


        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
                )

#send_keys is Selenium's way of typing into input elemtns
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
#time.sleep() is there to make sure the browser has finished loading
#before any assertions are made. This is called an explicit wait
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # fail just fails no matter what and produces the error message
        # serves as reminder to finish the actual test
        self.fail('Finish the test!')


