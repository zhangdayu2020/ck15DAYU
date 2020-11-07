# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage


class Add_Member_page(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_member(self, username, uniq_id, phone):
        self.find(By.CSS_SELECTOR, '#username').send_keys(username)
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(uniq_id)
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone)
        self.find(By.LINK_TEXT, '保存').click()
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)
        return True

    def get_member(self):
        contact_list = self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
        titlelist = []

        for element in contact_list:
            titlelist.append(element.get_attribute("title"))
        return titlelist
