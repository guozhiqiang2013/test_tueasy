# coding=utf-8

from selenium import webdriver
from PIL import Image
from PIL import ImageChops
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# 登陆
driver = webdriver.Chrome()
driver.get("http://192.168.0.6/")
driver.maximize_window()
WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.ID, "userName"))
)
driver.find_element_by_id("userName").send_keys("yujiezhang")
driver.find_element_by_id("passWord").send_keys("yujiezhang")
driver.find_element_by_id("btnLogin").click()
time.sleep(5)

# 插入图表
driver.find_element_by_xpath("//span[text()='文档']").click()
time.sleep(3)
test1mod = driver.find_element_by_xpath("//span[text()='测试文档']/parent::div/preceding-sibling::div/div[@class='spanArea']")
editbutton = test1mod.find_element_by_xpath("./span[2]")
driver.execute_script("arguments[0].click();", editbutton)
driver.find_element_by_xpath("//dt[text()=' 图表 ']").click()
driver.find_element_by_xpath("//img[@title='基础柱状图']").click()
time.sleep(3)
# 演示
yanshi_button = driver.find_element_by_xpath("//span[text()='演示']")
yanshi_button.click()
time.sleep(2)
# 截屏
driver.save_screenshot("D:\\before.jpg")
# 计算canvas大小和位置
frame = driver.find_element_by_xpath("//canvas[@data-zr-dom-id='_zrender_hover_']")
size= frame.size
location = frame.location
print size, location
rangle = (int(location['x']), int(location['y']),
          int(location['x'] + size['width']), int(location['y'] + size['height']))

# 截取canvas部分图像
beforeimg = Image.open("D:\\before.jpg")
canvas = beforeimg.crop(rangle)
canvas.save("D:\\canvas.jpg")

'''
对比两幅图,如果两幅图相同，diff==None，不同则为（v,v,v,v）
'''
canvasimg = Image.open("D:\\canvas.jpg")
diff = ImageChops.difference(beforeimg, canvasimg).getbbox()
print diff