#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/9/4 10:39
# @Author  : Soin
# @File    : demo.py
# @Software: PyCharm
import requests
import time
import json
import hashlib


def enmd5(text):
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.poco.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.poco.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# param = {"start": 60, "length": 20, "works_category": "1", "time_point": }
# param = f'\\{"start":180,"length":20,"works_category":"1","time_point":{int(time.time())}\\}'
# print(json.dumps(param))
# print(type(json.dumps(param)))
# sign_code = enmd5("poco_"+param+"_app")
print(enmd5('123456'))
# print(sign_code)

# data = {
#     'req': json.dumps({"version":"1.1.0","app_name":"poco_photography_web","os_type":"weixin","is_enc":0,"env":"prod","ctime":int(time.time() * 1000),"param":param,"sign_code":sign_code}),
#     'host_port': 'https://www.poco.cn',
# }
# print(data.get('req'))
#
# response = requests.post('https://web-api.poco.cn/v1_1/rank/get_homepage_recommend_list', headers=headers, data=data)
