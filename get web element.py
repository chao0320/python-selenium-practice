import time
from selenium import webdriver
browser= webdriver.Firefox()
url='https://www.baidu.com'
print (("我们正在访问 %s") %(url))
browser.get(url)
#browser.get("https://www.baidu.com")
browser .implicitly_wait(30) # 智能等待30s
#百度输入框的定位方式
#通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")
#通过name方式定位
#browser.find_element_by_name("wd").send_keys("selenium")
#通过tag_name 方式定位
#browser.find_element_by_tag_name("input").send_keys("selenium")
#通过class_name 方式定位
#browser.find_element_by_class_name("s_ipt").send_keys("selenium")
#通过CSS方式定位
#browser.find_element_by_css_selector("#kw").send_keys("selenium")
#通过x_path 方式定位
#browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

############################################
browser.find_element_by_id("su").click()
time.sleep(10)
browser.quit()
