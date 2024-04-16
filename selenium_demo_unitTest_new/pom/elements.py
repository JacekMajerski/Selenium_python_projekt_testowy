from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).clear()
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute("value")

class LoginPageElements(object):
    user_email = 'jmajerski09@dkj.m4u.pl'
    user_password_pass ="Listopad2022"
    user_password_fail ="Listopad"
    notify_incorrect_login = "ERROR: Too many failed login attempts. Please try again"
    notify_reset_email = "Password reset email has been sent."
class MainPageElements(object):
    url_main_page = "http://seleniumdemo.com/"
    url_shop_page = "http://seleniumdemo.com/?post_type=product"
    url_cart_page = "http://seleniumdemo.com/?page_id=5"
    describe_search = "Search"
    search_java = "java"
    search_result = "Java Selenium WebDriver"