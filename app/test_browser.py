# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver


class Test_app:
    def setup(self):
        desire_cap = dict(appPackage="com.tencent.mm", appActivity="com.tencent.mm.ui.LauncherUI",
                          platformName="android", deviceName="127.0.0.1:7555", noReset=True, unicodeKeyboard=True,
                          resetKeyBoard=True, chromedriverExecutable="D:/download/chromedriver/chromedriver_52.exe")
        desire_cap['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'}
        desire_cap['adbport'] = 5038

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(30)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

    def find_top_window(self):
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
            else:
                self.driver.switch_to.window(window)

    def test_enter_micro_program(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.9)
        sleep(10)
        # self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
        # self.driver.find_element(By.XPATH, "//*[@text='取消']")
        # self.driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("雪球")
        # self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        # self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(MobileBy.ID, "com.tencent.mm:id/cna").click()
        sleep(10)
        self.driver.find_element(By.XPATH, "//*[@text='自选']")

        # 进入webview
        sleep(30)
        contexts = self.driver.contexts
        print(contexts)
        print(self.driver.page_source)
        self.driver.switch_to.context('WEBVIEW_xweb')
        # self.driver.switch_to.context(contexts[1])
        contexts = self.driver.contexts
        print(contexts)
        self.driver.implicitly_wait(10)
        self.find_top_window()

        # css定位
        self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # 等待新窗口
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # 输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys("alibaba").perform()
        # 点击
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item").click()

    def teardown(self):
        # self.driver.quit()
        pass
