# coding=utf-8
import time
import unittest
from afterlogin import Login

class XiaZai(unittest.TestCase):
    u"""下载功能测试"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")
        a.in_editpage("测试文档")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def testXiaZai(self):
        driver = self.driver
        # 定位“下载”按钮
        xiazai_button = driver.find_element_by_xpath("//span[text()='下载']")
        xiazai_button.click()
        time.sleep(3)
        # 验证是否弹框
        self.assertTrue(driver.find_element_by_xpath("//span[text()=' 下载图片']").is_displayed())
