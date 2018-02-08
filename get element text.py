#coding=utf-8
import time
from selenium import webdriver;
browser = webdriver.Firefox()
url ='https://www.baidu.com'
browser.get(url)
time.sleep(3)
# id=cp 元素的文本信息
data = browser.find_element_by_id("cp").text
print(data) #定义的不需要加""

time.sleep(5)
browser.quit()
	

