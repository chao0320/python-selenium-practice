#coding=utf-8

'''
frame.html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>frame</title>
<script type="text/javascript"
async=""src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js
"></script>
<link
href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstra
p-combined.min.css" rel="stylesheet" />
<script type="text/javascript">$(document).ready(function(){
});
</script>
</head>
<body>
<div class="row-fluid">
<div class="span10 well">
<h3>frame</h3>
<iframe id="f1" src="inner.html" width="800",
height="600"></iframe>
</div>
</div>
</body>
<script
src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.
min.js"></script>
</html>
inner.html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>inner</title>
</head>
<body>
<div class="row-fluid">
<div class="span6 well">
<h3>inner</h3>
<iframe id="f2" src="http://www.baidu.com"
width="700"height="500"></iframe>
<a href="javascript:alert('watir-webdriver better than
selenium webdriver;')">click</a>
</div>
</div>
</body>
</html>
'''
from selenium import  webdriver
import os,time

broswer = webdriver.Chrome()
file_path = 'file:///'+ os.path.abspath('frame.html')
broswer.get(file_path)

broswer.implicitly_wait(30)
# 先找到iframe1 (id=f1)
broswer.switch_to_frame("f1")
#再找到下面的f2 (id=f2)
broswer.switch_to_frame("f2")

#下面可以正常操作元素了
broswer.find_element_by_id("kw").send_keys("selenium")
broswer.find_element_by_id("su").click()

time.sleep(3)
broswer.quit()