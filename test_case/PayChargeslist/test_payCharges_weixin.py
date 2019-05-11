#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 13:46
# @Author  : 叶永彬
# @File    : test_payCharges_weixin.py

from interface.car_in_out import ApiCase
from Pages.payCharges_page import ChargesPage
import unittest
import allure
from Config.Config import Config
from common.baseCommon import getFunName

@allure.feature("微信支付案例")
class TestPayChargesWeiXin(unittest.TestCase):
	"""微信支付案例"""

	def setUp(self):
		self.P = ChargesPage()
		self.carCode = self.P.create_carNum()

	def tearDown(self):
		self.P.back(3)

	@getFunName
	@allure.story("付费离场(微信支付)")
	def test_payleave_weixin(self):
		"""
		用例描述：付费离场(微信支付)
		"""
		A = ApiCase(carNum = Config().common_carNum)
		A.car_run_inside()
		self.P.pay_charges(Config().common_carNum)
		result = self.P.submit_pay(type="微信")
		assert result == True
		A.pay_charge()
		A.car_run_outside()

	@getFunName
	@allure.story("代缴停车费")
	def test_pay_another(self):
		"""
		用例描述：代缴停车费
		"""
		A = ApiCase(carNum=self.carCode)
		A.car_run_inside()
		result = self.P.pay_with_another(self.carCode)
		assert result == True
		A.pay_charge()
		A.car_run_outside()