# -*- coding: utf-8 -*-
# @File  : conftest.py
# @Author: 叶永彬
# @Date  : 2018/11/22
# @Desc  :

from common.Req import Req
from Api.Login import Login
import pytest
import unittest

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import inspect

# @pytest.fixture(scope="class")
# def userLogin():
#     L = Login()
#     Session = L.login()
#     return Req(Session)

@pytest.fixture(scope="class")
def login_homePage():
    """"登录主界面"""
    PKG = "com.tencent.mm"  # 微信包名
    stop_app(PKG)
    wake()
    start_app(PKG)
    poco(text="YDTtest").wait_for_appearance()
    poco(text="YDTtest").click()
    poco(text="交停车费").click()
    sleep(5)


@pytest.fixture()
def create_caseLog():
	fileName = get_current_function_name()
	print(fileName)

def get_current_function_name():
    return inspect.stack()[1][3]



"""

@pytest.fixture(scope="class")
def Login():

    S = requests.Session()

    headers ={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    seccode = "http://47.106.221.58:5002/mgr/normal/authz/seccode.do"

    re = S.get(seccode)

    verify_seccode = "http://47.106.221.58:5002/mgr/normal/authz/verify_seccode.do"

    data = {"seccode": 9999}

    re = S.post(verify_seccode,data=data)

    print(re.text)


    url = "http://47.106.221.58:5002/mgr/normal/ajax/login.do"

    data = {
    "username": "autotest",
    "password": "123456",
    "seccode": 9999}

    re = S.post(url,data,headers=headers)

    return Req(S)

"""


if __name__ == "__main__":
	login_homePage()