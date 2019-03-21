# -*- coding: utf-8 -*-
# @File  : test_park_data_driven.py
# @Author:
# @Date  : 2018/11/26
# @Desc  :


import pytest,os
import allure
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(BASE_DIR, "../.."))
from common.utils import YmlUtils
from Api.parkVisitorlist import parkVistorlist


args_item = "send_data,expect"
test_data,case_desc = YmlUtils("/test_data/Park/parklist.yml").getData
@pytest.mark.parametrize(args_item, test_data, ids=case_desc)
class TestWordpress():
    """验证搜索的关键字"""
    # @allure.story('验证查询')
    # def test_getlist(self,userLogin,send_data,expect):
    #     re = parkVistorlist(userLogin).getParklist(send_data["carLicenseNumber"])
    #     result =re.json()
    #     assert result["status"] == expect["status"]
    #     assert result["resultCode"] == expect["resultCode"]

    @allure.story('新增车辆')
    def test_vistorCar_save(self,userLogin,send_data,expect):
        re = parkVistorlist(userLogin).save(send_data["carLicenseNumber"],send_data["owner"],send_data["specialCarTypeConfigId"])
        result = re.json()
        assert result["status"] == expect["status"]
        result["resultCode"] == expect["resultCode"]

    @allure.story('修改车辆')
    def test_vistorCar_edit(self,userLogin,send_data,expect):
        re = parkVistorlist(userLogin).save(send_data["carLicenseNumber"], send_data["owner"],send_data["specialCarTypeConfigId"])
        result = re.json()
        assert result["status"] == expect["status"]
        result["resultCode"] == expect["resultCode"]