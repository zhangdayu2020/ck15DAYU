# -*- coding:utf-8 -*-
from selenium import webdriver


class Test_form():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form1(self):
        self.driver.get("https://testerhome.com/account/sign_in")
