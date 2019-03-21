#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 10:47
# @Author  : 叶永彬
# @File    : meSetting_page.py
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(BASE_DIR, "../.."))
from airtest.core.api import *
from Pages.poco_base import PocoBase
from Pages.payCharges_page import ChargesPage
import common.ParamConstant

class SettingPage(PocoBase):
    """我的模式界面"""
    def login_seetingPage(self):
        if self.poco("消息提醒").exists():
            self.log.info("进入【我】-【设置】的模块")
            pass
        else:
            self.click(self.poco("我"))
            self.swipe_poco(self.poco("我的消息"),"up")
            self.swipe_poco(self.poco("我的消息"), "up")
            self.click(self.poco("设置 "))
            self.log.info("进入【我】-【设置】的模块")
            self.screenshot("【我】-【设置】设置模块界面")

    def set_message_remind_open(self):
        """开启消息提醒功能"""
        try:
            result = self.set_operation("消息提醒已关闭","消息提醒已开启")
            if result:
                self.log.info("消息提醒开启设置成功")
                set_message_remind_open = True
            else:
                self.log.error("消息提醒开启设置失败")
                set_message_remind_open = False
        except TargetNotFoundError:
            self.log.error("消息提醒开启设置失败")
            set_message_remind_open = False
        return set_message_remind_open

    def set_message_remind_close(self):
        """关闭消息提醒功能"""
        try:
            result = self.set_operation("消息提醒已开启", "消息提醒已关闭")
            if result:
                self.log.info("消息提醒关闭设置成功")
                set_message_remind_close = True
            else:
                self.log.error("消息提醒关闭设置失败")
                set_message_remind_close = False
        except TargetNotFoundError:
            self.log.error("消息提醒关闭设置失败")
            set_message_remind_close = False
        return set_message_remind_close

    def set_allow_check_other_open(self):
        """允许他人查询开启"""
        try:
            result = self.set_operation("允许他人查询已关闭", "允许他人查询已开启")
            if result:
                self.log.info("允许他人查询开启设置成功")
                set_allow_check_other_open = True
            else:
                self.log.error("允许他人查询开启设置失败")
                set_allow_check_other_open = False
        except TargetNotFoundError:
            self.log.error("允许他人查询开启设置失败")
            set_allow_check_other_open = False
        return set_allow_check_other_open

    def set_allow_check_other_close(self):
        """允许他人查询关闭"""
        try:
            result = self.set_operation("允许他人查询已开启", "允许他人查询已关闭")
            if result:
                self.log.info("允许他人查询关闭设置成功")
                set_allow_check_other_close = True
            else:
                self.log.error("允许他人查询关闭设置失败")
                set_allow_check_other_close = False
        except TargetNotFoundError:
            self.log.error("允许他人查询关闭设置失败")
            set_allow_check_other_close = False
        return set_allow_check_other_close


    def set_operation(self,operation_value,expect_value):
        ChargesPage().web_refresh()
        self.login_seetingPage()
        self.touch(
            Template(BASE_DIR + r"\img\\" + operation_value + ".png", threshold=0.70, target_pos=6, rgb=True, record_pos=(-0.012, -0.481),
                     resolution=(1080, 1920)))
        if self.exists_poco(self.poco("设置成功")):
            if self.exists_pic(Template(BASE_DIR + r"\img\\" + expect_value + ".png", threshold=0.70, target_pos=6, rgb=True, record_pos=(-0.012, -0.481), resolution=(1080, 1920))):
                set_message_remind = True
                self.screenshot(expect_value + '界面')
            else:
                pass
        else:
            set_message_remind = False
            self.screenshot("设置失败")
        return set_message_remind

if __name__ == "__main__":
    a = SettingPage()
    a.set_message_remind_open()