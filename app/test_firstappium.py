# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
# from hamcrest import *
from appium import webdriver
import pytest
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_app():
    def setup(self):
        desire_cap = {
            # 设置caps的值
            # 默认是Android
            "platformName": "android",
            # adb devices的sn名称
            # "deviceName": "127.0.0.1:7555",
            "deviceName": "emulator-5554",
            # 包名
            "appPackage": "com.xueqiu.android",
            # activity名字
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyboard": True,
            "skipServerInstallation": True,
            "resetKeyBoard": True,
            # "automationName": "uiautomator1"

        }
        # 运行appium，前提是要打开appium server
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

    # @pytest.mark.skip()
    def test_firstappium(self):
        sleep(10)
        el8 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el8.click()
        el9 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el9.click()
        el9.send_keys("alibaba")
        el10 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]")
        el10.click()
        el11 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/current_price']")
        print(el11.text)
        # assert el11.text==300
        assert_that(el11.text, close_to(300, 5))

        self.driver.quit()

    @pytest.mark.skip()
    def test_2rd_appium(self):
        sleep(10)
        el8 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(el8.is_enabled())
        print(el8.get_attribute("name"))
        print(el8.size)
        print(el8.rect)
        print(el8.location)
        el8.click()
        el9 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el9.click()
        el9.send_keys("alibaba")
        el10 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]")
        print(el10.get_attribute("displayed"))

    @pytest.mark.skip()
    def test_app_touchaction(self):
        sleep(10)
        touchme = TouchAction(self.driver)
        print(self.driver.get_window_rect())
        win_rect = self.driver.get_window_rect()
        win_rect_width = win_rect['width']
        win_rect_height = win_rect['height']
        touchme.press(x=win_rect_width * 0.5, y=0.8 * win_rect_height).wait(200).move_to(x=win_rect_width * 0.5,
                                                                                         y=0.2 * win_rect_height).release().perform()

    @pytest.mark.skip()
    def test_ffourappium(self):
        sleep(10)
        el8 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el8.click()
        el9 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el9.click()
        el9.send_keys("alibaba")
        el10 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]")
        el10.click()

        el11 = (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(el11))
        self.driver.find_element(*el11)

    @pytest.mark.skip()
    def test_hamcrest(self):
        assert_that(10, equal_to(2 * 5))

    @pytest.mark.parametrize('searchkey,type,price', [
        ('alibaba', 'BABA', 180),
        ('xiaomi', '01810', 10)
    ])
    def test_mul_data(self, searchkey, type, price):
        # sleep(10)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        current_price = self.driver.find_element_by_xpath(
            f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert_that(current_price, close_to(price, price * 0.1))
