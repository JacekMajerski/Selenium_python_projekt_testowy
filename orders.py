import unittest

import selenium.webdriver.support.expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.page import *
from pom.elements import *
from pom.locators import *
from pom.actions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains



class TestOrdersPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://seleniumdemo.com/?page_id=5")
        self.cart_page = CartPage(self.driver)
        self.shop_page = ShopPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.orders_page = OrdersPage(self.driver)

    def test_go_to_product_site(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        actions.fill_in_the_blanks_on_order()
        self.cart_page.click_button_place_order()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrdersPageLocators.order_notice))
        self.orders_page.click_product()
        if (self.driver.current_url == MainPageElements.url_bdd_cucumber):
            print('Url address is as expected')
        else:
            print('Url address is not as expected')
        self.assertEqual(self.driver.current_url, MainPageElements.url_bdd_cucumber)

    def test_visibility_order_number(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        actions.fill_in_the_blanks_on_order()
        self.cart_page.click_button_place_order()
        try:
            # Czekaj aż element stanie się widoczny
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrdersPageLocators.order_number)
            )
            # Asercja sprawdzająca, czy element jest widoczny
            self.assertTrue(element.is_displayed(), "order is not visible.")
            print("order number is visible.")
        except TimeoutException:
            self.fail("order is not visible.")
    def test_visibility_order_date(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        actions.fill_in_the_blanks_on_order()
        self.cart_page.click_button_place_order()
        try:
            # Czekaj aż element stanie się widoczny
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrdersPageLocators.order_date)
            )
            # Asercja sprawdzająca, czy element jest widoczny
            self.assertTrue(element.is_displayed(), "date is not visible.")
            print("order date is visible.")
        except TimeoutException:
            self.fail("date is not visible.")

    def test_visibility_order_price(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        actions.fill_in_the_blanks_on_order()
        self.cart_page.click_button_place_order()
        try:
            # Czekaj aż element stanie się widoczny
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrdersPageLocators.order_price)
            )
            # Asercja sprawdzająca, czy element jest widoczny
            self.assertTrue(element.is_displayed(), "price is not visible.")
            print("order price is visible.")
        except TimeoutException:
            self.fail("price is not visible.")

    def test_visibility_order_payment_method(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        actions.fill_in_the_blanks_on_order()
        self.cart_page.click_button_place_order()
        try:
            # Czekaj aż element stanie się widoczny
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrdersPageLocators.order_payment_method)
            )
            # Asercja sprawdzająca, czy element jest widoczny
            self.assertTrue(element.is_displayed(), "payment method is not visible.")
            print("order payment method is visible.")
        except TimeoutException:
            self.fail("payment method is not visible.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


