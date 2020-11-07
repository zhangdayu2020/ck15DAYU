# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep


class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(1)
        self.driver.quit()
