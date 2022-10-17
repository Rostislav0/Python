import pytest
import time
import math
from selenium.webdriver.common.by import By

links = '''https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1'''


@pytest.mark.parametrize('link', links.split())
class TestStepicAnswer:
    def test_correct(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(8)

        textarea = browser.find_element(By.CSS_SELECTOR, "textarea[id]")
        textarea.click()
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)

        button = browser.find_element(By.CLASS_NAME, 'submit-submission')
        button.click()

        text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        try:
            assert text == 'Correct!', f'expected "Correct!", but got "{text}"'
        except AssertionError:
            with open("2_0_test_Errors.log", "a") as file:
                file.write(text)
