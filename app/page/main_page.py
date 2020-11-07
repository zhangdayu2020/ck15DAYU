# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.addresslist_page import AddressListPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_message(self):
        pass

    def goto_address(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        return AddressListPage(self.driver)
