import time

from .page import *


class LoginPageActions(BasePage):
    def __init__(self, driver, login_page):
        super().__init__(driver)
        self.login_page = login_page
        self.name = None
        self.user = None
        self.user_email = None

    def register(self):
        self.driver.get("https://ethereal.email/")
        self.login_page.click_register_ethereal()
        user_email = self.driver.find_element(*LoginPageLocators.username_ethereal).text
        print(user_email) #wyswietlenie utworzonego adresu email
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        self.login_page.set_register_username(user_email)
        self.user_email = user_email
        self.login_page.set_register_password(LoginPageElements.user_password_pass) #wpisanie maila
        self.login_page.click_register_button()
        self.user = user_email[:-15] #usuniecie domeny z maila
        name = self.driver.find_element(*LoginPageLocators.name_in_my_account).text #pobranie nazwy użytkownika po zarejestrowaniu
        self.name = name

class CartPageActions(BasePage):
    def __init__(self, driver, cart_page):
        super().__init__(driver)
        self.cart_page = cart_page


    def set_product_in_basket_and_go_to_order(self):
        self.driver.get("http://seleniumdemo.com")
        self.cart_page.set_cookies_product()
        self.driver.get("http://seleniumdemo.com/?page_id=6")

    def fill_in_the_blanks_on_order(self):
        time.sleep(2)
        self.cart_page.fill_first_name()
        time.sleep(1)
        self.cart_page.fill_last_name()
        time.sleep(1)
        self.cart_page.fill_company_name()
        time.sleep(1)
        self.cart_page.fill_street_name()
        time.sleep(1)
        self.cart_page.fill_postcode()
        time.sleep(1)
        self.cart_page.fill_city()
        time.sleep(1)
        self.cart_page.fill_phone()
        time.sleep(1)
        self.cart_page.fill_email()
        time.sleep(1)
        self.cart_page.click_button_place_order()

