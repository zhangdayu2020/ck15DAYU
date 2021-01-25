# -*- coding:utf-8 -*-
import shelve
from time import time, sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_wechat():
    def setup_method(self, method):

        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options = options)
        path="/usr/local/bin/chromedriver"
        # self.driver = webdriver.Chrome(executable_path=path)
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()

    def test_wewechat1(self):
        self.driver.get("https://work.weixin.qq.com/")
        cookies = self.driver.get_cookies()
        print(cookies)
        # cookies1 = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'm4BUWOO3MfH-9JuklVdLLBEa193aTMZwIKPDYijoMfdb5dY-8D2wdlQAdvrcKL9yG3saIZB0sQYp_TVFqhhAhB7ldBe-UNhUfqBD9HEoftmeab3qtxi_LG9Hn1e2wK-wu1GX7OF_fK5gmuM9xYZ9bikiLScw9qjVuLeRg-1qzLmDj_VYqq_gMyHlxXURQcMcvspxCCgyXNo00BL01-kt8t3txLPEFH_bEB19KwBTIWCQDBjsMx7sZmoqzfQE5yKZ3s8xIEB4UOgIwAEf9x5aZA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688851259514876'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324960167407'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'Oyghq3DTZQqXGnPxf1KDyyiGmjvBuj1XVhIjdISfIGtZQkvfiIfgWSIHNX5Kzgra'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a2372501'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635005658, 'httpOnly': False,
        #                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #                             'value': '1603466573,1603466875,1603469000,1603469659'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '1912294772855609'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.qq.com', 'expiry': 1603469719, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': False, 'value': '2037976064'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1603498103, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '1vhljlr'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688851259514876'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634904086, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.qq.com', 'expiry': 1603556073, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.661382947.1603466574'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1606061676, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1603469659'},
        #     {'domain': '.qq.com', 'expiry': 1666541673, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.2145941178.1603368090'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '8619133397'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        for cookie in cookies1:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(5)
        self.driver.find_element_by_link_text("通讯录").click()
        sleep(5)

    def test_wewechat2(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("cookies1")
        # db["new_cookie"] = cookies1
        cookies = db["new_cookie"]
        db.close()
        for c in cookies:
            self.driver.add_cookie(c)
        self.driver.refresh()
        sleep(5)
