# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
import time

#broswer = webdriver.Ie()
#broswer = webdriver.Firefox()
broswer = webdriver.Chrome()

url= "https://www.baidu.com"
broswer.get(url)

#  Chrome 全屏可以，不全屏也可以，Firefox全屏不全屏都不可以，提示could not be scrolled into view，IE默认全屏
#broswer.maximize_window()

#time.sleep(3)


#broswer.find_element_by_link_text("登录").click() # Chrome可以实现，Firefox提示could not be scrolled into view，IE 提示unable to find element with link text == 登录
broswer.find_element_by_xpath("//*[@id='u1']/a[7]").click() # Chrome可以实现
time.sleep(4)

broswer.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
time.sleep(3)

broswer.find_element_by_name("userName").clear()
broswer.find_element_by_name("userName").send_keys("782898626@qq.com")
broswer.find_element_by_name("userName").send_keys(Keys.TAB)

broswer.find_element_by_name("password").send_keys("cptbtptp123")
broswer.find_element_by_id("TANGRAM__PSP_10__submit").send_keys(Keys.ENTER)

time.sleep(4)
broswer.quit()