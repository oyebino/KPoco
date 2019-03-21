import requests
import json
import time
from Config.Config import Config
from common.logger import logger as log

class ApiCase(object):
    """车辆进出场接口方法"""
    dic = {}
    def __init__(self,carNum = None):

        self.url = Config().vems_host
        self.carNum = carNum
        self.usernameToken = self.get_center_people_token()
        self.realTimeCarSeq = ""
        self.stopTime = ""
        self.basicFee = ""
        self.taxPay = ""
        self.chargingTime = ""
        self.enterTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 1800))

    """车辆进场"""
    def car_run_inside(self):
        path = "/vems/cxfService/rest/gateWayInformation"
        urlpath = self.url + path
        payload = {
            "command": "REPORT_CAR_IN_LIST",
            "message_id": "4186",
            "sign_type": "MD5",
            "device_id": "0000000000000000000000149718F9DC",
            "sign": "62f6362a5a857c5ed31ff67c15b30cb4",
            "charset": "utf-8",
            "timestamp": "20180421161529354",
            "biz_content": {
                "enter_info_list": [{
                    "parking_lot_seq": "1",
                    "parking_area_seq": "2",
                    "car_license_number": "%s" % self.carNum,
                    "confidence": "92",
                    "total_amount": "0",
                    "discount_validate_value": "",
                    "discount_no": "",
                    "discount_name": "",
                    "amount_receivable": "0",
                    "discount_amount": "0",
                    "actual_receivable": "0",
                    "pay_status": "0",
                    "payment_mode": "1",
                    "pay_origin": "1",
                    "toll_collector_name": "",
                    "toll_collector_time": "",
                    "last_pay_time": "",
                    "enter_car_license_number": "%s" % self.carNum,
                    "enter_car_card_number": "",
                    "enter_time": "%s" % self.enterTime,
                    "enter_vip_type": "1",
                    "enter_vip_ticket_seq": "",
                    "enter_channel": "1",
                    "enter_type": "1",
                    "enter_speed": "0",
                    "enter_car_license_color": "1",
                    "enter_car_color": "0",
                    "enter_car_logo": "0",
                    "enter_car_license_type": "0",
                    "enter_car_full_picture": "/picpath/2018/04/21/00000000000/1/car/1_1_92_20180421161520_T20161.jpg",
                    "enter_car_license_picture": "/picpath/2018/04/21/00000000000/1/plate/1_1_92_20180421161520_T20161_plate.jpg",
                    "enter_car_type": "1",
                    "enter_recognition_confidence": "92",
                    "in_operator_name": "System",
                    "in_operator_time": "%s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                    "leave_car_license_number": "",
                    "leave_car_card_number": "",
                    "leave_time": "",
                    "leave_channel": "1",
                    "leave_vip_type": "1",
                    "leave_vip_ticket_seq": "",
                    "leave_type": "0",
                    "leave_speed": "0",
                    "leave_car_license_color": "0",
                    "leave_car_color": "0",
                    "leave_car_logo": "0",
                    "leave_car_license_type": "0",
                    "leave_car_full_picture": "",
                    "leave_car_license_picture": "",
                    "leave_car_type": "1",
                    "leave_recognition_confidence": "0",
                    "correct_type": "0",
                    "out_operator_name": "",
                    "out_operator_time": "",
                    "record_type": "0",
                    "is_correct": "0",
                    "correct_confidence": "0",
                    "last_correct_license_number": "",
                    "last_correct_name": "",
                    "last_correct_time": "",
                    "remark": "",
                    "third_prestore_amount": "0",
                    "third_dedution_amount": "0",
                    "third_prestore_origin": "0",
                    "amount_received": "0",
                    "amount_discounted": "0",
                    "enter_channel_name": "180主入口a",
                    "leave_channel_name": "",
                    "enter_custom_vip_name": "",
                    "leave_custom_vip_name": "",
                    "abnormal_out_remark": "",
                    "abnormal_out_reason": "",
                    "car_last_report_time": "",
                    "enter_statistical_area": "0",
                    "leave_statistical_area": "",
                    "is_park_in": "1",
                    "is_park_out": "0",
                    "is_locked": "0",
                    "is_manual_match": "0",
                    "pay_report_status": "0",
                    "vip_settlement_type": "-1",
                    "enter_novip_code": "1",
                    "enter_novip_remark": "",
                    "leave_novip_code": "1",
                    "leave_novip_remark": "",
                    "leave_correct_car_license_number": "",
                    "payment_mode_remark": "",
                    "pay_origin_remark": "VEMS",
                    "arrear_mark": "0",
                    "abnormal_in_reason": "",
                    "voucher_in_list": "",
                    "voucher_out_list": "",
                    "park_record_number": "",
                    "open_gate_type": "0",
                    "open_gate_time": "245",
                    "in_drivepos_picid": "",
                    "out_drivepos_picid": "",
                    "self_in_code": "",
                    "self_in_user_uniqcode": "",
                    "self_out_code": "",
                    "self_out_user_uniqcode": "",
                    "in_etc_car_code": "",
                    "in_etc_code": "",
                    "in_etc_reliable": "0",
                    "out_etc_car_code": "",
                    "out_etc_code": "",
                    "out_etc_reliable": "0",
                    "pay_bill_code": "",
                    "vip_car_rn": "",
                    "print_paper_invoice_flag": "0"
                }]
            }
        }
        data_json = json.dumps(payload)
        r = requests.post(urlpath,data = data_json)
        r.encoding = "utf-8"
        result = r.json()
        # print(result)
        if result['biz_content']['msg'] == "ok":
            log.info("【{}】车辆进场成功...".format(self.carNum))
        else:
	        log.error("【{}】车辆进场失败，原因:{}".format(self.carNum,result['biz_content']['msg']))

    """获取中央收费人员的token"""
    def get_center_people_token(self):
        path = "/vems/cxfService/centralPrice/loginCentralPrice"
        urlpath = self.url + path
        payload = {
            "username": "wx中央",
            "password": "E10ADC3949BA59ABBE56E057F20F883E",
            "devicetype": 1
        }
        data_json = json.dumps(payload)
        r = requests.post(urlpath,data =data_json)
        r.encoding ="utf-8"
        result = r.json()
        return result['usernameToken']


    """查询车辆的CarSeq"""
    def serch_car(self):
        path = "/vems/cxfService/centralPrice/searchCars"
        urlpath = self.url + path
        payload = {
            "licenseOrCardNum" : "%s" %self.carNum,
            "carType" : "场内车辆",
            "pageSeq" : "1",
            "pageSize" : "10",
            "usernameToken" : "%s"%self.usernameToken
        }
        data_json = json.dumps(payload)
        r = requests.post(urlpath, data=data_json)
        r.encoding = "utf-8"
        result = r.json()
        return result['data'][0]['realTimeCarSeq']

    """查询车辆的费用"""
    def check_car_charge(self):
        self.realTimeCarSeq = self.serch_car()
        path = "/vems/cxfService/centralPrice/checkFee"
        urlpath = self.url + path
        payload = {
            "carSeq" : "%s" %self.realTimeCarSeq,
            "usernameToken" : "%s" %self.usernameToken
        }
        data_json = json.dumps(payload)
        r = requests.post(urlpath, data =data_json)
        r.encoding = "utf-8"
        result = r.json()
        dic_car_message = dict()
        dic_car_message.update(basicFee=result['data']['basicFee'])
        dic_car_message.update(stopTime=result['data']['stopTime'])
        dic_car_message.update(taxPay=result['data']['taxPay'])
        dic_car_message.update(chargingTime=result['data']['chargingTime'])
        return dic_car_message

    """车辆费用缴纳"""
    def pay_charge(self):
        dic = self.check_car_charge()
        self.stopTime = dic['stopTime']
        self.basicFee = dic['basicFee']
        self.taxPay = dic['taxPay']
        self.chargingTime = dic['chargingTime']
        time.sleep(0.5)
        path = "/vems/cxfService/centralPrice/chargeFee"
        urlpath = self.url + path
        payload = {
            "usernameToken" : "%s"%self.usernameToken,
            "carSeq" : "%s" %self.realTimeCarSeq,
            "sumTime" : "%s" % self.chargingTime,
            "parkingTime" : "%s" %self.stopTime,
            "carTypeId" : "1",
            "localCouponId" : "",
            "localCouponName" : "无优惠",
            "traderCouponSeq" : "",
            "autoCouponName" : "",
            "autoCouponCode" : "",
            "basicFee" : "%s" % self.basicFee,
            "discountAmount" : "0.00",
            "alreadyPay" : "0.00",
            "taxPay" : "%s" % self.taxPay,
            "account" : "wx中央",
            "isLineup" : "0",
            "isCanUse" : "0"
        }
        data_json = json.dumps(payload)
        r = requests.post(urlpath, data=data_json)
        r.encoding = "utf-8"
        result = r.json()
        log.info("【{}】车辆{}".format(self.carNum,result['message']))

    """车辆费用离场"""
    def car_run_outside(self):
        path = "/vems/cxfService/rest/gateWayInformation"
        urlpath = self.url + path
        payload ={
            "command": "REPORT_CAR_OUT_LIST",
            "message_id": "1348",
            "sign_type": "MD5",
            "device_id": "00000000000000000000001497149A42",
            "sign": "00000000000000000000000000000000",
            "charset": "utf-8",
            "timestamp": "20170420170612517",
            "biz_content": {
                "leave_info_list": [{
                    "parking_lot_seq": "1",
                    "parking_area_seq": "2",
                    "car_license_number": "%s" % self.carNum,
                    "confidence": "97",
                    "total_amount": "%s" %self.basicFee,
                    "discount_validate_value": "",
                    "discount_no": "",
                    "discount_name": "",
                    "amount_receivable": "%s" %self.basicFee,
                    "discount_amount": "0",
                    "actual_receivable": "%s" %self.basicFee,
                    "pay_status": "1",
                    "payment_mode": "1",
                    "pay_origin": "1",
                    "toll_collector_name": "lgc岗亭",
                    "toll_collector_time": "%s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                    "last_pay_time": "%s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                    "enter_car_license_number": "%s" % self.carNum,
                    "enter_car_card_number": "",
                    "enter_time": "%s" % self.enterTime,
                    "enter_vip_type": "1",
                    "enter_vip_ticket_seq": "",
                    "enter_channel": "1",
                    "enter_type": "1",
                    "enter_speed": "0",
                    "enter_car_license_color": "1",
                    "enter_car_color": "0",
                    "enter_car_logo": "0",
                    "enter_car_license_type": "0",
                    "enter_car_full_picture": "/picpath/2017/04/20/00000000000/1/car/1_1_96_20170420170516_Y6854.jpg",
                    "enter_car_license_picture": "/picpath/2017/04/20/00000000000/1/plate/1_1_96_20170420170516_Y6854_plate.jpg",
                    "enter_car_type": "1",
                    "enter_recognition_confidence": "96",
                    "in_operator_name": "System",
                    "in_operator_time": "%s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                    "leave_car_license_number": "%s" % self.carNum,
                    "leave_car_card_number": "",
                    "leave_time": "%s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                    "leave_channel": "2",
                    "leave_vip_type": "1",
                    "leave_vip_ticket_seq": "0",
                    "leave_type": "2",
                    "leave_speed": "0",
                    "leave_car_license_color": "0",
                    "leave_car_color": "0",
                    "leave_car_logo": "0",
                    "leave_car_license_type": "0",
                    "leave_car_full_picture": "/picpath/2017/04/20/00000000000/2/car/1_2_97_20170420170558_Y6854.jpg",
                    "leave_car_license_picture": "/picpath/2017/04/20/00000000000/2/plate/1_2_97_20170420170558_Y6854_plate.jpg",
                    "leave_car_type": "1",
                    "leave_recognition_confidence": "97",
                    "correct_type": "0",
                    "out_operator_name": "lgc岗亭",
                    "out_operator_time": "%s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                    "record_type": "1",
                    "is_correct": "0",
                    "correct_confidence": "0",
                    "last_correct_license_number": "",
                    "last_correct_name": "",
                    "last_correct_time": "",
                    "remark": "",
                    "third_prestore_amount": "0",
                    "third_dedution_amount": "0",
                    "third_prestore_origin": "0",
                    "amount_received": "0",
                    "amount_discounted": "0",
                    "enter_channel_name": "180主入口a",
                    "leave_channel_name": "181主出口b",
                    "enter_custom_vip_name": "",
                    "leave_custom_vip_name": "",
                    "abnormal_out_remark": "",
                    "abnormal_out_reason": "",
                    "car_last_report_time": "%s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                    "enter_statistical_area": "2,1",
                    "leave_statistical_area": "2,1",
                    "is_park_in": "1",
                    "is_park_out": "1",
                    "is_locked": "0",
                    "is_manual_match": "0",
                    "pay_report_status": "1",
                    "vip_settlement_type": "-1",
                    "enter_novip_code": "1",
                    "enter_novip_remark": "",
                    "leave_novip_code": "1",
                    "leave_novip_remark": "",
                    "leave_correct_car_license_number": "",
                    "payment_mode_remark": "",
                    "pay_origin_remark": "",
                    "arrear_mark": "0",
                    "abnormal_in_reason": "",
                    "settle_record_list": []
                }]
            }
        }
        data_json = json.dumps(payload)
        r = requests.post(urlpath, data=data_json)
        r.encoding = "utf-8"
        result_json = r.json()
        result = result_json['biz_content']['msg']
        if result == "ok":
            log.info("【{}】车辆离场成功...".format(self.carNum))
        else:
            log.error("【{}】车辆离场失败...原因：{}".format(self.carNum,result))


if __name__ == '__main__':
    a = ApiCase(carNum = "粤A99999")
    # a.car_run_inside()
    # a.pay_charge()
    a.car_run_outside()