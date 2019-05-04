from selenium import webdriver
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
        self.assertIn('To-Do', self.browser.title)
        # fail just fails no matter what and produces the error message
        # serves as reminder to finish the actual test
        self.fail('Finish the test!')

if __name__ == '__main__':
    # this runs all my test classes when the scrip is run
    unittest.main(warnings='ignore')

