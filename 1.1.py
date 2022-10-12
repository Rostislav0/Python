from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from os.path import abspath, join, dirname

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
content = ["Ivan", "Petrov", "Iv@mail.ru"]


try:
    browser.get(link)
    data = browser.find_elements(By.CLASS_NAME, "form-control")
    for d, c in zip(data, content):
        d.send_keys(c)

    current_dir = abspath(dirname(__file__))
    file_path = join(current_dir, '1.1(bio).txt')

    for_file = browser.find_element(By.ID, "file")
    for_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
