import shelve
from time import sleep
import pytest
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase1():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.skip
    def test_case1(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(550, 691)
        sleep(5)
        self.driver.find_element(By.LINK_TEXT, "热门").click()
        self.driver.find_element(By.LINK_TEXT, "测试内推").click()
        sleep(5)

    @pytest.mark.skip
    def test_cookies(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [{
            'domain': '.ceshiren.com',
            'httpOnly': False,
            'name': 'Hm_lpvt_214f62eef822bde113f63fedcab70931',
            'path': '/',
            'secure': False,
            'value': '1603371031'
        }, {
            'domain': 'ceshiren.com',
            'expiry': 1608554796,
            'httpOnly': True,
            'name': '_t',
            'path': '/',
            'sameSite': 'Lax',
            'secure': True,
            'value': '84fa74b34a4e7a50dfbb17949fb368f3'
        }, {
            'domain': '.ceshiren.com',
            'expiry': 1666443030,
            'httpOnly': False,
            'name': '_ga',
            'path': '/',
            'secure': False,
            'value': 'GA1.2.1624453234.1600599983'
        }, {
            'domain': '.ceshiren.com',
            'expiry': 1634907031,
            'httpOnly': False,
            'name': 'Hm_lvt_214f62eef822bde113f63fedcab70931',
            'path': '/',
            'secure': False,
            'value': '1603118118,1603286451,1603309392,1603370796'
        }, {
            'domain': '.ceshiren.com',
            'expiry': 1603457430,
            'httpOnly': False,
            'name': '_gid',
            'path': '/',
            'secure': False,
            'value': 'GA1.2.1731964274.1603286451'
        }, {
            'domain': 'ceshiren.com',
            'httpOnly': True,
            'name': '_forum_session',
            'path': '/',
            'sameSite': 'Lax',
            'secure': True,
            'value': 'OFQ3dG1UMVo3VjlIZitQa1BPRG5ybm5NUDBPU0RPTjM1ZzZTbTgvK1RZelNjV2hMTC94eGQ0ZXlOcE4zU3M5dkEvaVVPRHJpU25UdVU0YUswc2dvUmZ3eDlmSCt1VElicm80a3dyK0MwMXdPUWsyWHJtYkFGdVhIa1ByK0UyYmRTd1Bxc3RkV0hTdlZvYU1jMWRCRUJMdHM2cXBwWEpYWCtGNXllZ2FBcFFvd0daSlZ3SFBEYSs0RENrTW92MkEzRU1jbmJ5Z3Y4VERnN25pdmVnTjRKSEtSSW84R2FkQzJpTkZmVVgza3diL01qcWh6OHJvODUyVnNFMkNCTW04Umo5aHpGYjdJQ0RRVUNpM0VVMlRVdElRREVVVlpleDhXSWZWYXZWalNQK01GTVhXTzNvUFA0bkxiRFlNZ0I1UngtLTl4dkJTVTVIMS96SWs0NWhrUG1aVUE9PQ%3D%3D--caa614a1598f243718eab59d838e06a85374a0cb'
        }]
        db = shelve.open("cookies")
        db['cookie'] = cookies
        db.close()
        self.driver.get("https://ceshiren.com/")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(10)

    def test_shelve(self):
        cookies = [{
            'domain': '.ceshiren.com',
            'httpOnly': False,
            'name': 'Hm_lpvt_214f62eef822bde113f63fedcab70931',
            'path': '/',
            'secure': False,
            'value': '1603371031'
        }, {
            'domain': 'ceshiren.com',
            'expiry': 1608554796,
            'httpOnly': True,
            'name': '_t',
            'path': '/',
            'sameSite': 'Lax',
            'secure': True,
            'value': '84fa74b34a4e7a50dfbb17949fb368f3'
        }, {
            'domain': '.ceshiren.com',
            'expiry': 1666443030,
            'httpOnly': False,
            'name': '_ga',
            'path': '/',
            'secure': False,
            'value': 'GA1.2.1624453234.1600599983'
        }, {
            'domain': '.ceshiren.com',
            'expiry': 1634907031,
            'httpOnly': False,
            'name': 'Hm_lvt_214f62eef822bde113f63fedcab70931',
            'path': '/',
            'secure': False,
            'value': '1603118118,1603286451,1603309392,1603370796'
        }, {
            'domain': '.ceshiren.com',
            'expiry': 1603457430,
            'httpOnly': False,
            'name': '_gid',
            'path': '/',
            'secure': False,
            'value': 'GA1.2.1731964274.1603286451'
        }, {
            'domain': 'ceshiren.com',
            'httpOnly': True,
            'name': '_forum_session',
            'path': '/',
            'sameSite': 'Lax',
            'secure': True,
            'value': 'OFQ3dG1UMVo3VjlIZitQa1BPRG5ybm5NUDBPU0RPTjM1ZzZTbTgvK1RZelNjV2hMTC94eGQ0ZXlOcE4zU3M5dkEvaVVPRHJpU25UdVU0YUswc2dvUmZ3eDlmSCt1VElicm80a3dyK0MwMXdPUWsyWHJtYkFGdVhIa1ByK0UyYmRTd1Bxc3RkV0hTdlZvYU1jMWRCRUJMdHM2cXBwWEpYWCtGNXllZ2FBcFFvd0daSlZ3SFBEYSs0RENrTW92MkEzRU1jbmJ5Z3Y4VERnN25pdmVnTjRKSEtSSW84R2FkQzJpTkZmVVgza3diL01qcWh6OHJvODUyVnNFMkNCTW04Umo5aHpGYjdJQ0RRVUNpM0VVMlRVdElRREVVVlpleDhXSWZWYXZWalNQK01GTVhXTzNvUFA0bkxiRFlNZ0I1UngtLTl4dkJTVTVIMS96SWs0NWhrUG1aVUE9PQ%3D%3D--caa614a1598f243718eab59d838e06a85374a0cb'
        }]
        db = shelve.open("cookies")
        self.driver.get("https://ceshiren.com/")
        # db['cookie'] = cookies

        cookies = db['cookie']
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(8)
