#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/9/12 11:14
# @Author  : Soin
# @File    : demo.py
# @Software: PyCharm
import requests

cookies = {
    'JSESSIONID': '69B780FCC2302699002A80728C05314F',
    'isXionganFlag': 'false',
    'language': 'zh_CN',
    'sid': '45455f1863614462a186e409363924f0',
    'cookiesession1': '678B28783E4FE68E020E0487775CEA73',
    'acw_tc': 'ac11000117576460307056290e8ffc741f01cf1af4930c802e10f088b407e7',
    '_gscu_422057653': '57646031dzkdzo76',
    '_gscbrs_422057653': '1',
    '_gcl_au': '1.1.1781253952.1757646032',
    'orderChannel': 'JPSS-YDXC',
    'acw_sc__v2': '68c38d6d095135843903c90750f83aba5aa73121',
    'WT.al_flight': 'WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(CKG)%3AWT.al_dstcity1(KHN)%3AWT.al_orgdate1(2025-09-19)',
    'ticketBoolingSearch': '%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E9%87%8D%E5%BA%86%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22CKG%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E5%8D%97%E6%98%8C%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22KHN%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222025-09-19%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D',
    '_gscs_422057653': '576460311ndada76|pv:7',
    'temp_zh': 'cou%3D2%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-20%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26cou%3D3%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-20%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26cou%3D4%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-20%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-19%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-19%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26',
    'ssxmod_itna': 'eqIx9DyDRGit=DIKYj2wDeqiKAQnDe0dGMB0DITq7=GFWDChB1irdCDxAKeqD8QD4ED+iZUxGXxg42xGkjDCeDh42f5DCGCdxmC35mmrwxy8ADbbYOT8KZ70jU8BA+CKikgCScg2qhG4h7iYDCPDEceGyeYDxxGTixDTDWeDGDD3Q4iTDieDjWgICFoDb=r5DlFTH4Da84i3a4PDR=xD0xD8K407vGoeDG5eqdmxeCajC8BjCjdDnrDvGWoD914DspuciWE67L=eGROnGlSrih3fDCKDj2rpDmWTM/4I+/8Y3nq1KEp4HP+Cme4QGLnGzl5smNqmwK7Gq+wiiD1CpNCP4Cjke46iK6DDA97YcbNK0GiySCHlIyd4xDvq8GgrnRea01jTPkGK22tlxiQ0DSrNYiDsGNFit4mV8GDD',
    'ssxmod_itna2': 'eqIx9DyDRGit=DIKYj2wDeqiKAQnDe0dGMB0DITq7=GFWDChB1irdCDxAKeqD8QD4ED+iZ4xDfii4EmOupd5CT5XsD5nL5hvChYD',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://b2c.csair.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=CKG&c2=KHN&d1=2025-09-19&at=1&ct=0&it=0&b1=CKG-CQW&b2=KHN',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'JSESSIONID=69B780FCC2302699002A80728C05314F; isXionganFlag=false; language=zh_CN; sid=45455f1863614462a186e409363924f0; cookiesession1=678B28783E4FE68E020E0487775CEA73; acw_tc=ac11000117576460307056290e8ffc741f01cf1af4930c802e10f088b407e7; _gscu_422057653=57646031dzkdzo76; _gscbrs_422057653=1; _gcl_au=1.1.1781253952.1757646032; orderChannel=JPSS-YDXC; acw_sc__v2=68c38d6d095135843903c90750f83aba5aa73121; WT.al_flight=WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(CKG)%3AWT.al_dstcity1(KHN)%3AWT.al_orgdate1(2025-09-19); ticketBoolingSearch=%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E9%87%8D%E5%BA%86%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22CKG%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E5%8D%97%E6%98%8C%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22KHN%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222025-09-19%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D; _gscs_422057653=576460311ndada76|pv:7; temp_zh=cou%3D2%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-20%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26cou%3D3%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-20%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26cou%3D4%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-20%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-19%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2025-09-19%3B%E9%87%8D%E5%BA%86-%E5%8D%97%E6%98%8C%3B1%2C0%2C0%3B00%3B%26; ssxmod_itna=eqIx9DyDRGit=DIKYj2wDeqiKAQnDe0dGMB0DITq7=GFWDChB1irdCDxAKeqD8QD4ED+iZUxGXxg42xGkjDCeDh42f5DCGCdxmC35mmrwxy8ADbbYOT8KZ70jU8BA+CKikgCScg2qhG4h7iYDCPDEceGyeYDxxGTixDTDWeDGDD3Q4iTDieDjWgICFoDb=r5DlFTH4Da84i3a4PDR=xD0xD8K407vGoeDG5eqdmxeCajC8BjCjdDnrDvGWoD914DspuciWE67L=eGROnGlSrih3fDCKDj2rpDmWTM/4I+/8Y3nq1KEp4HP+Cme4QGLnGzl5smNqmwK7Gq+wiiD1CpNCP4Cjke46iK6DDA97YcbNK0GiySCHlIyd4xDvq8GgrnRea01jTPkGK22tlxiQ0DSrNYiDsGNFit4mV8GDD; ssxmod_itna2=eqIx9DyDRGit=DIKYj2wDeqiKAQnDe0dGMB0DITq7=GFWDChB1irdCDxAKeqD8QD4ED+iZ4xDfii4EmOupd5CT5XsD5nL5hvChYD',
}

json_data = {
    'depCity': 'CKG',
    'arrCity': 'KHN',
    'flightDate': '20250919',
    'adultNum': '1',
    'childNum': '0',
    'infantNum': '0',
    'cabinOrder': '0',
    'airLine': 1,
    'flyType': 0,
    'international': '0',
    'action': '0',
    'segType': '1',
    'cache': 0,
    'preUrl': '',
    'tariffRules': [],
    'isMember': '',
    'language': 'zh',
    'businessType': 'COMMON',
    'isMultipass': 1,
}

response = requests.post('https://b2c.csair.com/portal/main/flight/direct/query',
                         cookies=cookies,
                         headers=headers, json=json_data)
print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"depCity":"CKG","arrCity":"KHN","flightDate":"20250919","adultNum":"1","childNum":"0","infantNum":"0","cabinOrder":"0","airLine":1,"flyType":0,"international":"0","action":"0","segType":"1","cache":0,"preUrl":"","tariffRules":[],"isMember":"","language":"zh","businessType":"COMMON","isMultipass":1}'
#response = requests.post('https://b2c.csair.com/portal/main/flight/direct/query', cookies=cookies, headers=headers, data=data)