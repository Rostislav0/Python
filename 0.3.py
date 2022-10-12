from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/find_link_text'

text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    new_link = browser.find_element(By.PARTIAL_LINK_TEXT, text)
    new_link.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')  # first name
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, 'last_name')  # last name
    input2.send_keys('Petrov')

    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')  # city
    input3.send_keys('Smolensk')

    input4 = browser.find_element(By.ID, 'country')  # country
    input4.send_keys('Russia')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)

finally:
    browser.quit()