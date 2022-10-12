from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(.5)

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    answer = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(answer)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

    alert = browser.switch_to.alert
    affirm = alert.text.split()[-1]
    pyperclip.copy(affirm)
    print(affirm)

finally:
    browser.quit()
