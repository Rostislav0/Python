import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def conn_brow(self):
        self.browser = webdriver.Chrome()

    def fill_form(self, link):
        path_first_block = "//div[@class='first_block']"
        path1 = path_first_block + "//input[contains(@class, 'first')]"
        path2 = path_first_block + "//input[contains(@class, 'second')]"
        path3 = path_first_block + "//input[contains(@class, 'third')]"

        content = {'Ivan': path1,
                   'Petrov': path2,
                   'iv@mail.ru': path3}

        self.conn_brow()
        self.browser.implicitly_wait(5)
        self.browser.get(link)

        for c, input in content.items():
            self.browser.find_element(By.XPATH, input).send_keys(c)

        button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_reg1(self):
        try:
            link = 'http://suninjuly.github.io/registration1.html'
            welcome_text = self.fill_form(link)

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "Should be equal text")

        finally:
            self.browser.quit()

    def test_reg2(self):
        try:
            link = 'http://suninjuly.github.io/registration2.html'
            welcome_text = self.fill_form(link)

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "Should be equal text")

        finally:
            self.browser.quit()


if __name__ == "__main__":
    unittest.main()
