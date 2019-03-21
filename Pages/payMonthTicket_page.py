#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 10:58
# @Author  : 叶永彬
# @File    : payMonthTicket_page.py

from Pages.poco_base import PocoBase
from airtest.core.api import *
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
from Pages.payCharges_page import ChargesPage


class PayMonthTicketPage(PocoBase):
	"""月票界面"""

	def login_monthTicketPage(self):
		ChargesPage().web_refresh()
		self.click(self.poco("月票"))
		self.screenshot("月票界面")

	def renew_monthTicket(self):
		self.login_monthTicketPage()
		self.click(self.poco("续期"))
		self.touch(Template(BASE_DIR + r"\img\勾选已阅读.png", threshold=0.7 , target_pos=4, resolution=(1080, 1920)))
		self.screenshot("月票续约付款界面")
		self.click(self.poco("确认支付"))
		return ChargesPage().submit_pay()

	def buy_monthTicket(self,parking):
		self.login_monthTicketPage()
		self.click(self.poco("购买月票"))
		return self.submit_monthTicket(parking)

	def submit_monthTicket(self,parking):
		self.click(self.poco("请选择停车场"))
		self.click(self.poco(parking))
		self.click(self.poco("车牌号"))
		self.touch(Template(BASE_DIR + r"\img\选择车牌.png",target_pos=8, record_pos=(0.02, 0.529), resolution=(1080, 1920)))
		self.touch(Template(BASE_DIR + r"\img\勾选已阅读.png",threshold=0.7 ,target_pos=4,  resolution=(1080, 1920)))
		self.screenshot("月票付款界面")
		self.click(self.poco("确认支付"))
		return ChargesPage().submit_pay()

	def visitor_authorization(self,carNum,time = "once"):
		self.login_monthTicketPage()
		self.click(self.poco("访客授权"))
		self.click(self.poco("继续授权"))
		self.click(self.poco("添加车牌"))
		ChargesPage().keySet_carNum(carNum)
		self.screenshot("授权界面")
		self.click(self.poco("确认授权"))
		if time == "once":
			self.touch(Template(BASE_DIR + r"\img\车辆授权次数.png", threshold=0.7, target_pos=7, rgb=False, record_pos=(0.01, 0.08), resolution=(1080, 1920)))
		else:
			self.touch(Template(BASE_DIR + r"\img\车辆授权次数.png", threshold=0.7, target_pos=9, rgb=False, record_pos=(0.01, 0.08),resolution=(1080, 1920)))
		sleep(3)
		if self.poco("不限").exists():
			self.screenshot("授权结果界面")
			return "不限次数"
		else:
			self.screenshot("授权结果界面")
			return "授权一次"

	def del_visitorCar(self):
		self.touch(Template(BASE_DIR + r"\img\访客车辆.png", threshold=0.7, target_pos=6, rgb=False, record_pos=(0.302, -0.358), resolution=(1080, 1920)))

	def check_details(self):
		self.login_monthTicketPage()
		self.click(self.poco("详情"))
		self.screenshot("查看详情界面")
		return self.poco("自动化测试停车场").get_name()