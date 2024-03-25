from .elements import BasePageElement
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

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
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class LoginPage(BasePage):  # Dodano dziedziczenie po BasePage
    username_textbox = (By.ID, 'username')
    password_textbox = (By.ID, 'password')
    login_button = (By.CSS_SELECTOR, "[name='login']")
# jaki to ma sens? co to robi? po co w takim razie plik z lokalizatorami?
    def set_username(self, username):
        username_element = self.driver.find_element(*MainPageLocators.username_textbox)
        username_element.clear()
        username_element.send_keys(username)

    def set_password(self, password):
        password_element = self.driver.find_element(*self.password_textbox)
        password_element.clear()
        password_element.send_keys(password)

   # def check_notify_bad_password(self):
        #password_element = self.driver.find_element(*MainPageLocators.not_incorrect_password)


    def click_login(self):
        login_button_element = self.driver.find_element(*self.login_button)
        login_button_element.click()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
