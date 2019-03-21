#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 19:41
# @Author  : 叶永彬
# @File    : test_chargesCoupon.py

import unittest
from interface.car_in_out import ApiCase
from Pages.payCharges_page import ChargesPage
from Pages.payCoupon_page import PayCouponPage
from interface.pomp import Pomp
from interface.pomp import werXin
from interface.aomp import commonConpon
import allure
from common.baseCommon import getFunName

class TestChargesCoupon(unittest.TestCase):
	"""费用优惠模块"""
	@classmethod
	def setUpClass(cls):
		cls.A = ChargesPage()
		cls.P = PayCouponPage()
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		self.carNum =self.A.create_carNum()
		self.C = ApiCase(carNum =self.carNum)
		self.C.car_run_inside()
		self.A.binding_carCode(self.carNum)

	def tearDown(self):
		self.C.car_run_outside()
		self.A.del_carCode(self.carNum)

	@getFunName
	@allure.story("商家券优惠-需余额缴费")
	def test_businessCoupon_payCharge(self):
		werXin().send_Business_coupon("UI一点停专用金额扣减0.01",self.carNum)
		self.A.pay_charges(self.carNum)
		result =self.P.use_businessCoupon("UI一点停专用金额扣减0.01")
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("商家金额优惠-不用缴费")
	def test_businessCoupon_noPaycharge(self):
		werXin().send_Business_coupon("UI一点停专用金额扣减25", self.carNum)
		self.A.pay_charges(self.carNum)
		result = self.P.use_businessCoupon("UI一点停专用金额扣减25")
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("商家券折扣6折-需余额缴费")
	def test_business_discount(self):
		werXin().send_Business_coupon("UI一点停专用折扣6折", self.carNum)
		self.A.pay_charges(self.carNum)
		result = self.P.use_businessCoupon("UI一点停专用折扣6折")
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("商家免费劵")
	def test_business_free(self):
		werXin().send_Business_coupon("UI一点停专用免费劵", self.carNum)
		self.A.pay_charges(self.carNum)
		result = self.P.use_businessCoupon("UI一点停专用免费劵")
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("商家固定券")
	def test_business_fixed(self):
		werXin().send_Business_coupon("UI一点停专用固定劵0.22元", self.carNum)
		self.A.pay_charges(self.carNum)
		result = self.P.use_businessCoupon("UI一点停专用固定劵0.22元")
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("商家时间劵-操作全部时间")
	def test_business_time(self):
		werXin().send_Business_coupon("UI一点停专用抵扣时间券", self.carNum)
		self.A.pay_charges(self.carNum)
		result = self.P.use_businessCoupon("UI一点停专用抵扣时间券")
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("通用劵-需要缴费")
	def test_commonConpon_payCharge(self):
		commonConpon().send_coupon("UI一点停通用劵")
		self.A.pay_charges(self.carNum)
		result = self.P.use_commonConpon("通用劵0.01元")
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("通用劵-不用缴费")
	def test_commonConpon_noPayCharge(self):
		commonConpon().send_coupon("UI一点停通用劵25元")
		self.A.pay_charges(self.carNum)
		result = self.P.use_commonConpon("通用劵25元")
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("线上优惠-需要缴费")
	def test_parkCoupon_payCharge(self):
		Pomp().park_coupon_manager("线上优惠0.01元","VALID")
		self.A.pay_charges(self.carNum)
		result = self.P.use_parkCoupon()
		self.A.submit_pay()
		Pomp().park_coupon_manager("线上优惠0.01元", "FROZE")
		assert result == True

	@getFunName
	@allure.story("线上优惠-不用缴费")
	def test_parkCoupon_noPayCharge(self):
		Pomp().park_coupon_manager("线上优惠25元", "VALID")
		self.A.pay_charges(self.carNum)
		result = self.P.use_parkCoupon()
		self.A.submit_pay()
		Pomp().park_coupon_manager("线上优惠25元", "FROZE")
		assert result == True

	@getFunName
	@allure.story("积分优惠-需余额缴费")
	def test_scoreCoupon_payCharge(self):
		self.A.pay_charges(self.carNum)
		result = self.P.use_scoreCoupon(isall= False)
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("积分优惠-不用缴费")
	def test_scoreCoupon_noPayCharge(self):
		self.A.pay_charges(self.carNum)
		result = self.P.use_scoreCoupon(isall= True)
		self.A.submit_pay()
		assert result == True

	@getFunName
	@allure.story("使用四种优惠劵方式")
	def test_use_all_coupon_PayCharge(self):
		werXin().send_Business_coupon("UI一点停专用金额扣减0.01", self.carNum)
		commonConpon().send_coupon("UI一点停通用劵")
		Pomp().park_coupon_manager("线上优惠0.01元", "VALID")
		self.A.pay_charges(self.carNum)
		self.P.use_businessCoupon("UI一点停专用金额扣减0.01")
		self.P.use_commonConpon("通用劵0.01元")
		self.P.use_parkCoupon()
		self.P.use_scoreCoupon(isall=False)
		result = self.A.submit_pay()
		Pomp().park_coupon_manager("线上优惠0.01元", "FROZE")
		assert result == True