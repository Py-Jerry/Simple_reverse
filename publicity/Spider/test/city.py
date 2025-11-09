#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/5 23:39
# @Author  : Soin
# @File    : city.py
# @Software: PyCharm
# info_data_list = [
#             {
#                 "name": "华北",
#                 "sub": [
#                     {
#                         "area": "北京市",
#                         "area_code": "110000"
#                     },
#                     {
#                         "area": "天津市",
#                         "area_code": "120000"
#                     },
#                     {
#                         "area": "河北省",
#                         "area_code": "130000"
#                     },
#                     {
#                         "area": "山西省",
#                         "area_code": "140000"
#                     },
#                     {
#                         "area": "内蒙古自治区",
#                         "area_code": "150000"
#                     }
#                 ]
#             },
#             {
#                 "name": "东北",
#                 "sub": [
#                     {
#                         "area": "辽宁省",
#                         "area_code": "210000"
#                     },
#                     {
#                         "area": "吉林省",
#                         "area_code": "220000"
#                     },
#                     {
#                         "area": "黑龙江省",
#                         "area_code": "230000"
#                     }
#                 ]
#             },
#             {
#                 "name": "华东",
#                 "sub": [
#                     {
#                         "area": "上海市",
#                         "area_code": "310000"
#                     },
#                     {
#                         "area": "江苏省",
#                         "area_code": "320000"
#                     },
#                     {
#                         "area": "浙江省",
#                         "area_code": "330000"
#                     },
#                     {
#                         "area": "安徽省",
#                         "area_code": "340000"
#                     },
#                     {
#                         "area": "福建省",
#                         "area_code": "350000"
#                     },
#                     {
#                         "area": "江西省",
#                         "area_code": "360000"
#                     },
#                     {
#                         "area": "山东省",
#                         "area_code": "370000"
#                     }
#                 ]
#             },
#             {
#                 "name": "华中",
#                 "sub": [
#                     {
#                         "area": "河南省",
#                         "area_code": "410000"
#                     },
#                     {
#                         "area": "湖北省",
#                         "area_code": "420000"
#                     },
#                     {
#                         "area": "湖南省",
#                         "area_code": "430000"
#                     }
#                 ]
#             },
#             {
#                 "name": "华南",
#                 "sub": [
#                     {
#                         "area": "广东省",
#                         "area_code": "440000"
#                     },
#                     {
#                         "area": "海南省",
#                         "area_code": "460000"
#                     },
#                     {
#                         "area": "广西壮族自治区",
#                         "area_code": "450000"
#                     }
#                 ]
#             },
#             {
#                 "name": "西南",
#                 "sub": [
#                     {
#                         "area": "重庆市",
#                         "area_code": "500000"
#                     },
#                     {
#                         "area": "四川省",
#                         "area_code": "510000"
#                     },
#                     {
#                         "area": "贵州省",
#                         "area_code": "520000"
#                     },
#                     {
#                         "area": "云南省",
#                         "area_code": "530000"
#                     },
#                     {
#                         "area": "西藏自治区",
#                         "area_code": "540000"
#                     }
#                 ]
#             },
#             {
#                 "name": "西北",
#                 "sub": [
#                     {
#                         "area": "陕西省",
#                         "area_code": "610000"
#                     },
#                     {
#                         "area": "甘肃省",
#                         "area_code": "620000"
#                     },
#                     {
#                         "area": "青海省",
#                         "area_code": "630000"
#                     },
#                     {
#                         "area": "宁夏回族自治区",
#                         "area_code": "640000"
#                     },
#                     {
#                         "area": "新疆维吾尔自治区",
#                         "area_code": "650000"
#                     },
#                     {
#                         "area": "新疆生产建设兵团",
#                         "area_code": "660000"
#                     }
#                 ]
#             }
#         ]
# for data in info_data_list:
#     # print(data)
#     for s in data['sub']:
#         print(s['area'])
#

import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
