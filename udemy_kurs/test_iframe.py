from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/iframe-training")

iframe = browser.find_element(By.XPATH, "//iframe[@src='https://techstepacademy.com/training-ground']")

browser.switch_to.frame(iframe)
browser.find_element(By.ID, 'ipt1')

browser.switch_to.default_content()




