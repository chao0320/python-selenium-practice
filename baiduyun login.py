# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time

broswer = webdriver.Chrome()
url="https://login.bce.baidu.com/"
broswer.get(url)
print("进入 %s" %(broswer.title),"页面")
# 将浏览器最大化
broswer.maximize_window()
time.sleep(3)

broswer.find_element_by_id("TANGRAM__PSP_4__userName").clear()
broswer.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("782898626@qq.com")
broswer.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(Keys.TAB)
time.sleep(3)
broswer.find_element_by_id("TANGRAM__PSP_4__password").send_keys("cptbtptp123")
broswer.find_element_by_id("TANGRAM__PSP_4__submit").send_keys(Keys.ENTER)
print("正在登录...")
time.sleep(3)
print("进入 %s" %(broswer.title),"页面，登录成功")
time.sleep(5)
broswer.quit()
