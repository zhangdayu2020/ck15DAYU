# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage:
    def __init__(self, driver):
        self.driver = driver

    def click_addmember(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()

        return MemberInviteMenuPage(self.driver)
