import unittest

import selenium.webdriver.support.expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.page import *
from pom.elements import *
from pom.locators import *
from pom.actions import *
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
        self.shop_page = ShopPage(self.driver)
        self.main_page = MainPage(self.driver)
    def test_verify_describe_of_empty_cart(self):
        describe_empty_cart = self.driver.find_element(*CartPageLocators.cart_describe).text
        self.assertEqual(describe_empty_cart, CartPageElements.empty_cart_describe, "Elements do not match")

    def test_go_to_shop(self):
        self.cart_page.go_to_shop()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_shop_page):
            print('Url address is as expected')
        else:
            print('Url address is not as expected')
        self.assertEqual(self.driver.current_url, MainPageElements.url_shop_page)

    def test_notyfication_adding_bad_coupon(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.click_to_enter_coupon()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(CartPageLocators.fill_code))
        self.cart_page.fill_bad_code()
        self.cart_page.click_apply_coupon()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(CartPageLocators.notify_bad_coupon))
        notify = self.driver.find_element(*CartPageLocators.notify_bad_coupon).text
        print(notify)
        if (notify == CartPageElements.notify_bad_code):
            print('Notification is as expected')
        else:
            print('Notification is not as expected')
        self.assertEqual(notify, CartPageElements.notify_bad_code)

    def test_first_name_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_first_name()
        name = self.driver.find_element(*CartPageLocators.first_name).get_attribute('value')
        print(name)
        if (name == CartPageElements.name):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(name, CartPageElements.name)

    def test_last_name_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_last_name()
        name = self.driver.find_element(*CartPageLocators.last_name).get_attribute('value')
        print(name)
        if (name == CartPageElements.last_name):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(name, CartPageElements.last_name)

    def test_company_name_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_company_name()
        name = self.driver.find_element(*CartPageLocators.company_name).get_attribute('value')
        print(name)
        if (name == CartPageElements.company):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(name, CartPageElements.company)

    def test_street_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_street_name()
        street = self.driver.find_element(*CartPageLocators.street_address).get_attribute('value')
        print(street)
        if (street == CartPageElements.address):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(street, CartPageElements.address)

    def test_street_additional_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_street_name()
        self.cart_page.fill_street_optional_name()
        street = self.driver.find_element(*CartPageLocators.street_address).get_attribute('value')
        street_number = self.driver.find_element(*CartPageLocators.street_address_optional).get_attribute('value')
        print(street, street_number)
        if (street == CartPageElements.address and street_number == CartPageElements.address_apartment):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(street, CartPageElements.address)
        self.assertEqual(street_number, CartPageElements.address_apartment)

    def test_postcode_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_postcode()
        postcode = self.driver.find_element(*CartPageLocators.postcode).get_attribute('value')
        print(postcode)
        if (postcode == CartPageElements.postcode):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(postcode, CartPageElements.postcode)
    def test_city_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_city()
        city = self.driver.find_element(*CartPageLocators.city).get_attribute('value')
        print(city)
        if (city == CartPageElements.city):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(city, CartPageElements.city)
    def test_phone_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_phone()
        phone = self.driver.find_element(*CartPageLocators.phone).get_attribute('value')
        print(phone)
        if (phone == CartPageElements.phone):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(phone, CartPageElements.phone)

    def test_email_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        self.cart_page.fill_email()
        email = self.driver.find_element(*CartPageLocators.email_address).get_attribute('value')
        print(email)
        if (email == LoginPageElements.user_email):
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')
        self.assertEqual(email, LoginPageElements.user_email)

    def test_notify_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        self.driver.get("http://seleniumdemo.com/?page_id=6")
        # Próba kliknięcia przycisku "place order" z obsługą wyjątku StaleElementReferenceException
        try:
            place_order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CartPageLocators.button_place_order))
            place_order_button.click()
        except selenium.common.exceptions.StaleElementReferenceException:
            place_order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CartPageLocators.button_place_order))
            place_order_button.click()

        # Oczekiwanie na pojawienie się błędu pierwszego imienia
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.first_name_error))

        # Pobranie tekstu błędu z elementu
        error_element = self.driver.find_element(*CartPageLocators.first_name_error)
        error = error_element.text
        print(error)

        if error == CartPageElements.first_name_error:
            print('The value entered is as expected')
        else:
            print('The value entered is not as expected')

        self.assertEqual(error, CartPageElements.first_name_error)

    def test_order_summary_verification(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.add_product_to_cart()
        actions.fill_in_the_blanks_on_order()
        self.cart_page.click_button_place_order()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrdersPageLocators.order_notice))
        notice = self.driver.find_element(*OrdersPageLocators.order_notice).text
        if (notice == OrdersPageElements.order_notice):
            print('Notification is as expected')
        else:
            print('Notification is not as expected')
        self.assertEqual(notice, OrdersPageElements.order_notice)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


