import unittest
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
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


