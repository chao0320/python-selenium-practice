'''
鼠标事件
ActionChains 类
context_click() 游击
double_click() 双击
drag_and_drop() 拖动 ##
'''
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

broswer = webdriver.Firefox()
url="https://login.bce.baidu.com/"
broswer.get(url)

broswer.maximize_window()
time.sleep(3)

#定位需要右击的元素
qqq = broswer.find_element_by_xpath("//*[@id='brand']/a/img")
#对定位到的元素进行操作
ActionChains(broswer).context_click(qqq).perform()
#print(qqq.get_attribute())
time.sleep(5)
broswer.quit()