# -*- coding:utf-8 -*-
from app.page.app import App


class Test_contact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = "hogwarts__002"
        gender = "男"
        phonenum = "13500000001"
        result = self.main.goto_address().click_addmember().add_member_manual()
        assert result
