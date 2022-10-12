from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/find_xpath_form'

browser = webdriver.Chrome()

try:
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')  # first name
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, 'last_name')  # last name
    input2.send_keys('Petrov')

    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')  # city
    input3.send_keys('Smolensk')

    input4 = browser.find_element(By.ID, 'country')  # country
    input4.send_keys('Russia')

    button = browser.find_element(By.XPATH, "//*[text() = 'Submit']")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
