# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo1.page.add_member_page import Add_Member_page
from web.podemo1.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver= webdriver.Chrome(options=options)
    #     self.driver.implicitly_wait(5)
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def main_go_add_member_page(self):
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        return Add_Member_page(self.driver)

    def contact_go_add_member_page(self):
        sleep(3)
        self.find(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        self.find(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        # self.find(By.XPATH,'//div[@class="ww_operationBar"]//a[@class="qui_btn ww_btn js_add_member"]').click()
        locator = (By.XPATH, '//div[@class="ww_operationBar"]//a[@class="qui_btn ww_btn js_add_member"]')

        # element = self.wait_for_click(locator)
        # element.click()
        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)
        return Add_Member_page(self.driver)
