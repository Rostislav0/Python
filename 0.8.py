from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser.get(link)

    x = browser.find_element(By.XPATH, '//img[@valuex]').get_attribute('valuex')
    y = calc(x)

    string_answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    string_answer.send_keys(y)

    robotCheckbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    robotsRule.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()
