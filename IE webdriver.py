# coding = utf-8
from selenium import webdriver
driver =webdriver.Ie()
driver.get('https://www.baidu.com')
print (driver.title)
driver.quit()