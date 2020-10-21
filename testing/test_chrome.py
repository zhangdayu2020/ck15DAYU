import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_chrome:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait( 5 )

    def teardown(self):
        self.driver.quit()

    def test_01(self):
        self.driver.get( "https://ceshiren.com/" )
        self.driver.find_element( By.XPATH, "//*[@id='navigation-bar']//a" ).click()

        # def wait(x):
        #     return len(self.driver.find_elements("//*[@id='navigation-bar']//a")) > 1
        # WebDriverWait(self.driver, 10).until(wait)

        WebDriverWait( self.driver, 10 ).until(
            expected_conditions.element_to_be_clickable( By.XPATH, "//*[@id='navigation-bar']//a" ) )
