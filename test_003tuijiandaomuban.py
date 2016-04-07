# coding:utf-8
from afterlogin import Login
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time

class TuiJian(unittest.TestCase):
    u"""推荐到模板功能测试"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")

    def tearDown(self):
        self.driver.quit()

    def testTuiJian(self):
        driver = self.driver
        listbefore = driver.find_elements_by_class_name("title")
        # 点击【文档】，进入文档页面
        driver.find_element_by_xpath("//span[text()='文档']").click()
        time.sleep(3)
        # 鼠标悬停到测试文档
        test1mod = driver.find_element_by_xpath(
            '//span[text()=\'测试文档\']/parent::div/preceding-sibling::div/div[@class=\'spanArea\']')
        # 点击“推荐到模板”按钮
        tuijian = test1mod.find_element_by_xpath("./span[4]")
        driver.execute_script("arguments[0].click()", tuijian)
        time.sleep(3)

        # 点击【模板】
        driver.find_element_by_xpath("html/body/div[1]/div/div/div/div[1]/a[1]/i").click()
        time.sleep(3)
        list1 = driver.find_elements_by_class_name("title")
        self.assertEqual(len(listbefore), len(list1)-1)
        # list2 = []
        # for i in list1:
        #     list2.append(i.text)
        #     # print i.text
        # # print list2
        # # for x in range(0, len(list2)):
        # #     print list2[x]
        # assert u'测试文档' in list2