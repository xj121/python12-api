#-*- coding:utf-8 _*-  
""" 
@author:mongo
@file: do_excel.py 
@version:
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import openpyxl
from common.request import Request
import json
class Case:

    def __init__(self):
        self.case_id = None
        self.url = None
        self.data = None
        self.title =None
        self.method =None
        self.expected = None
        self.actual =None
        self.result =None

class DoExcel:

    def __init__(self,file_name):
        try:
            self.workbook = openpyxl.load_workbook(filename=file_name)
        except FileNotFoundError as e :
            print('{0} not found, please check file path'.format(file_name))
            raise e

    def get_cases(self,sheet_name):
        sheet = self.workbook[sheet_name]
        max_row = sheet.max_row
        cases = []
        for r in range(2,max_row+1):
            case = Case() # 实例化一个case对象，用来存放测试数据
            case.id = sheet.cell(row=r,column=1).value # 取第r行，第1格的值
            case.url = sheet.cell(row=r, column=2).value  # 取第r行，第2格的值
            case.data = sheet.cell(row=r, column=3).value  # 取第r行，第3格的值
            case.title = sheet.cell(row=r, column=4).value  # 取第r行，第4格的值
            case.method = sheet.cell(row=r, column=5).value  # 取第r行，第5格的值
            case.expected = sheet.cell(row=r, column=6).value  # 取第r行，第6格的值
            cases.append(case)
        return cases


if __name__ == '__main__':
    do_excel = DoExcel('../datas/test_data.xlsx')
    cases = do_excel.get_cases('login')
    print(cases)
    for case in cases:
        data = eval(case.data)
        resp = Request(method=case.method,url=case.url,data=data)
        # print(resp.get_status_code())
        resp_text = json.dumps(resp.get_json(), ensure_ascii=False, indent=4)
        print(resp_text)
        #判断接口响应是否和Excel里面expected的值是否一致
        # if case.expected == resp.get_text():
        #     print('pass')
        # else:
        #     print('failed')
        # expected = '用户名或密码错误'
        # msg = eval(resp.get_text())['msg']
        # resp.get_json()
        #eval 函数不能自动的识别null转化成None
        #json 字符串和dict之间的转化，推荐大家优先使用json


