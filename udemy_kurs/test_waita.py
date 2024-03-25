from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

print("I have arrived")
WebDriverWait(browser, 10).until(alert_is_present())
print("An alert appeared")





