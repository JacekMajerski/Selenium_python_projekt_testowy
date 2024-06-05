import unittest

import selenium.webdriver.support.expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.page import *
from pom.elements import *
from pom.locators import *
from pom.actions import LoginPageActions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains



class TestOrdersPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page = CartPage(self.driver)

    """TESTS IN PROGRESS"""
    """TESTS IN PROGRESS"""
    """TESTS IN PROGRESS"""
    """TESTS IN PROGRESS"""
    """TESTS IN PROGRESS"""
    """TESTS IN PROGRESS"""
    """TESTS IN PROGRESS"""
    """TESTS IN PROGRESS"""
    """TESTS IN PROGRESS"""



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


