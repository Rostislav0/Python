from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/registration1.html'

path_first_block = "//div[@class='first_block']"
path1 = path_first_block + "//input[contains(@class, 'first')]"
path2 = path_first_block + "//input[contains(@class, 'second')]"
path3 = path_first_block + "//input[contains(@class, 'third')]"

content = {'Ivan': path1,
           'Petrov': path2,
           'iv@mail.ru': path3}


try:
    browser.get(link)

    for c, input in content.items():
        browser.find_element(By.XPATH, input).send_keys(c)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(.5)
    browser.quit()
