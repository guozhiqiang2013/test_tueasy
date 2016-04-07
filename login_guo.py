# coding: UTF-8
from selenium import webdriver
import  time


browser = webdriver.Firefox()
browser.get('http://123.57.27.73/')
browser.maximize_window()
time.sleep(2)
browser.find_element_by_id("userName").send_keys("admin")
browser.find_element_by_id("passWord").send_keys("admin")
time.sleep(1)
browser.find_element_by_id("btnLogin").click()