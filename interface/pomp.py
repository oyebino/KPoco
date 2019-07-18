import requests
import json
from interface.db_opertor import db_opertor
from Config.Config import Config
from common.logger import logger as log


class Pomp(object):
    """月票管理接口方法"""
    def __init__(self):
        self.host = Config().pomp_host
        seccodeUrl = self.host + "/mgr/normal/authz/seccode.do"
        verify_seccode = self.host + "/mgr/normal/authz/verify_seccode.do"
        loginURl = self.host + "/mgr/normal/ajax/login.do"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }
        self.S = requests.Session()
        self.S.get(seccodeUrl)
        seccodeData = {"seccode": 9999}
        self.S.post(verify_seccode, data=seccodeData)
        data = {
            "username": "autotest",
            "password": "123456",
            "seccode": 9999
        }
        self.S.post(loginURl, data, headers=headers)

    def refund_monthTicket(self,carNum="粤A99999"):
        """月票退款"""
        sql = "SELECT ID from month_ticket_bill where CAR_CODE ='{}' and VALID_STATUS ='0'".format(carNum)
        db = db_opertor()
        db.open()
        try:
            monthTicketBillId = db.select(sql)[0][0]
            refundUrl = self.host + "/mgr/monthTicketBill/refund.do"
            refundData = {
                "monthTicketBillId": "{}".format(monthTicketBillId),
                "refundValue": "1",
                "remark": "11",
                "realValue": "100"
            }
            result = self.S.post(refundUrl, refundData)
            # print(result.status_code)
            if result.status_code == 200:
                log.info("【{}】车辆月票退款成功".format(carNum))
            else:
                log.error("【{}】车辆月票退款失败".format(carNum))
        except Exception as e:
            log.error("退款失败，该车辆没有开通月票,{}".format(e))

    def park_coupon_manager(self,couponName,state):
        #state in FROZE or VALID
        """支付优惠管理"""
        sql = "SELECT ID from park_compaign_coupon where COUPON_NAME = '{}'".format(couponName)
        db = db_opertor()
        db.open()
        couponId = db.select(sql)[0][0]
        path = self.host + "/mgr/compaign/updateStatus.do"
        data = {
            "ids": "{}".format(couponId),
            "validStatus": "{}".format(state)
        }
        r = self.S.post(path,data)
        log.info("线上停车场优惠【{}】设置【{}】{}".format(couponName,state,r.json()['message']))

    def open_monthTicket(self,carNum):
        """开通月票"""
        path = self.host + "/mgr/monthTicketBill/open.do"
        data = {
            "monthTicketId":868,
            "timeperiodListStr":"2018-12-01 00:00:00 - 2019-12-31 23:59:59",
            "userName":"UI",
            "userPhone":"13800138000",
            "carCode": "{}".format(carNum),
            "price": 30,
            "totalValue":30,
            "renewTimeLength":1,
            "realValue":1
        }
        r = self.S.post(path, data)
        log.info("【{}】车辆月票开通{}".format(carNum,r.json()['message']))


class werXin(object):
    """商家劵"""
    def __init__(self, host= "https://ydtw.k8s.yidianting.com.cn"):
        self.host = host
        loginUrl = self.host + "/mgr-weixin/passport/signin.do"
        self.S = requests.session()
        data = {
            "username": "13531412589",
            "password": "123456"
        }
        self.S.post(loginUrl, data)

    def send_Business_coupon(self,coupon_name,carNum):
        """下发商家劵"""
        sql = "SELECT ID FROM park_trader_coupon_sell_bill psb WHERE psb.COUPON_TMP_ID in(SELECT ID FROM park_trader_coupon_template WHERE `NAME`='{}') ORDER BY ID DESC LIMIT 1 ".format(coupon_name)
        db = db_opertor()
        db.open()
        sellId = db.select(sql)[0][0]
        path = self.host + "/mgr-weixin/coupon/grant/grantCouponToCar.do"
        data = {
            "sellBillId": "{}".format(sellId),
            "carCode": "{}".format(carNum),
            "checkExisted": ""
        }
        print(data)
        result = self.S.post(path,data)
        log.info("微信下发商家劵【{}】到车辆【{}】{}".format(coupon_name,carNum,result.json()['message']))


if __name__ == '__main__':
    a = werXin()
    # b = Pomp()
    # b.refund_monthTicket(carNum="粤A99999")
    # b.park_coupon_manager("线上优惠25元", "FROZE")
    # FROZE     VALID
    a.send_Business_coupon("UI一点停专用固定劵0.22元","粤A99999")
    # b.open_monthTicket("粤A99998")