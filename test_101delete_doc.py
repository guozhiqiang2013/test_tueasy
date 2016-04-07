# coding=utf-8
import time
from TuEasyTestCase.afterlogin import Login
import unittest

class DeleteDoc(unittest.TestCase):
    u"""删除文档测试（取消和确定）"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def testDeleteDoc(self):
        driver = self.driver
        # 点击【文档】，进入文档页面
        driver.find_element_by_xpath("//span[text()='文档']").click()
        time.sleep(3)
        list1 = driver.find_elements_by_xpath("//span[text()='测试文档2']")
        ceshi_mod = driver.find_element_by_xpath(
            "//span[text()='测试文档2']/parent::div/preceding-sibling::div/div[@class='spanArea']")
        # 点击删除按钮
        del_button = ceshi_mod.find_element_by_xpath("./span[text()='删除']")
        driver.execute_script("arguments[0].click();", del_button)
        time.sleep(3)
        # 取消
        driver.find_element_by_xpath("html/body/div[3]/div/button[2]").click()
        list2 = driver.find_elements_by_xpath("//span[text()='测试文档2']")
        time.sleep(3)
        # 点击删除按钮，确定
        driver.execute_script("arguments[0].click();", del_button)
        driver.find_element_by_xpath("html/body/div[3]/div/button[1]").click()
        time.sleep(3)
        list3 = driver.find_elements_by_xpath("//span[text()='测试文档2']")
        print len(list1), len(list2), len(list3)
        self.assertEqual(len(list1), len(list2))
        self.assertEqual(len(list1), len(list3) + 1)