# coding = utf-8
''''''
import requests
import urllib3
urllib3.disable_warnings()
url="https://passport.cnblogs.com/user/signin"
url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
headers= {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
#只需要填写支持设备，下面的填写了，要打开fiddler
#"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#"Accept-Encoding": "gzip, deflate, br",
#"Referer": "https://i.cnblogs.com/EditPosts.aspx?opt=1",
#"Content-Type": "application/x-www-form-urlencoded",
#"Content-Length": "9348",
#"Cookie": "ga=GA1.2.943231981.1516789117; _gid=GA1.2.100676290.1517449349; .CNBlogsCookie=5664F0BDD269AF1712A8D79087D8F5F5FC493688AA34BB55720C3A77051F6EA1131C04B450EA1F04A0DDBEB58E103D2F5ED3FEEAD5A78EB09A8EEB791FC53A9923A68BAB6D63F9C7D2BC69EC7168606695D14832F088354F9AF95A886AD13C10D1CE28B8; .Cnblogs.AspNetCore.Cookies=CfDJ8N7AeFYNSk1Put6Iydpme2YSwCHpppLtD4kvOOxHQ_tQvpUbZ_B7PomsnhbBil5rZRHB8YJMByIRx31AiCdJyw0zZuB1gFIspw5rtiZEMM77Z8pWTvnXg-Qny4Drf1-symFMzGUQbfHXXrs2OAhJQ-7REJqka0LxUyqh9igcck2JlcLug01aNPY-dPSA0bYoVHANaW1Eebs2xhrdzzwcF4IJCxgOEdPXSKd-8sln4n3ngpWRTpyFGmmSk7oW2UpRe3i044F-ZWEUi-YqcJHFcQfs9UAVNIW_bSmqSYhKW2B1MAvyZvi5DpOWiTBOMwxxvQ; SERVERID=5600344ccf6bd2d4bb4775a2baf862da|1517455949|1517455442",
#"Connection": "keep-alive",
#"Upgrade-Insecure-Requests":"1"
}
s = requests.session()
r = s.get(url,headers=headers,verify=False)
print(s.cookies)

# 添加登录需要的两个cooike
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie','5664F0BDD269AF1712A8D79087D8F5F5FC493688AA34BB55720C3A77051F6EA1131C04B450EA1F04A0DDBEB58E103D2F5ED3FEEAD5A78EB09A8EEB791FC53A9923A68BAB6D63F9C7D2BC69EC7168606695D14832F088354F9AF95A886AD13C10D1CE28B8')
c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8N7AeFYNSk1Put6Iydpme2YSwCHpppLtD4kvOOxHQ_tQvpUbZ_B7PomsnhbBil5rZRHB8YJMByIRx31AiCdJyw0zZuB1gFIspw5rtiZEMM77Z8pWTvnXg-Qny4Drf1-symFMzGUQbfHXXrs2OAhJQ-7REJqka0LxUyqh9igcck2JlcLug01aNPY-dPSA0bYoVHANaW1Eebs2xhrdzzwcF4IJCxgOEdPXSKd-8sln4n3ngpWRTpyFGmmSk7oW2UpRe3i044F-ZWEUi-YqcJHFcQfs9UAVNIW_bSmqSYhKW2B1MAvyZvi5DpOWiTBOMwxxvQ')
c.set('AlwaysCreateItemsAsActive',"True")
c.set('AdminCookieAlwaysExoandAdvanced',"True")
s.cookies.update(c)
print(s.cookies)
# 登录成功后保存编辑内容
r1 = s.get(url2, headers=headers, verify=False)
# 保存草稿箱
body = {"__VIEWSTATE": "",
        "Editor$Edit$Advanced$chkComments":	"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":	"on",
        "Editor$Edit$Advanced$chkMainSyndication":	"on",
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$EditorBody": "<p>仅仅是</p>",
        "Editor$Edit$lkbDraft": "存为草稿",
        "Editor$Edit$txbTitle": "session关联接口5"}

r2 = s.post(url2, data=body,verify=False)
print("登录成功后的页面",r1.content.decode('utf-8'))
print("保存草稿成功后的界面",r2.content.decode('utf-8'))
