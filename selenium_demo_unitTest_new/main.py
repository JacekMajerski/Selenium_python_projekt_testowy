import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.page import LoginPage, MainPage
from pom.elements import LoginPageElements, MainPageElements
from pom.locators import LoginPageLocators, MainPageLocators
from pom.actions import LoginPageActions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class TestMainPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://seleniumdemo.com/")
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    def test_go_to_shop(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element(*MainPageLocators.go_to_shop)
        a.move_to_element(m).perform()
        self.main_page.click_go_to_shop()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_shop_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_shop_page)

    def test_go_to_cart_main_menu(self):
        self.main_page.click_go_to_cart_main_menu()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_cart_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_cart_page)

    def test_go_to_cart_icon(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element(*MainPageLocators.go_to_cart_icon)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.go_to_cart_icon))
        a.move_to_element(m).perform()
        self.main_page.click_go_to_cart_icon()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_cart_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_cart_page)

    def test_search_engine(self):
        self.main_page.click_search_engine()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.search_describe))
        inscription = self.driver.find_element(*MainPageLocators.search_describe).text
        print(inscription)
        if (inscription == MainPageElements.describe_search):
            print('Napis na wyszukiwarce jest zgodny z oczekiwanym')
        else:
            print('Napis na wyszukiwarce jest niezgodny z oczekiwanym, lub strona wczytała się niepoprawnie')
        self.assertEqual(inscription, MainPageElements.describe_search)

    def test_search_engine_search_java(self):
        self.main_page.click_search_engine()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.search_describe))
        self.main_page.click_search_field()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.search_field))
        self.main_page.set_search(MainPageElements.search_java)
        result = self.driver.find_element(*MainPageLocators.search_results).text
        print(result)
        if (result == MainPageElements.search_result):
            print('Wyszukany element jest zgodny z oczekiwanym')
        else:
            print('Wyszukany element jest niezgodny z oczekiwanym')
        self.assertEqual(result, MainPageElements.search_result)

    def test_go_to_shop_from_banner(self):
        self.main_page.click_go_to_shop_from_banner()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_shop_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_shop_page)

    def test_go_to_second_post(self):
        self.main_page.click_go_to_second_post()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_second_post):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_second_post)

    def test_go_to_hello_world(self):
        self.main_page.click_go_to_hello_world()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_hello_world):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_hello_world)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


