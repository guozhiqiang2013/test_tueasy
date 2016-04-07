# coding=utf-8
import unittest
import time
from afterlogin import Login

class EditGraphButton(unittest.TestCase):
    u"""验证图表上三个按钮功能"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")
        a.in_editpage("测试文档")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()

    def testEditGraphButton(self):
        driver = self.driver
        driver.find_element_by_xpath("//dt[text()=' 图表 ']").click()
        driver.find_element_by_xpath("//img[@title='基础柱状图']").click()
        # 收起按钮
        minbutton = driver.find_element_by_xpath("//div[@name='基础柱状图']/div/div[1]/div")
        # 图表区域
        showframe = driver.find_element_by_xpath("//div[@name='基础柱状图']/div/div[3]/div/div/canvas[3]")
        # 编辑按钮
        editbutton = driver.find_element_by_xpath("//div[@name='基础柱状图']/div/div[1]/img[2]")
        # 删除按钮
        delbutton = driver.find_element_by_xpath("//div[@name='基础柱状图']/div/div[1]/img[1]")
        # 验证收起按钮功能
        minbutton.click()
        self.assertEqual(showframe.size, {'width': 0, 'height': 0})
        minbutton.click()
        self.assertNotEqual(showframe.size, {'width': 0, 'height': 0})
        # 验证编辑按钮功能
        editbutton.click()
        loaddatalable = driver.find_element_by_xpath("//h4[text()='载入数据']")
        lable2 = driver.find_element_by_xpath("//h5[text()='边框']")
        self.assertTrue(loaddatalable.is_displayed())
        self.assertTrue(lable2.is_displayed())
        # 验证删除按钮功能
        delbutton.click()
        time.sleep(3)
        quedingbutton = driver.find_element_by_xpath("html/body/div[3]/div/button[1]")
        driver.execute_script("arguments[0].click();", quedingbutton)
        time.sleep(3)
        flag = False
        if(delbutton):
            flag = True
            return flag
        else:
            return flag
        self.assertFalse(flag)
