#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 11:05
# @Author  : 叶永彬
# @File    : baseCommon.py

import os,sys
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(BASE_DIR, ".."))
import common.ParamConstant
import os
import stat
import shutil

def getFunName(func):
	def wrapper(*args, **kwargs):
		common.ParamConstant.screenshotPath = root_path + "/result/screenshot/" + func.__name__ + "/"
		if os.path.exists(common.ParamConstant.screenshotPath):
			delete_file(common.ParamConstant.screenshotPath)
		return func(*args, **kwargs)
	return wrapper


def delete_file(filePath):
	if os.path.exists(filePath):
		for fileList in os.walk(filePath):
			for name in fileList[2]:
				os.chmod(os.path.join(fileList[0],name), stat.S_IWRITE)
				os.remove(os.path.join(fileList[0],name))
		shutil.rmtree(filePath)
		print("delete OK")
	else:
		print("no filepath")


def getFileName(func):
	def wrapper(*args, **kwargs):
		# common.ParamConstant.screenshotPath = root_path + "/result/screenshot/" +func.__name__ + "/"
		print(str(os.path.basename(sys.argv[0]).split(".")[0]))
		# if os.path.exists(common.ParamConstant.screenshotPath):
		# 	delete_file(common.ParamConstant.screenshotPath)
		return func(*args, **kwargs)
	return wrapper