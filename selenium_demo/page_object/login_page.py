from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, 'username')
        self.password_textbox = (By.ID, 'password')
        self.login_button = (By.CSS_SELECTOR, "[name='login']")

    def set_username(self, username):
        username_element = self.driver.find_element(*self.username_textbox)  # Poprawienie tej linii
        username_element.clear()
        username_element.send_keys(username)

    def set_password(self, password):
        password_element = self.driver.find_element(*self.password_textbox)  # Poprawienie tej linii
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        login_button_element = self.driver.find_element(*self.login_button)  # Poprawienie tej linii
        login_button_element.click()
