# coding=utf-8
from afterlogin import Login
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

class LookDoc(unittest.TestCase):
    u"""查看文档测试"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")

    def tearDown(self):
        self.driver.quit()

    def testLookDoc(self):
        driver = self.driver
        driver.find_element_by_xpath("//span[text()='文档']").click()
        time.sleep(3)
        current_mod = driver.find_element_by_xpath(
            "//span[text()='测试文档']/parent::div/preceding-sibling::div/div[@class='spanArea']")
        ActionChains(driver).move_to_element(current_mod).perform()
        # 点击查看按钮
        e = current_mod.find_element_by_xpath("./span[1]")
        driver.execute_script("arguments[0].click();", e)
        assert "page" in driver.current_url

