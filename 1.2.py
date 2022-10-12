from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(.5)

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    answer = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(answer)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

    alert = browser.switch_to.alert
    print(float(alert.text.split()[-1]))

finally:
    browser.quit()
