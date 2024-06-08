from telnetlib import EC



from .elements import *
from .locators import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    locator = 'q'

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""
    search_text_element = SearchTextElement()

    def click_go_to_shop(self):
        go_shop = self.driver.find_element(*MainPageLocators.go_to_shop)
        go_shop.click()


    def click_go_to_cart_main_menu(self):
        go_cart = self.driver.find_element(*MainPageLocators.go_to_cart_main_menu)
        go_cart.click()


    def click_go_to_cart_icon(self):
        go_cart_icon = self.driver.find_element(*MainPageLocators.go_to_cart_icon)
        go_cart_icon.click()


    def click_search_engine(self):
        search_engine = self.driver.find_element(*MainPageLocators.go_to_search)
        search_engine.click()


    def click_search_field(self):
        search_field = self.driver.find_element(*MainPageLocators.search_describe)
        search_field.click()


    def set_search(self, search_query):
        set_query = self.driver.find_element(*MainPageLocators.search_field)
        set_query.clear()
        set_query.send_keys(search_query)
        set_query.send_keys(Keys.RETURN)

    def click_go_to_shop_from_banner(self):
        button_shop = self.driver.find_element(*MainPageLocators.button_shop_banner)
        button_shop.click()

    def click_go_to_second_post(self):
        go_second_post = self.driver.find_element(*MainPageLocators.second_post_icon)
        go_second_post.click()

    def click_go_to_hello_world(self):
        go_to_hello_world = self.driver.find_element(*MainPageLocators.hello_world_icon)
        go_to_hello_world.click()

class LoginPage(BasePage):  # Dodano dziedziczenie po BasePage
    username_textbox = (By.ID, 'username')
    password_textbox = (By.ID, 'password')
    login_button = (By.CSS_SELECTOR, "[name='login']")
# jaki to ma sens? co to robi? po co w takim razie plik z lokalizatorami?
    def set_username(self, username):
        username_element = self.driver.find_element(*LoginPageLocators.username_textbox)
        username_element.clear()
        username_element.send_keys(username)

    def set_password(self, password):
        password_element = self.driver.find_element(*LoginPageLocators.password_textbox)
        password_element.clear()
        password_element.send_keys(password)

    def set_register_username(self, username):
        username_element = self.driver.find_element(*LoginPageLocators.register_username_textbox)
        username_element.clear()
        username_element.send_keys(username)

    def set_register_password(self, password):
        password_element = self.driver.find_element(*LoginPageLocators.register_password_textbox)
        password_element.clear()
        password_element.send_keys(password)
    def find_error_message_element(self):
        try:
            # Znajdujemy element zawierający komunikat o błędzie logowania
            error_message_element = self.driver.find_element(*LoginPageLocators.not_correct_password)
            return error_message_element
        except NoSuchElementException:
            # Jeśli element nie został znaleziony, zwracamy None
            return None

    def click_login_button(self):
        login_button_element = self.driver.find_element(*LoginPageLocators.login_button)
        login_button_element.click()

    def click_register_button(self):
        login_button_element = self.driver.find_element(*LoginPageLocators.register_button)
        login_button_element.click()

    def click_register_ethereal(self):
        create_account_button = self.driver.find_element(*LoginPageLocators.create_account_button)
        create_account_button.click()

    def get_email_ethereal(self, user_email):
        user_email = self.driver.find_element(*LoginPageLocators.username_ethereal).text
        print(user_email)

    def click_lost_your_password(self):
        lost_password = self.driver.find_element(*LoginPageLocators.lost_your_password)
        lost_password.click()

    def click_reset_password(self):
        reset_password = self.driver.find_element(*LoginPageLocators.reset_password_button)
        reset_password.click()

    def click_logout(self):
        logout = self.driver.find_element(*LoginPageLocators.logout_my_account)
        logout.click()

    def set_lost_email(self, email):
        lost_email = self.driver.find_element(*LoginPageLocators.lost_user_login)
        lost_email.clear()
        lost_email.send_keys(email)

    def click_breadcrumbs_to_main_page(self):
        bread_main_page = self.driver.find_element(*LoginPageLocators.breadcrumbs_my_account)
        bread_main_page.click()

class ShopPage(BasePage):  # Dodano dziedziczenie po BasePage
    def click_add_to_cart_bdd(self):
        add_to_cart = self.driver.find_element(*ShopPageLocators.button_add_to_cart_bdd)
        add_to_cart.click()

    def hover_the_mouse_over_the_basket(self):
        hover_basket = self.driver.find_element(*ShopPageLocators.number_in_icon_basket)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_basket).perform()

    def go_to_cart_page(self):
        go_to_cart = self.driver.find_element(*ShopPageLocators.button_view_cart)
        go_to_cart.click()

    def go_to_order_page(self):
        go_to_cart = self.driver.find_element(*ShopPageLocators.button_checkout)
        go_to_cart.click()

class CartPage(BasePage):
    def fill_input(self, locator, value):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.clear()
            element.send_keys(value)
        except Exception as e:
            print(f"Error interacting with element {locator}: {e}")
    def go_to_shop(self):
        go_to_shop = self.driver.find_element(*CartPageLocators.button_return_to_shop)
        go_to_shop.click()

    def set_cookies_product(self):
        self.driver.get("http://seleniumdemo.com/")
        cookie_hash = {
            'name': 'woocommerce_cart_hash',
            'value': '5c2c0a8be83a1306d87c17469a3dfffd',
        }
        cookie_item = {
            'name': 'woocommerce_items_in_cart',
            'value': '1',
        }
        cookie_session = {
            'name': 'wp_woocommerce_session_7c35fe1dca10889b305dae662226b0f6',
            'value': '0ddb9de40906abea730d05d5703e4cdd%7C%7C1718013685%7C%7C1718010085%7C%7C49bd7d7e9723a7c39a3a8eeb621ffad4',
        }
        self.driver.add_cookie(cookie_hash)
        self.driver.add_cookie(cookie_item)
        self.driver.add_cookie(cookie_session)


    def click_to_enter_coupon(self):
        enter_coupon = self.driver.find_element(*CartPageLocators.enter_code)
        enter_coupon.click()

    def fill_bad_code(self):
        fill_code = self.driver.find_element(*CartPageLocators.fill_code)
        fill_code.clear()
        fill_code.send_keys(CartPageElements.bad_code)

    def click_apply_coupon(self):
        apply_coupon = self.driver.find_element(*CartPageLocators.button_apply_coupon)
        apply_coupon.click()




    def fill_first_name(self):
            self.fill_input(CartPageLocators.first_name, CartPageElements.name)

    def fill_last_name(self):
            self.fill_input(CartPageLocators.last_name, CartPageElements.last_name)

    def fill_company_name(self):
            self.fill_input(CartPageLocators.company_name, CartPageElements.company)

    def fill_street_name(self):
            self.fill_input(CartPageLocators.street_address, CartPageElements.address)

    def fill_street_optional_name(self):
            self.fill_input(CartPageLocators.street_address_optional, CartPageElements.address_apartment)

    def fill_postcode(self):
            self.fill_input(CartPageLocators.postcode, CartPageElements.postcode)

    def fill_city(self):
            self.fill_input(CartPageLocators.city, CartPageElements.city)

    def fill_phone(self):
            self.fill_input(CartPageLocators.phone, CartPageElements.phone)

    def fill_email(self):
            self.fill_input(CartPageLocators.email_address, LoginPageElements.user_email)

    def click_button_place_order(self):
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CartPageLocators.button_place_order)
            )
            element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
