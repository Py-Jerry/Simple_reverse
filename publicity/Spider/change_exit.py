#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/1 23:07
# @Author  : Soin
# @File    : change_exit.py
# @Software: PyCharm

""" 境外社数据采集 """
from tools import logger, RetryRequest, MongoTools
import json
import time
import threading
from FeiShu_data_late import FeiShuTools

requests = RetryRequest()


class PublicCity:
    def __init__(self):
        self.info_data_list = [
            {
                "name": "华北",
                "sub": [
                    {
                        "area": "北京市",
                        "area_code": "110000"
                    },
                    {
                        "area": "天津市",
                        "area_code": "120000"
                    },
                    {
                        "area": "河北省",
                        "area_code": "130000"
                    },
                    {
                        "area": "山西省",
                        "area_code": "140000"
                    },
                    {
                        "area": "内蒙古自治区",
                        "area_code": "150000"
                    }
                ]
            },
            {
                "name": "东北",
                "sub": [
                    {
                        "area": "辽宁省",
                        "area_code": "210000"
                    },
                    {
                        "area": "吉林省",
                        "area_code": "220000"
                    },
                    {
                        "area": "黑龙江省",
                        "area_code": "230000"
                    }
                ]
            },
            {
                "name": "华东",
                "sub": [
                    {
                        "area": "上海市",
                        "area_code": "310000"
                    },
                    {
                        "area": "江苏省",
                        "area_code": "320000"
                    },
                    {
                        "area": "浙江省",
                        "area_code": "330000"
                    },
                    {
                        "area": "安徽省",
                        "area_code": "340000"
                    },
                    {
                        "area": "福建省",
                        "area_code": "350000"
                    },
                    {
                        "area": "江西省",
                        "area_code": "360000"
                    },
                    {
                        "area": "山东省",
                        "area_code": "370000"
                    }
                ]
            },
            {
                "name": "华中",
                "sub": [
                    {
                        "area": "河南省",
                        "area_code": "410000"
                    },
                    {
                        "area": "湖北省",
                        "area_code": "420000"
                    },
                    {
                        "area": "湖南省",
                        "area_code": "430000"
                    }
                ]
            },
            {
                "name": "华南",
                "sub": [
                    {
                        "area": "广东省",
                        "area_code": "440000"
                    },
                    {
                        "area": "海南省",
                        "area_code": "460000"
                    },
                    {
                        "area": "广西壮族自治区",
                        "area_code": "450000"
                    }
                ]
            },
            {
                "name": "西南",
                "sub": [
                    {
                        "area": "重庆市",
                        "area_code": "500000"
                    },
                    {
                        "area": "四川省",
                        "area_code": "510000"
                    },
                    {
                        "area": "贵州省",
                        "area_code": "520000"
                    },
                    {
                        "area": "云南省",
                        "area_code": "530000"
                    },
                    {
                        "area": "西藏自治区",
                        "area_code": "540000"
                    }
                ]
            },
            {
                "name": "西北",
                "sub": [
                    {
                        "area": "陕西省",
                        "area_code": "610000"
                    },
                    {
                        "area": "甘肃省",
                        "area_code": "620000"
                    },
                    {
                        "area": "青海省",
                        "area_code": "630000"
                    },
                    {
                        "area": "宁夏回族自治区",
                        "area_code": "640000"
                    },
                    {
                        "area": "新疆维吾尔自治区",
                        "area_code": "650000"
                    },
                    {
                        "area": "新疆生产建设兵团",
                        "area_code": "660000"
                    }
                ]
            }
        ]
        mongo = MongoTools(db_="PublicCityData")
        self.db = mongo.db
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}
        # 新数据
        self.new_data = []
        # self.now_table_name = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.now_table_name = '2025-11-09 01:18:39'

    def process_response(self, response: dict, url: str, area="无"):
        """ 处理返回数据 """

        db_name = url.split("/")[-1]
        collection = self.db[db_name]
        resp_data = response.get('resp_data', {})
        data_list = resp_data.get('list', [])
        for d in data_list:
            if not collection.find_one(d):
                logger.success(f"数据不存在，存入数据:{d}")
                self.db[db_name + self.now_table_name].insert_one({
                    "area": area,
                    **d
                })
            else:
                logger.debug(f"数据已存在，不存入:{d}")
        return True if len(data_list) != 20 else False

    def change_exit(self, url, page=1):
        params = {
            'page': str(page),
            'pagesize': '20',
        }

        resp = requests.get(url=url, params=params,
                            headers=self.headers)
        return self.process_response(resp.json(), url)

    def get_exit(self):
        """ 境外社数据采集 """
        sheet = 'mOr29g'
        url = 'https://publicity.mr.mct.gov.cn/web/data/change_exit'
        page = 1
        while True:
            logger.success(f"==================== 当前正在采集境外社第{page}页 ====================")
            is_end_page = self.change_exit(page=page, url=url)
            if is_end_page:
                break
            page += 1
        # fst = FeiShuTools()
        # exit_info_data = fst.read_data_by_sheet_id(sheet)

    def inside_change(self, areacode, page, area, url):
        """
        按地区抓取全部分页数据
        """
        params = {'page': str(page), 'pagesize': '20', 'areacode': str(areacode)}
        resp = requests.get(url=url, params=params, headers=self.headers)
        return self.process_response(resp.json(), url, area=area)

    def get_inside(self):
        sheet = '6c63f2'
        url = 'https://publicity.mr.mct.gov.cn/web/data/inside_change'
        # for info_data in self.info_data_list:
        #     for info in info_data["sub"]:
        #         area = info["area"]
        #         areacode = info["area_code"]
        #         page = 1
        #         while True:
        #             logger.success(f"==================== 当前正在采集国内社:{area}第{page}页 ====================")
        #             is_end_page = self.inside_change(page=page, areacode=areacode, area=area, url=url)
        #             if is_end_page:
        #                 break
        #             page += 1
        self.check_new_data(
            sheet_id=sheet,
            url=url
        )
    def check_new_data(self, sheet_id, url):
        new_data_list = []
        db_name = url.split("/")[-1]
        collen = self.db[db_name]
        now_db_name = self.db[db_name + self.now_table_name]
        fst = FeiShuTools()
        info_data = fst.read_data_by_sheet_id(sheet_id)
        for info in info_data:
            for new_data in now_db_name.find(info):
                new_data_list.append(new_data)



        # 将now_db_name 里面的数据存储到collen 里，并删除now_db_name



if __name__ == '__main__':
    pc = PublicCity()
    # pc.get_exit()
    pc.get_inside()
