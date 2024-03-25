from .elements import BasePageElement
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


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

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*LoginPageLocators.GO_BUTTON)
        element.click()

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

    def click_go_to_shop(self):
        go_shop = self.driver.find_element(*LoginPageLocators.go_to_shop)
        go_shop.click()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
