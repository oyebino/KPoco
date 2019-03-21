import requests
import json
from interface.db_opertor import db_opertor
from Config.Config import Config
from common.logger import logger as log

class commonConpon(object):
    def __init__(self):
        self.host = Config().aomp_host
        seccodeUrl = self.host + "/getValidateCode.do"
        checkLoginUrl = self.host + "/checkLogin.do"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        self.S = requests.Session()
        self.S.get(seccodeUrl)
        data = {
            "user": "uiauto",
            "pwd": "123456",
            "isOnLine": "isOnLine",
            "flag": -1,
            "validateCode": 9999
        }
        result =self.S.post(checkLoginUrl, data, headers=headers)
        # print(result.json())


    def send_coupon(self,couponName):
        """下发通用劵"""
        sql = "select ID from coupon_template where name = '{}'".format(couponName)
        db = db_opertor()
        db.open()
        couponId = db.select(sql)[0][0]
        path = self.host + "/coupon/sendCouponS.do"
        data = {
            "couponId": "{}".format(couponId),
            "chooseArray": "3634"   #用户ID
        }
        result = self.S.post(path, data)
        # print(result.json())
        log.info("【{}】通用劵下发{}".format(couponName,result.json()['message']))




if __name__ == '__main__':
    b = commonConpon()
    b.send_coupon("UI一点停通用劵")
