# -*- coding:utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        self.driver.find_element_by_css_selector("#corp_name").send_keys("youyu")
        self.driver.find_element_by_css_selector("#manager_name").send_keys("dayu")
        self.driver.find_element_by_css_selector("#submit_btn").click()
        return True
