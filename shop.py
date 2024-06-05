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



class TestShopPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://seleniumdemo.com/?post_type=product")
        self.shop_page = ShopPage(self.driver)
        self.main_page = MainPage(self.driver)

    def test_add_to_basket_verify_button(self):
        self.shop_page.click_add_to_cart_bdd()
        try:
            # oczekiwanie na widocznosc elementu
            button_after_adding_to_cart = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(ShopPageLocators.button_after_adding_to_cart)
            )
            # Asercja sprawdzająca, czy element jest widoczny, jesli nie wyswietli sie komunikat
            self.assertTrue(button_after_adding_to_cart.is_displayed(), "The add to cart button is not visible")
        except TimeoutException:
            self.fail("The add to cart button was not found on the page")


    def test_add_to_basket_verify_number_on_basket(self):
        self.shop_page.click_add_to_cart_bdd()
        try:
            number_basket_element = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(ShopPageLocators.number_in_icon_basket))
            number_basket = number_basket_element.text
            self.assertEqual(number_basket, ShopPageElements.number_on_basket, "element is as expected")
        except TimeoutException:
            self.fail("the number icon is not visible")
        except AssertionError:
            self.fail( '- element is not expected')

    def test_verify_product_in_view_shopping_cart(self):
        self.shop_page.click_add_to_cart_bdd()
        product_name = self.driver.find_element(*ShopPageLocators.product_name_in_shop).text
        product_price = self.driver.find_element(*ShopPageLocators.product_price_in_shop).text
        self.shop_page.hover_the_mouse_over_the_basket()
        product_name_in_mini_basket = self.driver.find_element(*ShopPageLocators.product_name_in_mini_basket).text
        product_price_in_mini_basket = self.driver.find_element(*ShopPageLocators.product_price_in_mini_basket).text
        self.assertEqual(product_name, product_name_in_mini_basket, "nazwa produktu sie nie zgadza")
        self.assertEqual(product_price, product_price_in_mini_basket, "cena produktu sie nie zgadza")

    def test_verify_product_icon_in_view_shopping_cart(self):
        self.shop_page.click_add_to_cart_bdd()
        self.shop_page.hover_the_mouse_over_the_basket()
        icon_mini_basket = self.driver.find_element(*ShopPageLocators.icon_on_mini_basket)
        is_visible = icon_mini_basket.is_displayed()
        if is_visible:
            print("Element jest widoczny na stronie.")
        else:
            print("Element nie jest widoczny na stronie.")

    def test_verify_of_button_checkout_visibility_in_view_shopping_cart(self):
        self.shop_page.click_add_to_cart_bdd()
        self.shop_page.hover_the_mouse_over_the_basket()
        button_checkout = self.driver.find_element(*ShopPageLocators.button_checkout)
        is_visible = button_checkout.is_displayed()
        if is_visible:
            print("Element jest widoczny na stronie.")
        else:
            print("Element nie jest widoczny na stronie.")

    def test_verify_of_button_view_cart_visibility_in_view_shopping_cart(self):
        self.shop_page.click_add_to_cart_bdd()
        self.shop_page.hover_the_mouse_over_the_basket()
        button_view_cart = self.driver.find_element(*ShopPageLocators.button_view_cart)
        is_visible = button_view_cart.is_displayed()
        if is_visible:
            print("Element jest widoczny na stronie.")
        else:
            print("Element nie jest widoczny na stronie.")

    def test_go_to_cart_page(self):
        self.shop_page.click_add_to_cart_bdd()
        self.shop_page.hover_the_mouse_over_the_basket()
        self.shop_page.go_to_cart_page()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_cart_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_cart_page)

    def test_go_to_order_page(self):
        self.shop_page.click_add_to_cart_bdd()
        self.shop_page.hover_the_mouse_over_the_basket()
        self.shop_page.go_to_order_page()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_order_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_order_page)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


