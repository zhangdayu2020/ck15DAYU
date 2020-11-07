# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By


class Test_touchaction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element(By.ID, "kw")
        ele.send_keys("ruby study")
        search_btn = self.driver.find_element(By.ID, "su")
        action = TouchActions(self.driver)
        action.tap(search_btn)
        sleep(5)
        action.scroll_from_element(ele, 0, 10000)
        action.perform()
        sleep(5)
