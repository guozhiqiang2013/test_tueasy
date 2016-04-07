# coding=utf-8

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login(object):

    def __init__(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()

    def login_tueasy(self, username, password):

        #self.driver.get("http://192.168.0.6/")
        self.driver.get("http://123.57.27.73/")
        self.driver.maximize_window()
        #等待用户名出来以后，是个等待的意思
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, "userName"))
        )
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_id("passWord").send_keys(password)
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(3)
        assert self.driver.find_element_by_xpath("html/body/div[1]/header/div/a[2]").text == username

    def in_editpage(self, doc_name):
        self.driver.find_element_by_xpath("//span[text()='文档']").click()
        time.sleep(3)
        test1mod = self.driver.find_element_by_xpath(
            "//span[text()='" + doc_name + "']/parent::div/preceding-sibling::div/div[@class='spanArea']")
        editbutton = test1mod.find_element_by_xpath("./span[2]")
        self.driver.execute_script("arguments[0].click();", editbutton)

'''
if __name__=="__main__":
    a = Login()
    a.login_tueasy("yujiezhang","yujiezhang")
    a.in_editpage("测试文档")
'''
