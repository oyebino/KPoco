# -*- coding: utf-8 -*- 
# @File : config.py
# @Author: 叶永彬
# @Date : 2018/9/13 
# @Desc : 读取config.ini 配置文件

from configparser import ConfigParser
import os
from sys import argv

class Config(object):

    VALUE_ENT_AOMP_HOST = "aomp_host"
    VALUE_ENT_POMP_HOST = "pomp_host"
    VALUE_ENT_WEIXIN_HOST = "weixin_host"
    VALUE_ENT_VEMS_HOST = "vems_host"
    VALUE_ENT_DB = "db"
    VALUE_ENT_DB_PORT = "db_port"
    VALUE_ENT_DB_NAME = "db_name"
    VALUE_ENT_DB_USER = "db_user"
    VALUE_ENT_DB_PASSWORD = "db_password"
    VALUE_ENT_COMMON_CARNUM = "common_carNum"

    def __init__(self,env="SIT"):

        self.CATEGORY = env
        self.config = ConfigParser()

        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path,encoding='UTF-8')
        self.aomp_host = self.config.get(self.CATEGORY,self.VALUE_ENT_AOMP_HOST)
        self.pomp_host = self.config.get(self.CATEGORY,self.VALUE_ENT_POMP_HOST)
        self.weixin_host = self.config.get(self.CATEGORY,self.VALUE_ENT_WEIXIN_HOST)
        self.vems_host = self.config.get(self.CATEGORY, self.VALUE_ENT_VEMS_HOST)
        self.db = self.config.get(self.CATEGORY,self.VALUE_ENT_DB)
        self.db_port = self.config.get(self.CATEGORY,self.VALUE_ENT_DB_PORT)
        self.db_name = self.config.get(self.CATEGORY,self.VALUE_ENT_DB_NAME)
        self.db_user = self.config.get(self.CATEGORY,self.VALUE_ENT_DB_USER)
        self.db_password = self.config.get(self.CATEGORY, self.VALUE_ENT_DB_PASSWORD)
        self.common_carNum = self.config.get(self.CATEGORY, self.VALUE_ENT_COMMON_CARNUM)

    def get(self,title,value):
        return self.config.get(title, value)


if __name__=='__main__':
    C = Config()
    print(C.common_carNum)
