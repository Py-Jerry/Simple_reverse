#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/9/15 10:02
# @Author  : Soin
# @File    : demo.py
# @Software: PyCharm
import requests

cookies = {
    'next': 'http%3A//forum.butian.net/btlogin%3FredirectPath%3Dhttps%3A//forum.butian.net/',
    'User-Center': 'ce41350c-e4f0-4418-80d1-c1152253f57c',
    'csrf_token': '1757905440##00673e9cde8732ff558b615a46b3797e26fe617e',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://user.skyeye.qianxin.com',
    'Pragma': 'no-cache',
    'Referer': 'https://user.skyeye.qianxin.com/user/sign-in?next=http://forum.butian.net/btlogin?redirectPath=https://forum.butian.net/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'next=http%3A//forum.butian.net/btlogin%3FredirectPath%3Dhttps%3A//forum.butian.net/; User-Center=ce41350c-e4f0-4418-80d1-c1152253f57c; csrf_token=1757905440##00673e9cde8732ff558b615a46b3797e26fe617e',
}

json_data = {
    'account': '12345678910',   # 这里直接明文
    'password': 'Tc/lPFEBgr19uuDw4iLqRw==',
    'geetest_challenge': '22f0d7855d95d0b4eff6c6b4d663824a6n',
    'geetest_validate': 'a4794cfba8ec351aa53c6244d8bc4d3a',
    'geetest_seccode': 'a4794cfba8ec351aa53c6244d8bc4d3a|jordan',
    'next': 'http://forum.butian.net/btlogin?redirectPath=https://forum.butian.net/',
    'custom_callback_params': {
        'redirectPath': 'https://forum.butian.net/',
    },
    'key_iv': 'Xym+d/YBVjQJEn/rPOV56DyOoeuJda6u+vfdZ03t22372jfmKVxAQ4ycFc9qGegghwavZOjlERZfQAxoG0F6282l/WqanNYg92mF3tszg7MD/ahg1Bv4t10gTYA0rn3NrVOX+jz6bQTsl4NziiUxSaZMKYFY6M4m/MRQVnwz98uGJQb62Tk3rEA39H2DIIuUkiYjNs2G1jXqC5pd8g3Bg/MQT+4Nmr++/UKt8PoW3662jLz++ELqg7zuKGqNdrBTBxoqaUHgedXhNpHohrvbg/S6VavC9vjQnxaP1cLOfW6fPyIHavra3z+zXJ5tRffcOXuQgKWePxsOPCTxGDub/A==',
    'csrf_token': '1757905440##00673e9cde8732ff558b615a46b3797e26fe617e',
}

response = requests.post('https://user.skyeye.qianxin.com/api/v1/sign-in', cookies=cookies, headers=headers, json=json_data)

