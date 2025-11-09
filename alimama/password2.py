#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/9/12 10:21
# @Author  : Soin
# @File    : password2.py
# @Software: PyCharm
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5  # 或者使用 PKCS1_OAEP 更安全，但需与加密端一致
from Crypto import Random
import binascii

# 假设你从 c.config 中获取了以下值
# rsaModulus (模数 n) 是一个很长的十六进制字符串或大整数
# rsaExponent (指数 e) 是 10001 (十六进制), 对应十进制 65537

# 你的 c.config.rsaModulus 和 c.config.rsaExponent 应该来自服务器或配置
# 这里用 placeholder，你需要替换成实际的值
# 例如，modulus 可能是一个十六进制字符串："a1b2c3...d4e5f6" 或者一个非常大的整数
rsa_modulus_hex = 'd3bcef1f00424f3261c89323fa8cdfa12bbac400d9fe8bb627e8d27a44bd5d59dce559135d678a8143beb5b8d7056c4e1f89c4e1f152470625b7b41944a97f02da6f605a49a93ec6eb9cbaf2e7ac2b26a354ce69eb265953d2c29e395d6d8c1cdb688978551aa0f7521f290035fad381178da0bea8f9e6adce39020f513133fb'  # 替换为实际的模数字符串
rsa_exponent_hex = "10001"  # 通常指数就是 10001 (十六进制)

# 将十六进制字符串转换为整数
modulus_int = int(rsa_modulus_hex, 16)
exponent_int = int(rsa_exponent_hex, 16)  # 转换后应为 65537

# 使用模数和指数构建 RSA 公钥对象
rsa_public_key = RSA.construct((modulus_int, exponent_int))

# 要加密的明文数据，对应 JavaScript 中的参数 e
plain_text = "123456"  # 替换为你要加密的内容

# 初始化加密器，使用 PKCS#1 v1.5 填充模式
# 注意：有些系统可能使用更安全的 PKCS#1 OAEP 填充模式，这需要与加密方保持一致
# 如果对方使用的是 OAEP，则这里应使用 PKCS1_OAEP.new(rsa_public_key)
cipher = PKCS1_v1_5.new(rsa_public_key)

# 加密操作
# RSA 加密要求明文为字节类型
plaintext_bytes = plain_text.encode('utf-8')
# 加密
encrypted_data = cipher.encrypt(plaintext_bytes)

# 通常，加密后的数据是二进制，为了方便传输，会进行 Base64 编码或转换为十六进制
encrypted_data_hex = binascii.hexlify(encrypted_data).decode('utf-8')
encrypted_data_b64 = binascii.b2a_base64(encrypted_data).decode('utf-8').strip()

print(f"明文: {plain_text}")
print(f"加密后的数据 (十六进制): {encrypted_data_hex}")
print(f"加密后的数据 (Base64): {encrypted_data_b64}")
'15f73328411a08fcfa40bfc796c61242bcc2d7fef81d8fe6b07dbb12a2caecd2f26f9b2aee5c94db6ba7d94379aa037898c74524f9806f2d3b7cb74c8b962e2f2eb8e5360876019faa730dde9216aa99149259a3f0fb7aebbb9acc302cb9698a797b128018c593f03983e0e3e9892b08fbbfef200ea8417b9e572ccf4481add9'
'0f18ce8c7949d38484cd6b19e3c4f5e0df8fdd6c88cf6ffaecd9dc1b8202b84c673a447c7246dc2cef9c09eb97312b978233add9ad04ce85f72a650e6cdd50ff5b12b2f17948768c18773689950aa672b0e6c7dc6c771c6389415ae1f7eb39a0b284645c4ab76434e140bc18aaa2bed27e81b40923ed0be217fc2f99c6c39d7e'