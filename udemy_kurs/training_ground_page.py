from selenium.webdriver.common.by import By

from .page_object.base_element import BaseElement
from .page_object.base_page import BasePage

class TrainingGroundPage(BasePage):

    url = 'https://techstepacademy.com/training-ground/'

    def button1(self):
        locator = (By.ID, 'b1')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1])