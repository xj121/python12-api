#-*- coding:utf-8 _*-  
""" 
@author:mongo
@file: request.py 
@version:
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import requests

class Request:

    def __init__(self,method,url,data=None,cookies=None,headers=None):
        try:
            if method == 'get':
                self.resp = requests.get(url=url, params=data, cookies=cookies, headers=headers)
            elif method == 'post':
                self.resp = requests.post(url=url, data=data, cookies=cookies, headers=headers)
            elif method == 'delete':
                self.resp = requests.delete(url=url, data=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e


    def get_status_code(self):
        return self.resp.status_code

    def get_text(self):
        return self.resp.text

    def get_json(self):
        return self.resp.json()
