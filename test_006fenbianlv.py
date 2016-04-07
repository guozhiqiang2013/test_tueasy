# coding=utf-8

import unittest
import time
from selenium.webdriver import ActionChains
from afterlogin import Login

class FenBianLv(unittest.TestCase):
    u"""调整分辨率功能测试"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")
        a.in_editpage("测试文档")

    def tearDown(self):
        self.driver.quit()

    def testFenBianLv(self):

        driver = self.driver
        # 点击【文档】，进入文档页面
        # driver.find_element_by_xpath("html/body/div[1]/div/div/div/div[1]/a[2]/i").click()
        # time.sleep(3)
        # # 鼠标悬停到测试文档
        # test1mod = driver.find_element_by_xpath(
        #     "//span[text()='测试文档']/parent::div/preceding-sibling::div/div[@class='spanArea']")
        # ActionChains(driver).move_to_element(test1mod).perform()
        #
        # # 定位“编辑”按钮
        # editbutton = test1mod.find_element_by_xpath("./span[2]")
        # editbutton.click()
        time.sleep(3)
        # 查看每次点击是否调整画布分辨率准确
        fbl_button = driver.find_element_by_class_name("size")
        blank_frame = driver.find_element_by_xpath("//section")
        size1 = blank_frame.size
        self.assertEqual(size1, {'width': 1920, 'height': 1080})
        fbl_button.click()
        size2 = blank_frame.size
        self.assertEqual(size2, {'width': 1440, 'height': 900})
        fbl_button.click()
        size3 = blank_frame.size
        self.assertEqual(size3, {'width': 1360, 'height': 768})
        fbl_button.click()
        size4 = blank_frame.size
        self.assertEqual(size4, {'width': 1024, 'height': 768})
        fbl_button.click()
        size5 = blank_frame.size
        self.assertEqual(size5, {'width': 800, 'height': 600})
        self.assertEqual(fbl_button.text, "800:600")