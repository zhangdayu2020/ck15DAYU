# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


class ContactAddPage:
    def __init__(self, driver):
        self.driver = driver

    def add_contact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()

        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
            phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        return True
