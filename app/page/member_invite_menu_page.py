# -*- coding:utf-8 -*-
from app.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def add_member_manual(self):
        return ContactAddPage(self.driver)
