# -*- coding:utf-8 -*-

"""
app.py module for app action
eg:start app, restart app, stop app, goto main page
"""
from appium import webdriver

from app.page.main_page import MainPage


class App:

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # noReset 保留缓存， 比如登录状态
        caps["noReset"] = "True"
        # 不停止应用，直接运行测试用例
        # caps["dontStopAppOnReset"] = "true"
        caps['skipDeviceInitialization'] = 'true'
        caps['skipServerInstallation'] = 'true'
        # caps["settings[waitForIdleTimeout]"] = 0
        # 关键  localhost:4723  本机ip:server端口
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        sleep(30)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def goto_main(self) -> MainPage:
        return MainPage()
