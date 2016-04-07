# coding=utf-8
import time
import unittest
from afterlogin import Login

class Yanshi(unittest.TestCase):
    u"""演示功能测试"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")
        a.in_editpage("测试文档")
        time.sleep(3)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()

    def testYanShi(self):
        driver = self.driver
        driver.find_element_by_xpath("//dt[text()=' 图表 ']").click()
        driver.find_element_by_xpath("//img[@title='基础柱状图']").click()
        time.sleep(3)
        yanshi_button = driver.find_element_by_xpath("//span[text()='演示']")
        frame = driver.find_element_by_xpath("//canvas[@data-zr-dom-id='_zrender_hover_']")
        print frame
        location1 = frame.location
        #yanshi_button.click()
        driver.execute_script("arguments[0].click();",yanshi_button)
        time.sleep(3)
        location2 = frame.location
        self.assertNotEqual(location1, location2)