from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseElement(object):
    def __init__(self, driver, locator, by):
        self.driver = driver
        self.locator = locator
        self.by = by

        self.web_element = None

    def find(self):
        element = WebDriverWait(self.driver, 10).until()
