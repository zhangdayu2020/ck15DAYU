from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_actionchains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element_by_xpath("//*[@value='click me']")
        ele_double_click = self.driver.find_element_by_xpath("//*[@value='dbl click me']")
        ele_right_click = self.driver.find_element_by_xpath("//*[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.double_click(ele_double_click)
        action.context_click(ele_right_click)
        action.perform()

    def test_move_to(self):
        self.driver.get("https://www.baidu.com/")
        ele_move = self.driver.find_element_by_xpath("//span[contains(text(),'设置')]")
        action = ActionChains(self.driver)

        action.move_to_element(ele_move)
        action.perform()
        sleep(5)

    def test_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")

        ele_drag = self.driver.find_element(By.XPATH, "//*[@id='dragger']")
        ele_drop1 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Item 1')]")
        ele_drop2 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Item 2')]")
        ele_drop3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Item 3')]")
        ele_drop4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Item 4')]")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop1)
        action.drag_and_drop(ele_drag, ele_drop2)
        action.drag_and_drop(ele_drag, ele_drop3)
        action.drag_and_drop(ele_drag, ele_drop4)
        action.perform()

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("TOM")
        action.send_keys(Keys.SPACE)
        action.send_keys("AND JERRY ARE GOOD")
        action.send_keys(Keys.BACK_SPACE)
        action.perform()
        sleep(5)
