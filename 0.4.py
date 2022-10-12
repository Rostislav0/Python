from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    inputs = browser.find_elements(By.TAG_NAME, 'input')

    for input in inputs:
        input.send_keys("I'm not robot")

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
