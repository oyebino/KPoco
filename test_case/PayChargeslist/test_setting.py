#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 11:06
# @Author  : 叶永彬
# @File    : test_setting.py

from Pages.meSetting_page import SettingPage
import unittest
import allure
from common.baseCommon import getFunName

@allure.feature("设置模块")
class TestSetting(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.S = SettingPage()

	@classmethod
	def tearDownClass(cls):
		pass

	@allure.story("设置开启信息提醒功能")
	@getFunName
	def test_setting_message_remind_aopen(self):
		"""
		用例描述：设置开启信息提醒功能
		"""
		result = self.S.set_message_remind_open()
		assert result == True

	@getFunName
	@allure.story("设置关闭信息提醒功能")
	def test_setting_message_remind_close(self):
		"""
		用例描述：设置关闭信息提醒功能
		"""
		result = self.S.set_message_remind_close()
		assert result == True

	@getFunName
	@allure.story("设置开启允许他人查询功能")
	def test_setting_allow_check_other_aopen(self):
		"""
		用例描述：设置开启允许他人查询功能
		"""
		result = self.S.set_allow_check_other_open()
		assert result == True

	@getFunName
	@allure.story("设置关闭允许他人查询功能")
	def test_setting_allow_check_other_close(self):
		"""
		用例描述：设置关闭允许他人查询功能
		"""
		result = self.S.set_allow_check_other_close()
		assert result == True