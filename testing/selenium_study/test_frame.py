# -*- coding:utf-8 -*-
from time import sleep

from testing.selenium_study.base import Base


class Test_frame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        self.driver.find_element_by_id('droppable').click()
        # self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content()
        print(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/form/div/div[1]/button').text)
