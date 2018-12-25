# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 测试上下文
"""
import re


class DoRegex:

    @staticmethod
    def replace(target): # 查找并且替换
        pattern = '\$\{(.*?)\}'
        while re.search(pattern, target):  # 找到一个就返回match
            m = re.search(pattern, target)
            key = m.group(1)  # 取第一个分组里面的字符，也就是我们需要的key
            from common.basic_data import Context
            user = getattr(Context, key)
            target = re.sub(pattern, user, target, count=1)
        return target


from common.config import ConfigLoader


class Context:
    config = ConfigLoader()
    normal_user = config.get('basic', 'normal_user')
    pwd = config.get('basic', 'pwd')


if __name__ == '__main__':
    normal_user = getattr(Context, 'normal_user')  # 获取变量的值
    # setattr(Context, 'admin_user','abc') # 添加属性
    # admin = getattr(Context, 'admin_user')
    # print(admin)
    if hasattr(Context, 'admin_user'):  # 判断是否有这个属性值
        delattr(Context, 'admin_user')  # 删除属性
    else:
        print('没有这个属性。不执行删除')

    context = Context(1, 2)
    print(getattr(context, 'a'))
