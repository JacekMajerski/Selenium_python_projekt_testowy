import unittest
from selenium import webdriver
import pom.page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def test_successful_login(self):
        login_page = pom.page.LoginPage(self.driver)  # Poprawiona linia
        login_page.set_username("aglae.corwin15@ethereal.email")
        login_page.set_password("Listopad2022")
        login_page.click_login()

    def test_unsuccessful_login(self):
        login_page = pom.page.LoginPage(self.driver)  # Poprawiona linia
        login_page.set_username("aglae.corwin15@ethereal.email")
        login_page.set_password("Listopad")
        login_page.click_login()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
