# -*- coding:utf-8 -*-
from web.podemo1.page.main_page import MainPage


class Test_add_mem():

    def setup(self):
        self.main = MainPage()

    def test_add_mem1(self):
        username = "aaaa2"
        uniq_id = "13211111112"
        phone = "13211111112"
        # self.main.main_go_add_member_page().add_member(username,uniq_id,phone)
        self.main.contact_go_add_member_page().add_member(username, uniq_id, phone)
