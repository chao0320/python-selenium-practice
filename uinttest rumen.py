# coding=utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        time.sleep(1)
        print("end")
    def test01(self):
        print("执行测试用例1")
    def test03(self):
        print("执行测试用例3")
    def test02(self):
        print("执行测试用例2")
    def addtest(self):
        print("添加add方法")
if __name__=="__main__":
    unittest.main()
