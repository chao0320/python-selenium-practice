# coding=utf-8
import requests
import re
# 禁用安全请求警告
import urllib3
urllib3.disable_warnings()
# 先打开登录首页，获取部分cooki
url = "https://jenkins.qa.netpulse.support/j_acegi_security_check"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://jenkins.qa.netpulse.support/login?from=%2F",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "231",
            "Cookie": "JSESSIONID.f25ff9ab=r625lmed9kldju32mrszueed",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
}
d = {"j_username": "zhangchao",

"j_password": "TKeuqVez",
"remember_me": "on",
"from": "/",
"json":	{"j_username": "zhangchao",
         "j_password": "TKeuqVez",
         "remember_me": "true",
         "from": "/"},
"Submit":	"登录"
}
s = requests.session()
r = s.post(url,headers=headers, data=d, verify=False)
print(r.content.decode('utf-8'))# 对响应界面进行解码

#对页面进行

print(r.status_code)
t = re.findall(r'<b>(.+?)</b>',r.content.decode('utf-8'))# 对响应界面进行解码
print(t[0])
print(t[1])