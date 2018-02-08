# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

broswer = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
broswer.get(file_path)

# 选择页面上所有的input,然后从中过滤出所有的CheckBox，并进行勾选
'''
inputs = broswer.find_elements_by_tag_name('input')# tag_name可以，css_
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
'''
# 对所有的CheckBox选中
checkboxes = broswer.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(3)

# 将最后的一个CheckBox取消勾选
broswer.find_elements_by_css_selector('input[type=checkbox]').pop().click()

# 打印当前页面有多少个CheckBox
print(len(broswer.find_elements_by_css_selector('input[type=checkbox]')))
time.sleep(4)
broswer.quit()