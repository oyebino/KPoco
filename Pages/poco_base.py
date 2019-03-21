
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 10:47
# @Author  : 叶永彬
# @File    : meSetting_page.py

import os
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.aircv.error import FileNotExistError
from common.logger import logger
from poco.exceptions import *
import common.ParamConstant
import time


class PocoBase():

    def __init__(self):

        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

        self.log = logger

    def click(self,obj):
        """
        点击
        :param obj: poco对象
        :return:
        """
        try:
            obj.wait_for_appearance(timeout=20)
            obj.click()
            self.web_loading()
            self.log.info(str(obj)[17:] + "点击成功")
        except PocoTargetTimeout:
            self.log.error(str(obj)[17:] + "没有显示")
            raise PocoTargetTimeout

    def swipe_poco(self,obj,direction):
        """
        滑动一段距离
        :param obj: poco对象
        :param direction: 'up','down','left','right',
        :return:
        """
        try:
            obj.wait_for_appearance(timeout=20)
            obj.swipe(direction,duration=1)
            self.log.info(str(obj)[17:] + "向" + direction + "滑动成功")
        except PocoTargetTimeout:
            self.log.error(str(obj)[17:] + "没有找到")
            raise PocoTargetTimeout

    def swipe_pic(self, v,vector=None):
        """
        滑动一段距离
        :param v: 图片
        :param vector: 滑动方向的坐标,
        :return:
        """
        try:
            wait(v)
            swipe(v,vector = vector)
            self.log.info(str(v) + "向" + str(vector) + "滑动成功")
        except TargetNotFoundError:
            self.log.error(str(v) + "没有找到")
            raise TargetNotFoundError

    def touch(self,v):
        """
        识别图片进行点击
        :param v:
        :return:
        """
        try:
            wait(v)
            touch(v)
            self.log.info(str(v)+ "点击成功")
        except TargetNotFoundError:
            self.log.error(str(v)+ "没有找到")
            raise TargetNotFoundError
        except FileNotExistError:
            self.log.error(str(v) + "图片路径找不到")
            raise FileNotExistError

    def isContains(self,actual,expected):
        """
        检查文本是不是包含
        :param actual:
        :param expected:
        :return:
        """
        try:
            if actual in expected:
                result = True
            else:
                result =False
            assert_equal(result,True)
            self.log.info("实际文本【{}】包含期望文本【{}】".format(actual,expected))
        except AssertionError:
            self.log.error("实际文本【{}】不包含期望文本【{}】".format(actual,expected))

    def isTextCorrect(self,actual,expected):
        """
        检查文本是否一致
        :param actual:
        :param expected:
        :return:
        """
        try:
            if actual == expected:
                result = True
            else:
                result =False
            # assert_equal(result,True)
            self.assertTrue(result)
            self.log.info("找到了期望的文字:【" +expected+ "】")
        except AssertionError:
            self.log.error("期望的文字是 【" + expected + "】 但是找到了 【" + actual + "】")

    def getName(self,obj):
        """
        获取poco对象的name值
        :param obj: poco对象
        :return: str
        """
        try:
            obj.wait_for_appearance(timeout=20)
            nameValue = obj.get_name()
            return nameValue
        except PocoTargetTimeout:
            self.log.error(str(obj)[17:] + "没有显示")
            raise PocoTargetTimeout

    def exists_poco(self,obj):
        """
        poco对象是否存在
        :param obj:
        :return:T or F
        """
        if obj.exists:
            self.log.info( str(obj)[17:] + "已存在")
            return True
        else:
            self.log.error(str(obj)[17:] + "不存在")
            return False

    def exists_pic(self,v):
        """
        判断图片是否存在
        :param v:
        :return:
        """
        if exists(v):
            self.log.info("已找到验证图片" + str(v))
            return True
        else:
            # self.log.error("没有找到验证图片" + str(v))
            return False

    def wait(self,obj,timeout = 20):
        """
        等待poco对象出现
        :param obj:
        :return:
        """
        try:
            obj.wait_for_appearance(timeout=timeout)
            # self.log.info(str(obj)[17:] + "已出现")
        except PocoTargetTimeout:
            self.log.error(str(obj)[17:] + "没有出现")
            raise PocoTargetTimeout

    def screenshot(self,fileName):
        """
	    截图方法
	    :param fileName: 输入截图名称
	    :return:返回一个时间戳+名称的图图片
	    """
        filePath =str(common.ParamConstant.screenshotPath) + str(time.time()).split(".")[0] + fileName +".png"
        if str(common.ParamConstant.screenshotPath) =="":
            return
        if not os.path.exists(str(common.ParamConstant.screenshotPath)):
            os.makedirs(str(common.ParamConstant.screenshotPath))
        snapshot(filename =filePath)
        self.log.info("截图成功...")

    def web_loading(self):
        """等待加载"""
        sleep(0.2)
        for num in range(0, 30):
            if self.poco("数据加载中").exists():
                sleep(0.1)
            else:
                sleep(0.2)
                break