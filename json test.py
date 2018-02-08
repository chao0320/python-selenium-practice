# coding=utf-8
import requests
import json
import HTMLTestRunner
'''
payload = {"yoyo":True,
           "json":False,
           "python":"226296743"
          }
print(payload)
print(type(payload))
#转化为json格式
data_json = json.dumps(payload)
print(type(data_json))
print (data_json)
'''
url = "http://www.kuaidi100.com/query?type=zhongtong&postid=539484472117&temp=0.1939689408047508 "
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
           }
s = requests.session()
r = s.get(url, headers=headers,verify=False)
print("1",r.content.decode('utf-8'))
result = r.json()
print("2",result)
data = result["data"] # 获取data里的内容
# 如果换成下面这种会读不出来,data部分是json格式的，上面的不是
'''
data = r['data']
'''
print ("3",data)
print("4",data[0])
get_result = data[0]['context'] #获取1签收状态
print ("5",get_result)
if "已签收" in get_result:
    print("快递单已签收成功")
else:
    print("未签收")