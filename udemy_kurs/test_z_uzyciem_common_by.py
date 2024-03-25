from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/trial-of-the-stones")
# Riddle of Stones
stone_input = browser.find_element(By.ID, "r1Input")
stone_answer_butn = browser.find_element(By.ID, "r1Btn")
stone_result = browser.find_element(By.ID, "passwordBanner")

# Riddle of Secrets
secrets_input = browser.find_element(By.ID, "r2Input")
secrets_answer_butn = browser.find_element(By.ID, "r2Butn")

# Two Merchants
# Simple Aproach
richest_merchant_name = browser.find_element(By.ID, "r3Input")
merchant_input = browser.find_element(By.ID, "r3Butn")
merchant_answer_butn = browser.find_element(By.ID, "successBanner2")

check_butn = browser.find_element(By.ID, 'checkButn')

complete_msg = browser.find_element(By.ID, 'trialCompleteBanner')

# Run script

stone_input.send_keys('rock')
stone_answer_butn.click()
password = stone_result.text

secrets_input.send_keys(password)
secrets_answer_butn.click()

merchant_input.send_keys(richest_merchant_name)
merchant_answer_butn.click()

check_butn.click()
assert complete_msg.text == 'Trial Complete'
