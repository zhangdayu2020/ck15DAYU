# -*- coding:utf-8 -*-
from appium import webdriver


class Test_app():
    def setup(self):
        self.desire_cap = {
            "platformName": "android",
            # adb devices的sn名称
            "deviceName": "127.0.0.1:7555",
            # 包名
            "appPackage": "",
            # activity名字
            "appActivity": "",
            "noReset": True,
            "unicodeKeyboard": True,
            "skipServerInstallation": True,
            "resetKeyBoard": True

        }


# 运行appium，前提是要打开appium server
self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
self.driver.implicitly_wait(10)
work_desk = self.driver.find
