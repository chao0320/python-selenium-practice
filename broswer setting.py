# coding=utf-8
import time
from selenium import webdriver
broswer = webdriver.Firefox()
url = 'https://www.baidu.com'
broswer.get(url)
#print ("将浏览器最大化")

# broswer.maximize_window() #把浏览器最大化
#参数数字为像素点
print ("设置浏览器窗口大小为宽400高800")
broswer.set_window_size(400,800)
time.sleep(3)
# 窗口设置太小不能正常进行元素获取
#broswer.find_element_by_id("kw").send_keys("selenium")
#broswer.find_element_by_id("su").click()

time.sleep(5)
broswer.quit()
