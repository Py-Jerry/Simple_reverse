#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/13 11:13
# @Author  : Soin
# @File    : demo.py
# @Software: PyCharm
import requests
import hashlib
import time
import execjs

def requestId():
    with open("requestsId.js",'r',encoding='utf') as js_fp:
        js_code = js_fp.read()
        ctx = execjs.compile(js_code)
        return ctx.call('getUuid')

def timestamp():
    return int(time.time() * 1000)
def to_md5(text):
    """
        实现字符串->md5
    :param text:
    :return:
    """
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()
def post_api():
    url = "https://api.birdreport.cn/front/province/summary/chartProvinceYear"

    payload = {
        # "{"version":"CH4","year":"2025"}"
      'rlB/9hoADMHvM7eBEtW/GqsXS70rG8 gt2ajLVbG3Tmlw4MjrkeH4RVdHhm3Mda4v5IzxnZ7XYxE3OoMP5 Faq4VxDrwXxQHo8Vhd7YUp0xD3leNFewEsbkvoE OOlRzGaGmETesn5QtmaeyEcnBecy9deozji0Viq2cSxZUWGQ': "" # 前面的是RSA 后面默认空
    }

    headers = {
      'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
      'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
      'Cache-Control': "no-cache",
      'Origin': "https://www.birdreport.cn",
      'Pragma': "no-cache",
      'Referer': "https://www.birdreport.cn/",
      'Sec-Fetch-Dest': "empty",
      'Sec-Fetch-Mode': "cors",
      'Sec-Fetch-Site': "same-site",
      'requestId': "e2cdb5077ea8d741c2787817a009c7c0",  # ?
      'sec-ch-ua': "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
      'sec-ch-ua-mobile': "?0",
      'sec-ch-ua-platform': "\"Windows\"",
      'sign': "c65f1dafeefde7603d523e5fea2384c4",   # md5
      'timestamp': "1760324436000"  # 时间戳
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)
if __name__ == '__main__':
    # print(timestamp())
    print(requestId())