#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 15:56
# @Author  : 叶永彬
# @File    : payCoupon_page.py

import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(BASE_DIR, "../.."))
from airtest.core.api import *
from Pages.poco_base import PocoBase

class PayCouponPage(PocoBase):
	"""支付优惠劵界面"""
	def __init__(self,PKG ="com.tencent.mm"):
		self.PKG = PKG
		super(PayCouponPage, self).__init__()

	def use_scoreCoupon(self,isall = True):
		"""停车场积分抵扣金额"""
		try:
			self.touch(Template(BASE_DIR + r"\img\停车场积分抵扣金额开关.png", threshold=0.7, target_pos=5, rgb=False, record_pos=(0.321, -0.199),resolution=(1080, 1920)))
			self.log.info("点击开启停车场积分抵扣开关")
			# self.screenshot("开启停车场积分抵扣开关界面")
			if self.exists_pic(Template(BASE_DIR + r"\img\抵扣金额.png", threshold=0.7, record_pos=(-0.291, -0.069),resolution=(1080, 1920))):
				self.log.info("停车场积分抵扣金额开关已开启")
				if isall:
					self.log.info("停车场积分抵扣全部金额")
					use_scoreCoupon = True
					return use_scoreCoupon
				else:
					self.touch(Template(BASE_DIR + r"\img\抵扣金额.png", threshold=0.7, target_pos=6, rgb=False, record_pos=(-0.291, -0.069),resolution=(1080, 1920)))
					use_scoreCoupon = True
					self.log.info("点击减少积分折扣金额")
			else:
				self.log.error("停车场积分抵扣金额开关开启失败")
				use_scoreCoupon = False
		except TargetNotFoundError:
			use_scoreCoupon = False
			self.log.error("没有停车场积分抵扣的优惠功能")
		return 	use_scoreCoupon

	def use_parkCoupon(self):
		"""线上优惠"""
		if self.exists_poco(self.poco("车场优惠")):
			self.log.info("停车场线上优惠已开启")
			use_parkCoupon = True
		else:
			self.log.error("停车场线上线上优惠不存在")
			use_parkCoupon = False
		return use_parkCoupon

	def use_commonConpon(self,commonConponName):
		"""通用劵"""
		try:
			if self.exists_poco(self.poco("通用停车券")):
				self.click(self.poco("通用停车券"))
				self.log.info("点击打开通用停车券")
				if self.exists_pic(
					Template(BASE_DIR + r"\img\\" + commonConponName + ".png", threshold=0.70, target_pos=5, rgb=False, record_pos=(0.324, -0.081),resolution=(1080, 1920))):
					self.touch(Template(BASE_DIR + r"\img\\" + commonConponName + ".png", threshold=0.70, target_pos=5, rgb=False,record_pos=(0.324, -0.081), resolution=(1080, 1920)))
					use_commonConpon = True
					self.log.info("选择通用劵【{}】".format(commonConponName))
					self.screenshot("选择通用劵界面")
					home()
					start_app(self.PKG)
					sleep(2)
				else:
					self.log.error("没有该通用劵【{}】".format(commonConponName))
					use_commonConpon = False
			else:
				self.log.error("没有通用劵【{}】".format(commonConponName))
				use_commonConpon = False
		except TargetNotFoundError:
			self.log.error("没有该通用劵【{}】".format(commonConponName))
			use_commonConpon = False
		return use_commonConpon


	def use_businessCoupon(self,businessCoupon_name):
		"""使用商家劵"""
		if self.exists_poco(self.poco("优惠券")):
			self.click(self.poco("优惠券"))
			self.log.info("成功点击优惠劵")
			if self.exists_poco(self.poco(businessCoupon_name)):
				self.click(self.poco(businessCoupon_name))
				self.click(self.poco("确定"))
				self.log.info("成功选择商家劵【{}】".format(businessCoupon_name))
				self.screenshot("选择商家劵界面")
				home()
				start_app(self.PKG)
				sleep(2)
				use_businessCoupon = True
			else:
				self.log.error("用户没有该商家优惠劵：【{}】".format(businessCoupon_name))
				use_businessCoupon = False
		else:
			self.log.error("用户没有存在的商家劵:【{}】".format(businessCoupon_name))
			use_businessCoupon = False
		return use_businessCoupon
