#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 15:45
# @Author  : 叶永彬
# @File    : test_buyMonthTicket.py

import unittest
from Pages.payMonthTicket_page import PayMonthTicketPage
from Pages.payCharges_page import ChargesPage
import allure
from interface.pomp import Pomp
from Config.Config import Config
from common.baseCommon import getFunName

class TestMonthTicket(unittest.TestCase):
	"""购买月票模块"""

	@classmethod
	def setUpClass(cls):
		cls.A = ChargesPage()
		cls.M = PayMonthTicketPage()

	@classmethod
	def tearDownClass(cls):
		Pomp().refund_monthTicket(carNum=Config().common_carNum)
		pass

	@getFunName
	@allure.story("购买月票")
	def test_buy_monthTicket(self):
		result =self.M.buy_monthTicket("自动化测试停车场")
		assert result == True

	@getFunName
	@allure.story("访客授权一次")
	def test_visitor_authorization_once(self):
		self.carCode = self.A.create_carNum()
		result = self.M.visitor_authorization(self.carCode,time = "once")
		assert result == "授权一次"
		self.M.del_visitorCar()

	@getFunName
	@allure.story("访客授权永久")
	def test_visitor_authorization_forever(self):
		self.carCode = self.A.create_carNum()
		result = self.M.visitor_authorization(self.carCode,time = "forever")
		assert result == "不限次数"
		self.M.del_visitorCar()

	@getFunName
	@allure.story("点击月票详情")
	def test_monthTicket_detail(self):
		result = self.M.check_details()
		assert result == "自动化测试停车场"
		ChargesPage().back(1)

	@getFunName
	@allure.story("月票续约")
	def test_mothTicket_renew(self):
		result = self.M.renew_monthTicket()
		assert result == True