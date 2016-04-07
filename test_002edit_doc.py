# coding=utf-8
from afterlogin import Login
import unittest, time

class EditButton(unittest.TestCase):
    u"""编辑功能测试"""
    def setUp(self):
        pass

    def tearDown(self):
        self.driver.quit()

    def testEditbutton(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")
        a.in_editpage("测试文档")
        time.sleep(3)
        assert "name" in self.driver.current_url