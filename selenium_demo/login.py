from selenium import webdriver
from page_object.login_page import LoginPage

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()  # Poprawienie tej linii
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.set_username("aglae.corwin15@ethereal.email")
        self.login_page.set_password("Listopad2022")
        self.login_page.click_login()

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    test = TestLogin()
    test.setup_method()
    test.test_successful_login()
    test.teardown_method()



