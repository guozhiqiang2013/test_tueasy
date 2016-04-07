# coding=utf-8
from afterlogin import Login
import unittest
import time

class CreateDoc(unittest.TestCase):
    u"""创建文档测试"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")

    def tearDown(self):
        self.driver.quit()


    def testCreateDoc(self):
        # 点击空白模板新建文档
        driver = self.driver
        blank_mod = driver.find_element_by_xpath(
            "//span[text()='空白模板']/parent::div/preceding-sibling::div/div[@class='spanArea']")
        # ActionChains(driver).move_to_element(blank_mod).perform()

        createbutton = blank_mod.find_element_by_xpath("./span[text()='创建文档']")
        driver.execute_script("arguments[0].click();", createbutton)
        # 输入文档名称，点击确定
        driver.find_element_by_xpath("//input[@placeholder='新建文档名字']").send_keys(u"测试文档")
        driver.find_element_by_xpath("//span[text()='确定']").click()
        time.sleep(3)
        # assert u"测试文档" in driver.current_url
        a =  driver.find_element_by_xpath("//span[text()='保存']")
        driver.execute_script("arguments[0].click();",a)
        time.sleep(10)
        # 回到文档页面，检查新建文档是否存在
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(5)
        driver.find_element_by_xpath("//span[text()='文档']").click()
        time.sleep(5)
        # spanlist = driver.find_elements_by_class_name("title")
        # spanlist2 = []
        # for span in spanlist:
        #     spanlist2.append(span.text)
        # print spanlist2
        assert u"测试文档" in driver.page_source

if __name__ == "__main__":
    a = CreateDoc()
    a.testCreateDoc()