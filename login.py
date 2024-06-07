import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.page import LoginPage, MainPage
from pom.elements import LoginPageElements, MainPageElements
from pom.locators import LoginPageLocators, MainPageLocators
from pom.actions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class TestLoginPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    def test_successful_login(self):
        """Test successful login"""
        self.login_page.set_username(LoginPageElements.user_email)
        self.login_page.set_password(LoginPageElements.user_password_pass)
        self.login_page.click_login_button()
        name = self.driver.find_element(*LoginPageLocators.name_in_my_account).text
        user = LoginPageElements.user_email[:-11]
        self.assertIn(name, user)

    def test_register_success(self):
        self.driver.get("https://ethereal.email/")
        self.login_page.click_register_ethereal()
        user_email = self.driver.find_element(*LoginPageLocators.username_ethereal).text
        print(user_email)
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        self.login_page.set_register_username(user_email)
        self.login_page.set_register_password(LoginPageElements.user_password_pass)
        self.login_page.click_register_button()
        user = user_email[:-15]
        print(user)
        name = self.driver.find_element(*LoginPageLocators.name_in_my_account).text
        self.assertIn(name, user)

    def test_register_with_actions(self):
        actions = LoginPageActions(self.driver, self.login_page)
        actions.register()
        print(actions.name, actions.user)
        self.assertIn(actions.name, actions.user)

    def test_lost_password_with_actions(self):
        actions = LoginPageActions(self.driver, self.login_page)
        actions.register()
        self.login_page.click_logout()
        self.login_page.click_lost_your_password()
        self.login_page.set_lost_email(actions.user_email)
        self.login_page.click_reset_password()
        notify = self.driver.find_element(*LoginPageLocators.not_reset_email).text
        self.assertIn(notify, LoginPageElements.notify_reset_email)

    def test_breadcrumbs_from_my_account_to_main_page(self):
        self.login_page.click_breadcrumbs_to_main_page()
        print(self.driver.current_url)
        if (self.driver.current_url == MainPageElements.url_main_page):
            print('Adres Url jest zgodny z oczekiwanym')
        else:
            print('Adres Url jest niezgodny z oczekiwanym')
        self.assertEqual(self.driver.current_url, MainPageElements.url_main_page)

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

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    

