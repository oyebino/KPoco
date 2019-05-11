#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:31
# @Author  : 叶永彬
# @File    : test_charges.py

from interface.car_in_out import ApiCase
from Pages.payCharges_page import ChargesPage
import unittest
import allure
from common.baseCommon import getFunName
from Config.Config import Config

@allure.feature("交费模块")
class TestPayChargeslist(unittest.TestCase):

	@getFunName
	@allure.story("添加-删除-车牌号")
	def test_add_and_del_carNum(self):
		"""
		用例描述：添加-删除-车牌号
		"""
		P = ChargesPage()
		carCode = P.create_carNum()
		assert P.binding_carCode(carCode) == True
		assert P.del_carCode(carCode) == True

	@getFunName
	@allure.story("设置常用车牌")
	def test_setting_often_carNum(self):
		"""
		用例描述：设置常用车牌
		"""
		P = ChargesPage()
		carCode = P.create_carNum()
		P.binding_carCode(carCode)
		P.set_often_carNum(carCode)
		result = P.set_often_carNum(Config().common_carNum)
		P.del_carCode(carCode)
		assert result == True

	@getFunName
	@allure.story("车辆锁定-解锁")
	def test_lock_and_unlock(self):
		"""
		用例描述：车辆锁定-解锁
		"""
		A = ApiCase(carNum =Config().common_carNum)
		A.car_run_inside()
		P = ChargesPage()
		result = P.lock_car(Config().common_carNum)
		assert result == True
		P.unlock_car(Config().common_carNum)
		A.pay_charge()
		A.car_run_outside()
		P.web_refresh()

	@getFunName
	@allure.story("付费离场(余额支付)")
	def test_payleave_account(self):
		"""
		用例描述：付费离场(余额支付)
		"""
		A = ApiCase(carNum =Config().common_carNum)
		A.car_run_inside()
		P = ChargesPage()
		P.pay_charges(Config().common_carNum)
		result = P.submit_pay()
		assert result== True
		A.car_run_outside()
