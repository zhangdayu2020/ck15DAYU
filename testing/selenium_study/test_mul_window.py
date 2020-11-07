# -*- coding:utf-8 -*-
from time import sleep

from testing.selenium_study.base import Base


class Test_mulwindows(Base):

    def test_click(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.window_handles)

        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("april")

        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        sleep(3)
