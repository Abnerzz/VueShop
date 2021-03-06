"""
@author: Stephen
@file: yunpian.py
@time: 2018/4/20 0020 14:34
"""
import requests
import json

class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"


    def send_sms(self, code, mobile):
        params = {
            'api_key': self.api_key,
            'mobile': mobile,
            'text': "【幕学生鲜】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),
        }

        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        print(re_dict)



if __name__ == "__main__":
    yun_pian = YunPian("d6c4ddbf50ab36611d2f52041a0b949e")
    yun_pian.send_sms("1234", "18217568316")