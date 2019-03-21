#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 11:01
# @Author  : 叶永彬
# @File    : commonFun.py

class common():
	def cal_amount(self,check_money,discount_money,pay_money,isFree):
		"""余额比对"""
		cal_amount = False
		if isFree:
			cal_amount =True
			return cal_amount
		else:
			value = check_money - discount_money
			if value == pay_money:
				cal_amount = True
		return cal_amount

