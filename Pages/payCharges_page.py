#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 16:29
# @Author  : 叶永彬
# @File    : payCharges_page.py

from airtest.core.api import *
import random,string
from Pages.poco_base import PocoBase
import os
from airtest.aircv.error import FileNotExistError
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(BASE_DIR, "../.."))

class ChargesPage(PocoBase):
	"""一点停公众号交费界面"""
	def __init__(self,PKG ="com.tencent.mm"):
		self.PKG = PKG
		super(ChargesPage, self).__init__()

	def carNum_transform(self,carNum):
		"""转换成poco可以识别的车牌属性"""
		return carNum[0:2] + "·" + carNum[2:] + " "

	def choose_carCode(self,carNum):
		"""选择车牌界面"""
		self.web_refresh()
		try:
			if carNum == "+":
				# carCode = "javascript:;"
				for num in range(0,3):
					if self.exists_pic(Template(BASE_DIR + r"\img\添加车牌.png", threshold=0.8,target_pos=4, rgb=False ,record_pos=(0.003, -0.56), resolution=(1080, 1920))):
						self.log.info("切换到【+】增加车牌")
						self.screenshot("添加车牌界面")
						return
					else:
						self.swipe_pic(Template(BASE_DIR + r"\img\拖动车牌.png", threshold=0.7, target_pos=4, rgb=False,record_pos=(0.376, -0.556), resolution=(1080, 1920)), vector=[-0.7958, -0.0091])
						self.web_loading()
				# self.log.error("没有可添加车牌的位置")
				raise TargetNotFoundError
				# assert False
			else:
				carCode = self.carNum_transform(carNum)
				for num in range(0, 3):
					if self.exists_poco(self.poco(carCode)):
						sleep(1)
						pox =self.poco(carCode).get_position()
						if self.checkCarNumPox(pox) == [0,0]:
							if carNum[3:8] in self.poco(carCode).get_name():
								self.log.info("成功切换车牌为:【{}】".format(carNum))
								self.screenshot("{}车牌界面".format(carNum))
								return
						else:
							self.swipe_pic(Template(BASE_DIR + r"\img\拖动车牌.png", threshold=0.7, target_pos=4, rgb=False,record_pos=(0.376, -0.556), resolution=(1080, 1920)), vector=[-0.7958, -0.0091])
							self.web_loading()
					else:
						self.swipe_pic(Template(BASE_DIR + r"\img\拖动车牌.png", threshold=0.8, target_pos=4, rgb=False,record_pos=(0.376, -0.556), resolution=(1080, 1920)), vector=[-0.7958, -0.0091])
						self.web_loading()
				# self.log.error("没有绑定该车牌:【{}】".format(carNum))
				raise TargetNotFoundError
				# assert False
		except FileNotExistError:
			self.log.error("拖动车牌图片不存在.")
		except TargetNotFoundError:
			self.log.error("没有【{}】车牌的位置".format(carNum))

	def keySet_carNum(self,carNum,carType = "蓝牌"):
		if carType == "蓝牌":
			pass
		else:
			self.click(self.poco(carType))
		self.log.info("选择车牌类型为【{}】".format(carType))
		if carType == "民航":
			carCode = carNum[2:]
			home()
			start_app(self.PKG)
		else:
			first = carNum[0:1]
			self.poco(first).click()
			home()
			start_app(self.PKG)
			carCode = carNum[1:]
		for s in carCode:
			self.poco(s).click()
		# self.click(self.poco("请确定您选择了正确的车牌种类"))
		self.log.info("成功输入车牌【{}】".format(carNum))
		self.screenshot("输入车牌界面")
		home()
		start_app(self.PKG)

	def binding_carCode(self ,carNum ,carType = "蓝牌"):
		"""绑定车牌"""
		self.choose_carCode("+")
		self.touch(Template(BASE_DIR + r"\img\添加车牌.png", record_pos=(0.003, -0.56), resolution=(1080, 1920)))
		self.keySet_carNum(carNum,carType)
		self.click(self.poco("确认添加"))
		# poco("绑定成功").wait_for_appearance(timeout=30)
		car = self.carNum_transform(carNum)
		self.web_loading()
		self.wait(self.poco(car))
		if self.exists_poco(self.poco(car)):
			self.log.info("车牌【{}】绑定成功".format(carNum))
			self.screenshot("车牌【{}】绑定成功界面".format(carNum))
			binding_carCode = True
		else:
			self.log.error("绑定失败")
			binding_carCode = False
		return binding_carCode

	def del_carCode(self,carNum):
		"""去除绑定车牌"""
		self.choose_carCode(carNum)
		carCode = self.carNum_transform(carNum)
		# sleep(3)
		self.web_loading()
		self.click(self.poco(carCode))
		try:
			self.touch(Template(BASE_DIR + r"\img\点击车牌按钮.png", threshold=0.7, target_pos=8, rgb=False, record_pos=(0.008, 0.598), resolution=(1080, 1920)))
		except TargetNotFoundError:
			self.log.error("没有找到该删除菜单")
			assert False
		# poco("删除车牌成功").wait_for_appearance()
		if self.exists_poco(self.poco("删除车牌成功")):
			self.log.info("【{}】车牌删除成功".format(carNum))
			self.screenshot("车牌删除成功界面")
			del_carCode =True
		else:
			self.log.error("【{}】车牌删除失败".format(carNum))
			del_carCode =False
		return del_carCode

	def lock_car(self,carNum):
		"""锁车"""
		self.choose_carCode(carNum)
		self.click(self.poco("锁车"))
		sleep(2)
		try:
			if self.exists_pic(Template(BASE_DIR + r"\img\锁车图标.png", threshold=0.70, rgb=True, record_pos=(-0.109, 0.402), resolution=(1080, 1920))):
				self.log.info("锁车成功")
				self.screenshot("锁车成功界面")
				lock_car =True
			else:
				self.log.error("锁车失败")
				self.screenshot("锁车失败界面")
				assert False
		except TargetNotFoundError:
			self.log.error("锁车图片不存在")
			lock_car = False
			assert False
		return lock_car

	def unlock_car(self,carNum):
		"""解锁"""
		self.choose_carCode(carNum)
		self.click(self.poco("锁车"))
		sleep(2)
		try:
			if self.exists_pic(Template(BASE_DIR + r"\img\解锁图标.png", threshold=0.70, rgb=True, record_pos=(-0.109, 0.402), resolution=(1080, 1920))):
				self.log.info("解锁成功")
				unlock_car = True
				self.screenshot("解锁成功界面")
			else:
				self.log.error("解锁失败")
				self.screenshot("解锁失败界面")
				assert False
		except TargetNotFoundError:
			self.log.error("解锁图片不存在")
			assert False
		return unlock_car

	def pay_charges(self,carNum):
		"""付款界面"""
		self.choose_carCode(carNum)
		self.web_loading()
		self.click(self.poco("付费离场"))
		self.poco(nameMatches="余额.*").wait_for_appearance(timeout=30)
		self.click(self.poco(nameMatches="余额.*"))
		if self.exists_poco(self.poco(nameMatches="余额.*")):
			self.log.info("进入付款界面")
			self.screenshot("付款界面")
			return True


	def check_amount(self):
		"""检查金额比对"""
		check_money = float(self.poco(nameMatches="¥.*").get_name()[1:])
		if self.poco(nameMatches="¥ .*").exists():
			pay_money = float(self.poco(nameMatches="¥ .*").get_name()[2:])
		else:
			pay_money = float(self.poco(nameMatches="需支付.*").get_name()[5:])
		discount_money = 0
		if self.poco(nameMatches="-¥.*").exists():
			discountPocos = self.poco(nameMatches="-¥.*")
			for pocoName in discountPocos:
				value = float(pocoName.get_name()[2:])
				discount_money = discount_money + value
		if self.cal_amount(check_money, pay_money,discount_money):
			self.log.info("需付金额【{}】 = 查询金额【{}】- 优惠金额【{}】".format(pay_money,check_money,discount_money))
			pay_charges = True
		else:
			self.log.error("需付金额【{}】!=查询金额【{}】- 优惠金额【{}】".format(pay_money,check_money,discount_money))
			pay_charges = False
		assert pay_charges == True


	def submit_pay(self,type="余额"):
		"""确认支付操作"""
		if type =="余额":
			self.check_amount()
			if not self.poco("确认支付").attr("touchable")== "True":
				sleep(3)
			self.click(self.poco("确认支付"))
			self.web_loading()
			self.wait(self.poco(nameMatches =".*成功"))
			if "成功" in self.getName(self.poco(nameMatches =".*成功")):
				self.log.info("成功支付")
				self.screenshot("成功支付界面")
				submit_pay = True
			else:
				self.log.error("支付失败")
				submit_pay = False
		else:
			self.click(self.poco("微信支付"))
			self.click(self.poco("确认支付"))
			self.web_loading()
			self.wait(self.poco(text="立即支付"))
			if self.exists_poco(self.poco(text="立即支付")):
				self.log.info("微信成功支付")
				self.screenshot("微信成功支付界面")
				submit_pay = True
			else:
				self.log.error("微信支付失败")
				submit_pay = False
		return submit_pay


	def cal_amount(self,check_money,pay_money,discount_money,isFree =False):
		"""余额比对"""
		cal_amount = False
		if isFree:
			cal_amount =True
			return cal_amount
		else:
			value = float(round(check_money - discount_money, 2))
			if value == pay_money:
				cal_amount = True
		return cal_amount

	def create_carNum(self,uppercase_num =1,digits_num =5,carType=None):
		"""创建随机车牌"""
		ascii_uppercase = 'ABCDEGHJKLMNPQRSTWXY'
		src_digits = string.digits  # string_数字
		src_uppercase = ascii_uppercase  # string_大写字母
		# 生成字符串
		carNum = random.sample(src_uppercase, uppercase_num) + random.sample(src_digits, digits_num)
		# 列表转字符串
		if carType == "民航":
			new_carNum = "民航" + ''.join(carNum)[1:]
		elif carType == "新能源":
			new_carNum = "粤" + ''.join(carNum) + "F"
		else:
			new_carNum = "粤" + ''.join(carNum)
		return new_carNum

	def set_often_carNum(self,carNum):
		"""设置常用车牌"""
		self.choose_carCode(carNum)
		carCode = self.carNum_transform(carNum)
		self.click(self.poco(carCode))
		try:
			self.touch(Template(BASE_DIR + r"\img\点击车牌按钮.png", threshold=0.7, target_pos=2, rgb=False, record_pos=(0.008, 0.598),resolution=(1080, 1920)))
		except TargetNotFoundError:
			self.log.error("点击车牌菜单不存在")
			assert False
		if self.exists_poco(self.poco("常用车牌设置成功")):
			set_often_carNum = True
			self.screenshot("常用车牌设置成功界面")
			self.log.info("{}常用车牌设置成功".format(carNum))
		else:
			set_often_carNum = False
			self.log.error("{}常用车牌设置失败".format(carNum))
		return set_often_carNum

	def web_refresh(self):
		if self.poco("com.tencent.mm:id/j1").exists():
			self.poco("com.tencent.mm:id/j1").click()
		else:
			self.poco("com.tencent.mm:id/jr").click()
		self.poco(text="刷新").click()
		self.poco("我").wait_for_appearance(timeout=20)
		self.web_loading()
		self.log.info("刷新页面成功")

	def web_loading(self):
		"""等待加载"""
		sleep(0.5)
		for num in range(0,30):
			if self.poco("数据加载中").exists():
				sleep(1)
			if self.poco("正在登录中...").exists():
				sleep(1)
			else:
				sleep(0.5)
				break

	def pay_with_another(self,carNum):
		self.choose_carCode("+")
		self.click(self.poco("代缴停车费"))
		self.wait(self.poco("输入车牌号码"))
		self.input_carNum(carNum)
		self.click(self.poco("查询"))
		self.screenshot("查询代缴停车费界面")
		self.web_loading()
		self.click(self.poco("立即支付"))
		self.wait(self.poco(text="广东艾科智泊科技股份有限公司"))
		result = self.exists_poco(self.poco(text="广东艾科智泊科技股份有限公司"))
		if result:
			self.screenshot("微信代缴成功界面")
			self.log.info("代缴成功")
			pay_with_another = True
		else:
			self.screenshot("微信代缴失败界面")
			self.log.error("代缴失败")
			pay_with_another = False
		return pay_with_another

	def input_carNum(self,carNum):
		self.poco("一点停").child("android.view.View").child("android.view.View")[0].child("android.view.View").click()
		first = carNum[0:1]
		self.click(self.poco(first))
		home()
		start_app(self.PKG)
		carCode = carNum[1:]
		for s in carCode:
			self.click(self.poco(s))


	def back(self,num):
		"""返回次数"""
		for n in range(0,num):
			keyevent("BACK")
			sleep(1)

	def checkCarNumPox(self,pox):
		"""获取车牌的坐标是否在当页面"""
		if pox[0] > 0 and pox[0] < 1:
			if pox[1] > 0 and pox[1] < 1:
				return [0, 0]
		return [1, 1]

if __name__ == "__main__":
	a = ChargesPage()
	# a.choose_carCode("+")
	# a.binding_carCode("粤A78945")
	# a.del_carCode("粤A78945")
	a.lock_car("粤A99999")