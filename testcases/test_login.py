# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import json
import unittest

from ddt import ddt, data

from common import contants
from common.do_excel import DoExcel
from common.request import Request




@ddt
class TestLogin(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 实例化一个DoExcel对象
    cases = do_excel.get_cases('login')

    def setUp(self):
        print('测试准备')

    @data(*cases)
    def test_login(self, case):
        data = json.loads(case.data)
        resp = Request(method=case.method, url=case.url, data=data)  # 通过封装的Request类来完成接口的调用
        print('status_code:', resp.get_status_code())  # 打印响应码
        resp_dict = resp.get_json()  # 获取请求响应，字典
        self.assertEqual(case.expected, resp.get_text())

    def tearDown(self):
        print('测试清除')

