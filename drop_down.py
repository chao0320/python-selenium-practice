# coding=utf-8
from selenium import webdriver
import HtmlTestRunner
import os,time

broswer = webdriver.Chrome()
#file_path = 'file:///'+ os.path.abspath('drop_down.html')
print("文件路径是",os.path.abspath('drop_down.html'))
file_path = ('E:\Study\python study\practice\drop_down.html')
broswer.get(file_path)
time.sleep(2)

#先定位到下拉框
m = broswer.find_element_by_id("ShippingMethod")
m.click()

# 在定位到下拉框的选项
m.find_element_by_xpath("//*[@id='ShippingMethod']/option[3]").click()
time.sleep(3)
broswer.quit()