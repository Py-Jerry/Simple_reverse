#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/9/2 17:03
# @Author  : Soin
# @File    : demo.py
# @Software: PyCharm
import requests
import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5  # 使用与 JSEncrypt 兼容的填充模式


cookies = {
    'agentmembers': 'notSet',
    'mantis6894': 'cedd15eb1b774177a676a37237876f21@6894',
    'safedog-flow-item': '',
    'sessionId': '1756803865436',
    'Hm_lvt_86efc728d941baa56ce968a5ad7bae5f': '1756803867',
    'Hm_lpvt_86efc728d941baa56ce968a5ad7bae5f': '1756803867',
    'HMACCOUNT': 'C81530F83C68362B',
    '_bl_uid': 'aXm65fb72RIbnFngdvIn5j4iay5C',
    'wxLoginUrl': 'https%3A%2F%2Fk.wangxiao.cn%2Fuser%2F',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'EagleEye-SessionID': 'gamyCf442Rzb8RnO6vwd171qkIL6',
    'EagleEye-TraceID': '446907221756803885731100481d1d',
    'EagleEye-pAppName': 'ihuy5j2ab7@7cd9bc63da81d1d',
    'Origin': 'https://user.wangxiao.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://user.wangxiao.cn/login?url=https%3a%2f%2fk.wangxiao.cn%2fuser%2f',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sessionId': '1756803865436',
    'source': 'pc',
    'token': '',
    # 'Cookie': 'agentmembers=notSet; mantis6894=cedd15eb1b774177a676a37237876f21@6894; safedog-flow-item=; sessionId=1756803865436; Hm_lvt_86efc728d941baa56ce968a5ad7bae5f=1756803867; Hm_lpvt_86efc728d941baa56ce968a5ad7bae5f=1756803867; HMACCOUNT=C81530F83C68362B; _bl_uid=aXm65fb72RIbnFngdvIn5j4iay5C; wxLoginUrl=https%3A%2F%2Fk.wangxiao.cn%2Fuser%2F',
}

json_data = {
    'userName': '123456',
    'password': 'cw5oRaUBgMZCxdufc76DXF6/3WMv6DpyczVkaxJ6QRWtjL6mb+vHUPIo8mc8XMENVaYDKJBYekM/sPr2Hz+Ps3NSVcNu1o9SNlcHSH3Wi9YQooS911L//40fLl5+cuOxoRBILgqxPL+kF27oAgNJ4KHm4JPDSHO7oIPjvtey4rw=',
    'imageCaptchaCode': 'krrz',
}

response = requests.post('https://user.wangxiao.cn/apis//login/passwordLogin', cookies=cookies, headers=headers, json=json_data)

print(response.json())


def encrypt_password(password, public_key_str):
    """
    使用 RSA 公钥加密字符串
    :param password: 待加密的明文字符串
    :param public_key_str: RSA 公钥字符串（PEM 格式，不含头尾标识）
    :return: Base64 编码后的加密字符串
    """
    # 将字符串公钥规范为 PEM 格式
    # 确保公钥格式正确，这是解密成功的关键[6](@ref)
    public_key = '-----BEGIN PUBLIC KEY-----\n' + public_key_str + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(public_key)
    cipher = PKCS1_v1_5.new(rsakey)
    # 对数据进行加密并 Base64 编码
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()  # 返回字符串形式的密文

# 公钥
key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB'
# 待加密的数据
pwd = '123456'
timestamp = int(time.time() * 1000)
data_to_encrypt = pwd + '' + str(timestamp)
encrypted_password = encrypt_password(data_to_encrypt, key)
print(encrypted_password)