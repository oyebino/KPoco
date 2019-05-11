#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 15:59
# @Author  : 叶永彬
# @File    : test_add_carNumType.py
from interface.car_in_out import ApiCase
from Pages.payCharges_page import ChargesPage
import unittest
import allure
from common.baseCommon import getFunName

@allure.feature("添加不同类型车牌")
class TestAddTypeCarNum(unittest.TestCase):

	def setUp(self):
		self.P = ChargesPage()

	def tearDown(self):
		self.P.del_carCode(self.carCode)
		self.A.car_run_outside()

	@getFunName
	@allure.story("添加黄牌车-进出场缴费一次")
	def test_add_yellowCarNum_and_pay(self):
		"""
		用例描述：添加黄牌车-进出场缴费一次
		"""
		self.carCode = self.P.create_carNum()
		self.A = ApiCase(carNum =self.carCode + "黄")
		self.A.car_run_inside()
		result = self.P.binding_carCode(self.carCode,carType="黄牌")
		self.P.pay_charges(self.carCode)
		self.P.submit_pay()
		assert result == True

	@getFunName
	@allure.story("添加白牌车-进出场缴费一次")
	def test_add_whiteCarNum_and_pay(self):
		"""
		用例描述：添加白牌车-进出场缴费一次
		"""
		self.carCode = self.P.create_carNum()
		self.A = ApiCase(carNum=self.carCode + "白")
		self.A.car_run_inside()
		assert self.P.binding_carCode(self.carCode, carType="白牌") == True
		self.P.pay_charges(self.carCode)
		self.P.submit_pay()

	@getFunName
	@allure.story("添加黑牌车-进出场缴费一次")
	def test_add_blackCarNum_and_pay(self):
		"""
		用例描述：添加黑牌车-进出场缴费一次
		"""
		self.carCode = self.P.create_carNum()
		self.A = ApiCase(carNum=self.carCode + "黑")
		self.A.car_run_inside()
		assert self.P.binding_carCode(self.carCode, carType="黑牌") == True
		self.P.pay_charges(self.carCode)
		self.P.submit_pay()

	@getFunName
	@allure.story("添加新能源牌车-进出场缴费一次")
	def test_add_greenCarNum_and_pay(self):
		"""
		用例描述：添加新能源牌车-进出场缴费一次
		"""
		self.carCode = self.P.create_carNum(carType="新能源")
		self.A = ApiCase(carNum=self.carCode)
		self.A.car_run_inside()
		assert self.P.binding_carCode(self.carCode, carType="新能源") == True
		self.P.pay_charges(self.carCode)
		self.P.submit_pay()

	@getFunName
	@allure.story("添加民航车-进出场缴费一次")
	def test_add_flightCarNum_and_pay(self):
		"""
		用例描述：添加民航车-进出场缴费一次
		"""
		self.carCode = self.P.create_carNum(carType="民航")
		self.A = ApiCase(carNum=self.carCode)
		self.A.car_run_inside()
		assert self.P.binding_carCode(self.carCode, carType="民航") == True
		self.P.pay_charges(self.carCode)
		self.P.submit_pay()

