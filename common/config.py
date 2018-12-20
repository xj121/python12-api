# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 配置文件的读取
"""
import configparser
import os

from common import contants


# 创建实例
# 加载配置文件
# 根据section，option 来取到配置的值
class ConfigLoader:

    def __init__(self):
        # 创建实例
        self.conf = configparser.ConfigParser()
        # 加载配置文件
        file_name = os.path.join(contants.configs_dir, 'global.conf')
        self.conf.read(filenames=file_name,encoding='utf-8')
        if self.getboolean('switch','on'):
            online = os.path.join(contants.configs_dir, 'online.conf')
            self.conf.read(filenames=online,encoding='utf-8')
        else:
            test = os.path.join(contants.configs_dir, 'test.conf')
            self.conf.read(filenames=test,encoding='utf-8')

    def get(self, section, option): # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.get(section, option)

    def get(self, section, option): # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.get(section, option)

    def getboolean(self, section, option): # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getboolean(section, option)

    def getint(self, section, option): # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getint(section, option)

    def getfloat(self, section, option): # 返回float类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getfloat(section, option)


if __name__ == '__main__':
    config = ConfigLoader()
    url_pre = config.get('api', 'url_pre')
    print(type(url_pre),url_pre)

    # # 创建实例
    #     # conf = configparser.ConfigParser()
    #     # # 加载配置文件
    #     # file_name = os.path.join(contants.configs_dir, 'global.conf')
    #     # conf.read(file_name)
    #     # on = conf.getboolean('switch','on')
    #     # print(type(on), on)