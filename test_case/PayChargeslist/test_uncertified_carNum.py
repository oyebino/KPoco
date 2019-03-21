#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 9:44
# @Author  : 叶永彬
# @File    : test_uncertified_carNum.py

from interface.pomp import Pomp
from interface.car_in_out import ApiCase
from Pages.uncertifiedCarnum_page import UncertifiedCarPage
from Pages.payCharges_page import ChargesPage
import unittest
import allure
from common.baseCommon import getFunName

class TestUncertifiedCarNum(unittest.TestCase):
	"""未认证车辆"""
	@classmethod
	def setUpClass(cls):
		cls.carNum = ChargesPage().create_carNum()
		cls.U = UncertifiedCarPage(cls.carNum)
		ChargesPage().binding_carCode(cls.carNum)
		cls.A = ApiCase(carNum =cls.carNum)
		cls.A.car_run_inside()
		Pomp().open_monthTicket(cls.carNum)

	@classmethod
	def tearDownClass(cls):
		ChargesPage().del_carCode(cls.carNum)
		cls.A.car_run_outside()
		Pomp().refund_monthTicket(carNum = cls.carNum)

	@getFunName
	@allure.story("认证车牌--车牌下方有验证提醒")
	def test_Uncertified_carNum_warn(self):
		result = self.U.find_uncertified_warm()
		assert "车辆未认证" in result

	@getFunName
	@allure.story("认证车牌--点击进场图片会弹出要提示认证的提醒")
	def test_Uncertified_carPicture_warn(self):
		result = self.U.find_uncertified_carPicture_warn()
		assert "查看进场图片需要行驶证认证" == result

	@getFunName
	@allure.story("未认证车牌--点击上锁会弹出要认证提醒")
	def test_Uncertified_lock_warn(self):
		result = self.U.find_uncertified_lock_warn()
		assert "锁车需要行驶证认证" == result

	@getFunName
	@allure.story("未认证车牌--进场的车辆停车场会显示为***停车场")
	def test_Uncertified_parkingName(self):
		result = self.U.find_uncertified_parkingName()
		assert "***停车场" == result

	@getFunName
	@allure.story("未认证车牌--点击月票详情会弹出要认证提醒")
	def test_Uncertified_amonthTicketDetail_authorize_warn(self):
		result = self.U.Uncertified_monthTicketDetail_authorize_warn(self.carNum)
		assert "访客授权需行驶证认证" == result
