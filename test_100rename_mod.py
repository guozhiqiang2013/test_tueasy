# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from afterlogin import Login
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

class RenameDoc(unittest.TestCase):
    u"""对文档重命名测试"""
    def setUp(self):
        a = Login()
        self.driver = a.driver
        a.login_tueasy("yujiezhang", "yujiezhang")

    def tearDown(self):
        self.driver.quit()

    def testRenameDoc(self):
        driver = self.driver
        driver.find_element_by_xpath("//span[text()='文档']").click()
        WebDriverWait(driver, 20, 0.5).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='测试文档']/following-sibling::i[1]"))
        )
        docmod = driver.find_element_by_xpath("//span[text()='测试文档']")
        if(docmod.is_displayed() == False):
            '''下拉滚动条'''
            scroll = driver.find_element_by_class_name("scroll-button")
            ActionChains(driver).click_and_hold(scroll).move_by_offset(0, 1000).release(scroll).perform()
        else:
            pass
        editbutton = driver.find_element_by_xpath("//span[text()='测试文档']/following-sibling::i")
        driver.execute_script("arguments[0].click();", editbutton)
        time.sleep(5)
        '''******textbox再以名称定位会抛出异常，换成以属性定位******'''
        textbox = driver.find_element_by_xpath("//span[@contenteditable='true']")
        textbox.clear()
        textbox.send_keys(u"测试文档2")
        editbutton.click()
        time.sleep(3)
        assert u"测试文档2" in driver.page_source