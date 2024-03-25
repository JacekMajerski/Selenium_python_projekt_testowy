from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')
    username_textbox = (By.ID, 'username')
    password_textbox = (By.ID, 'password')
    login_button = (By.CSS_SELECTOR, "[name='login']")
    not_incorrect_password = (By.XPATH, "//strong[.='ERROR']")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass

