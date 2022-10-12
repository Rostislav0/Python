from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()


try:
    browser.get(link)

    num1 = int(browser.find_element(By.CSS_SELECTOR, "span[id='num1']").text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, "span[id='num2']").text)
    num_answer = num1 + num2

    dropdown = Select(browser.find_element(By.CSS_SELECTOR, "select[id='dropdown']"))
    dropdown.select_by_value(str(num_answer))

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()
    
finally:
    time.sleep(3)
    browser.quit()
