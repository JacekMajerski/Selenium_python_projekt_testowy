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
        self.assertEqual(describe_empty_cart, CartPageElements.empty_cart_describe, "Elementy nie sa zgodne")

    def test_go_to_shop(self):
        self.cart_page.go_to_shop()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_shop_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_shop_page)

    def test_notyfication_adding_bad_coupon(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.click_to_enter_coupon()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(CartPageLocators.fill_code))
        self.cart_page.fill_bad_code()
        self.cart_page.click_apply_coupon()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(CartPageLocators.notify_bad_coupon))
        notify = self.driver.find_element(*CartPageLocators.notify_bad_coupon).text
        print(notify)
        if (notify == CartPageElements.notify_bad_code):
            print('Notyfikacja jest zgodna z oczekiwaną')
        else:
            print('Notyfikacja jest niezgodna z oczekiwaną')
        self.assertEqual(notify, CartPageElements.notify_bad_code)

    def test_first_name_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_first_name()
        name = self.driver.find_element(*CartPageLocators.first_name).get_attribute('value')
        print(name)
        if (name == CartPageElements.name):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(name, CartPageElements.name)

    def test_last_name_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_last_name()
        name = self.driver.find_element(*CartPageLocators.last_name).get_attribute('value')
        print(name)
        if (name == CartPageElements.last_name):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(name, CartPageElements.last_name)

    def test_company_name_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_company_name()
        name = self.driver.find_element(*CartPageLocators.company_name).get_attribute('value')
        print(name)
        if (name == CartPageElements.company):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(name, CartPageElements.company)

    def test_street_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_street_name()
        street = self.driver.find_element(*CartPageLocators.street_address).get_attribute('value')
        print(street)
        if (street == CartPageElements.address):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(street, CartPageElements.address)

    def test_street_additional_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_street_name()
        self.cart_page.fill_street_optional_name()
        street = self.driver.find_element(*CartPageLocators.street_address).get_attribute('value')
        street_number = self.driver.find_element(*CartPageLocators.street_address_optional).get_attribute('value')
        print(street, street_number)
        if (street == CartPageElements.address and street_number == CartPageElements.address_apartment):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(street, CartPageElements.address)
        self.assertEqual(street_number, CartPageElements.address_apartment)

    def test_postcode_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_postcode()
        postcode = self.driver.find_element(*CartPageLocators.postcode).get_attribute('value')
        print(postcode)
        if (postcode == CartPageElements.postcode):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(postcode, CartPageElements.postcode)
    def test_city_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_city()
        city = self.driver.find_element(*CartPageLocators.city).get_attribute('value')
        print(city)
        if (city == CartPageElements.city):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(city, CartPageElements.city)
    def test_phone_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_phone()
        phone = self.driver.find_element(*CartPageLocators.phone).get_attribute('value')
        print(phone)
        if (phone == CartPageElements.phone):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(phone, CartPageElements.phone)

    def test_email_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()
        self.cart_page.fill_email()
        email = self.driver.find_element(*CartPageLocators.email_address).get_attribute('value')
        print(email)
        if (email == LoginPageElements.user_email):
            print('Wpisana wartosc jest zgodna z oczekiwana')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')
        self.assertEqual(email, LoginPageElements.user_email)

    def test_notify_entry(self):
        actions = CartPageActions(self.driver, self.cart_page)
        actions.set_product_in_basket_and_go_to_order()

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
            print('Wpisana wartość jest zgodna z oczekiwaną')
        else:
            print('Wpisana wartość jest niezgodna z oczekiwaną')

        self.assertEqual(error, CartPageElements.first_name_error)

    def test_order_summary_verification(self):
        self.driver.delete_all_cookies()
        self.driver.get('http://seleniumdemo.com/')
        self.main_page.click_go_to_shop()
        self.shop_page.click_add_to_cart_bdd()
        self.shop_page.hover_the_mouse_over_the_basket()
        self.shop_page.go_to_order_page()

        self.driver.get("http://seleniumdemo.com/?page_id=6")

        actions = CartPageActions(self.driver, self.cart_page)
        actions.fill_in_the_blanks_on_order()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


