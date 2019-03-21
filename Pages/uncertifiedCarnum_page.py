#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 9:48
# @Author  : 叶永彬
# @File    : uncertifiedCarnum_page.py

from airtest.core.api import *
from Pages.payCharges_page import ChargesPage
from Pages.poco_base import PocoBase
import inspect

class UncertifiedCarPage(PocoBase):
	"""未认证车辆界面"""
	def __init__(self,carNum):
		self.P = ChargesPage()
		self.carNum = carNum
		super(UncertifiedCarPage, self).__init__()

	def find_uncertified_warm(self):
		"""返回车牌下方验证提醒"""
		self.P.choose_carCode(self.carNum)
		carCode = self.P.carNum_transform(self.carNum).strip()
		text = self.poco(carCode + "车辆未认证，点击认证").get_name()
		return text

	def find_uncertified_carPicture_warn(self):
		"""返回进场图片会弹出要提示认证的提醒"""
		return self.get_pocoValue("查看进场图片需要行驶证认证","进场图片")

	def find_uncertified_lock_warn(self):
		"""返回上锁弹出要提示认证的提醒"""
		return self.get_pocoValue("锁车需要行驶证认证", "锁车")

	def find_uncertified_parkingName(self):
		"""返回停车场名为“***停车场”"""
		return self.get_pocoValue("***停车场")

	def Uncertified_monthTicketDetail_authorize_warn(self,carNum):
		"""返回月票详情和授权会弹出要认证提醒"""
		self.click(self.poco("月票"))
		home()
		start_app("com.tencent.mm")
		carVaule = self.getName(self.poco(nameMatches="车牌号:.*"))
		for num in range(0,2):
			if carNum in carVaule:
				self.click(self.poco("访客授权"))
				text = self.getName(self.poco("访客授权需行驶证认证"))
				self.screenshot("提示框界面")
				self.click(self.poco("取消 "))
				return text
				# break
			else:
				self.swipe_poco(self.poco(nameMatches="车牌号.*"),[-0.5, 0])
				home()
				start_app("com.tencent.mm")

	def get_pocoValue(self,check_poco,click_poco = None):
		self.P.choose_carCode(self.carNum)
		if click_poco:
			self.click(self.poco(click_poco))
			self.screenshot("提示框界面")
		return self.getName(self.poco(check_poco))
