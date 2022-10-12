from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element as pe
from selenium.webdriver.support.wait import WebDriverWait
import time
import math
import pyperclip



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    price = WebDriverWait(browser, 15).until(pe((By.ID, 'price'), '100'))

    button.click()

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    answer = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(answer)

    submit = browser.find_element(By.ID, "solve")
    submit.click()

    alert = browser.switch_to.alert
    affirm = alert.text.split()[-1]
    pyperclip.copy(affirm)
    print(affirm)

finally:
    browser.quit()