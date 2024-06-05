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



class TestCartPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://seleniumdemo.com/?page_id=5")
        self.cart_page = CartPage(self.driver)


    def test_verify_describe_of_empty_cart(self):
        describe_empty_cart = self.driver.find_element(*CartPageLocators.cart_describe).text
        self.assertEqual(describe_empty_cart, CartPageElements.empty_cart_describe, "Elementy nie sa zgodne")

    def test_go_to_shop(self):
        self.cart_page.go_to_shop()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_shop_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_shop_page)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


