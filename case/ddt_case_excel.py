#数据驱动 读取excel文件

# coding = utf-8


import unittest
import ddt
import code
import email
import sys
from unittest import suite
sys.path.append('F:/selenium_python_DataDriver')
from selenium import webdriver
from business.register_business import RegisterBusiness
import HTMLTestRunner
from util.excel_until import ExcelUtil
import os
import time
from log.user_log import UserLog

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class DataDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        print('所有case执行之前的前置')
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        print('所有case执行之后的后置')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info("this is chrome")
        self.register = RegisterBusiness(self.driver)     
    def tearDown(self):
        time.sleep(3)
        for method_name,error in self._outcome.errors:                        # TearDown 中捕获错误信息：for method_name,error in self._outcome.errors （self._outcome.errors返回list）
            if error:
                case_name = self._testMethodName                              # 根据当前动态的类名和方法名来获取
                self.driver.save_screenshot(os.path.join(os.getcwd(),"report",case_name+".png"))
        self.driver.close()
    
    # @ddt.data([email,'username','password',code,'assertCode','assertText'],[email,'username','password',code,'assertCode','assertText'])
    # @ddt.unpack
    @ddt.data(*data)
    def test_register_ddt_case(self,data):
        email,username,password,code,assertCode,assertText = data
        function_error = self.register.register_function(email,username,password,code,assertCode,assertText)
        # 通过if判断
        # if email_error == True:
        #     print("注册成功了，此条case失败")

        #通过assert判断是否为error
        #self.assertFalse(function_error,"输入框有错误时不报错，case执行register_function返回False")
        self.assertTrue(function_error,"输入框均正确时不报错，case执行通过，注册成功")


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(),"report","ddt_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(DataDriver)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is ddt report",description=u"这个是DDT测试报告",verbosity=2)
    runner.run(suite)


