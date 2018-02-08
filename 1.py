# coding= utf-8
import requests
# 请求百度
r = requests.get("https://www.baidu.com")
print(r.status_code)
print(r.text)
print(r.content.encode('utf-8'))