#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/9/5 10:18
# @Author  : Soin
# @File    : demo.py
# @Software: PyCharm
import requests
import hashlib
import random
import string
import execjs
import ddddocr
with open("bestwehotel.js", 'r', encoding='utf-8') as fp:
    js_code = fp.read()
    aes = execjs.compile(js_code)
def to_md5(text: str) -> str:
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()


def get_random(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits  # a-zA-Z0-9
    return ''.join(random.choice(chars) for _ in range(length))


def get_random_js() -> str:
    return aes.call('getRandom')

def get_verifyImageKey(mobile: str):
    dddd = ddddocr.DdddOcr()
    url = f"https://hotel.bestwehotel.com/api/safeverify/getImageVerify?mobile={mobile}&verifyImageKey={random.random()}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    with open('verify.png', 'wb') as f:
        f.write(response.content)
    res = dddd.classification(response.content)
    print(res)
    return res
# 示例
def login(username, password):
    t = get_random()
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://hotel.bestwehotel.com',
        'Pragma': 'no-cache',
        'Referer': 'https://hotel.bestwehotel.com/NewLogin/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'X-WE-SDK': '1.5.5',
        'rw': t,
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'groupTypeId': 2,
        'type': 1,
        'mobile': str(username),
        'password': aes.call('l', str(password)),  # 密码
        'rememberMe': False,
        'verifyCode': get_verifyImageKey(str(username)),  # 图像验证
        'TDFingerprint': 'sWPH517570382281GNWKzpUZX7',
        'blackBoxMd5': '143b8b69dee8bb27b1f99cbea79216c8',
        'did': '93b225fa9dda7cb43be84cfd47bc719a',
        'deviceInfo': {
            'fingerPrintJs': 'cfc746b91482f8c639bebf398ff296a9',
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'platform': 'Win32',
        },
        'sw': to_md5(t+str(username) +'cfc746b91482f8c639bebf398ff296a9'),
        'channelCode': 'CA00046',
    }

    print(json_data)

    response = requests.post('https://hotel.bestwehotel.com/api/member/login', headers=headers,
                             json=json_data)
    print(response.text)


if __name__ == '__main__':

    login('17770154462', 'whb031006')
