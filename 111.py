import socket
import time
timeout = 20
socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
sleep_download_time = 10
time.sleep(sleep_download_time) #这里时间自己设定
request = urllib.request.urlopen(https://www.baidu.com)#这里是要读取内容的url
content = request.read()#读取，一般会在这里报异常
request.close()