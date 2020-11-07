# -*- coding:utf-8 -*-
from web.podemo.index_page import IndexPage


class TestWX():
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        self.index.goto_register().register(username, uniq_id, phone)
