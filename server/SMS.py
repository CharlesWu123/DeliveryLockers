#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import hashlib
import time


class SendCode:

    def send(self, account, pswd, mobile, msg, ts, state):
        url = 'http://139.196.108.241:8080' + {
            1: '/Api/HttpSendSMYzm.ashx',
            2: '/Api/HttpSendSMYx.ashx',
            3: '/Api/HttpSendSMVoice.ashx'
        }[state]
        if ts != "":
            m = hashlib.md5()
            strs = account + pswd + str(ts)
            m.update(strs.encode("utf8"))
            pswd = m.hexdigest()
        body = {"account": account, "pswd": pswd, "mobile": mobile, "msg": msg, "ts": str(ts)}

        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/x-www-form-urlencoded"
                       }

        response = requests.post(url, data=body, headers=header_dict)

        return json.loads(response.text)


def main(CAPTCHA, addr, phoneNum):
    # account 用户账号
    # pswd 必填参数。用户密码
    # mobile 必填参数。合法的手机号码
    # msg  必填参数。短信内容
    # ts  可选参数，时间戳，格式yyyyMMddHHmmss
    # state 必填参数   状态  1:验证码短信  2:营销短信  3:语音验证码
    send = SendCode()

    res = send.send('13240385731', '997420Wzc', phoneNum, '【快递柜】请凭取件码【{}】至{}快递柜取包裹！'.format(CAPTCHA, addr),
                    (int(time.time())), 1)
    print(res['result'])


if __name__ == '__main__':
    CAPTCHA = 123456
    addr = '潘家园松榆北路建业苑6层'
    phoneNum = 13240385731
    main(CAPTCHA, addr, phoneNum)
    print('发送成功')
