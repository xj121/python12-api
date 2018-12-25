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
from common.basic_data import DoRegex, Context
from common.do_excel import DoExcel
from common.request import Request

do_excel = DoExcel(contants.case_file)  # 实例化一个DoExcel对象
cases = do_excel.get_cases('recharge2')


@ddt
class TestRecharge(unittest.TestCase):

    def setUp(self):
        print('如何将登陆放到这里来做？')

    @data(*cases)
    def test_recharge(self, case):
        # 参数化处理
        data = DoRegex.replace(case.data)
        data = json.loads(data)
        if hasattr(Context, 'cookies'):  # 判断是否有cookies
            cookies = getattr(Context, 'cookies') # 获取放到上下文里面的cookies
        else:
            cookies = None
        resp = Request(method=case.method, url=case.url, data=data, cookies=cookies)  # 通过封装的Request类来完成接口的调用
        # 判断有没有cookie
        if resp.get_cookies():  # 判断返回里面是否有cookies
            setattr(Context, 'cookies', resp.get_cookies())  # 放入到上下文中
        print('status_code:', resp.get_status_code())  # 打印响应码
        resp_dict = resp.get_json()  # 获取请求响应，字典
        self.assertEqual(case.expected, int(resp_dict['code']))  # 判断返回的code 是否与期望结果一致

    def tearDown(self):
        pass
