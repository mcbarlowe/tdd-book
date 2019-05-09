from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    # setUp methods of test classes are executed before each test
    def setUp(self):
        self.browser = webdriver.Firefox()

    # tearDown methods run after each test method
    def tearDown(self):
        self.browser.quit()

    # all test method names start with the actual word test
    def test_can_start_a_list_and_retrieve_it_later(self):

        # gets homepage
        self.browser.get('http://localhost:8000')

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
        inputbox.send_keys(Keys.ENTER)
#time.sleep() is there to make sure the browser has finished loading
#before any assertions are made. This is called an explicit wait
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
#any() checks if any item in the iterable is true and returns true if so. This
#also works with dictionaries but only returns if any of the keys are True not
#the values
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows)
                )

        # fail just fails no matter what and produces the error message
        # serves as reminder to finish the actual test
        self.fail('Finish the test!')

if __name__ == '__main__':
    # this runs all my test classes when the scrip is run
    unittest.main(warnings='ignore')

