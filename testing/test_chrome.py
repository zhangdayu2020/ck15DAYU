from time import sleep, time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_chrome:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_01(self):
        self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element(By.XPATH, '//*[contains(text(),"精华帖")]').click()

        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@data-tag-name="精华帖"]')) >100
        # WebDriverWait(self.driver, 10).until(wait)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@data-tag-name="精华帖"]')))
        self.driver.find_element(By.XPATH, '//*[contains(text(),"测试开发")]').click()
