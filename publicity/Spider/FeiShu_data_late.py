#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/8 23:47
# @Author  : Soin
# @File    : FeiShu_data_late.py
# @Software: PyCharm
from tools import RetryRequest
import json


class FeiShuTools:
    def __init__(self):
        # 飞书应用凭证
        self.APP_ID = 'cli_a704bdef28fad01c'
        self.APP_SECRET = '4IWG9ba25MHmuoYHFPi03dtpCERwa642'
        self.requests = RetryRequest()
        self.FILE_TOKEN_listen = "YEOVsTBBRhRA9atZYAScq5xHnjd"

    # requests = RetryRequest()
    def get_access_token(self):
        """
        获取访问令牌。
        返回:
            str: 访问令牌。
        """
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        # 准备请求数据，包含应用的ID和密钥
        post_data = {"app_id": self.APP_ID, "app_secret": self.APP_SECRET}
        # 向飞书接口发送POST请求，获取访问令牌
        r = self.requests.post(url, data=post_data)
        # 从响应中提取租户访问令牌
        access_token = r.json()["tenant_access_token"]
        return access_token

    def read_data_by_sheet_id(self, range):
        """
        根据Sheet ID和范围读取数据。
        参数:
            spreadsheet_id (str): 表格ID。
            range (str): 数据范围。
            access_token (str, optional): 访问令牌。默认调用get_access_token()获取。
        返回:
            pd.DataFrame: 数据DataFrame。
        """
        url = f"https://open.feishu.cn/open-apis/sheet/v2/spreadsheets/{self.FILE_TOKEN_listen}/values/{range}"
        headers = {"Authorization": f"Bearer {self.get_access_token()}",
                   "Content-Type": "application/json; charset=utf-8",
                   }
        params = {
            'valueRenderOption': 'ToString',
            'dateTimeRenderOption': 'FormattedString'
        }
        response = self.requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            # 提取表格数据
            values = data.get('data', {}).get('valueRange', {}).get('values', [])
            info_list = []
            for value in values[1:]:
                info_data = {}
                if value[0] is not None:
                    info_data['old_name'] = value[0]
                if value[1] is not None:
                    info_data['old_shareholder_info'] = value[1]
                if value[2] is not None:
                    info_data['old_corporation_name'] = value[2]
                info_list.append(info_data)
            return info_list

    def sendTextmessage(self, content):
        """
            群机器人消息发送
        """
        robot_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/3846e7cb-2822-4070-b8b5-3feab0e51953'
        headers = {"Content-Type": "application/json; charset=utf-8"}
        payload_message = {
            "msg_type": "text",
            "content": {
                "text": content
            }
        }
        response = self.requests.post(url=robot_url, data=json.dumps(payload_message), headers=headers)  # 发送
        return response.json()

    def create_table(self, sheet_token, sheet_name):
        """
        创建一个子表，并返回创建状态
        :return:
        """
        url = f'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{sheet_token}/sheets_batch_update'  # 访问表格接口
        headers = {
            'Authorization': f'Bearer {self.get_access_token()}',  # 携带token去访问接口
            'Content-Type': 'application/json'
        }
        data = {
            "requests": [
                {
                    "addSheet": {  # 新建子表的参数为addSheet
                        "properties": {
                            "title": sheet_name,  # 子表内容
                            "index": 1
                        }
                    }
                }
            ]
        }

        response = self.requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            # 获取新建子表的ID
            sheet_id = response.json()['data']['replies'][0]['addSheet']['properties']['sheetId']
            self.add_header(sheet_token, sheet_id, sheet_name)
            return True
        else:
            # logger.error(f"子表创建失败: {response.status_code}, {response.text}")
            raise Exception("子表创建失败了")

    def add_header(self, sheet_token, sheet_id, sheet_name):
        """
        向指定子表添加表头
        :param sheet_id: 子表ID
        """
        url = f'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{sheet_token}/values_append'
        headers = {
            'Authorization': f'Bearer {self.get_access_token()}',
            'Content-Type': 'application/json'
        }
        if "境内社" in sheet_name:
            values = [
                "城市", '旅游社名称', '出资人', '法定代表人', '经营场所', "变更后", '旅游社名称', '出资人',
                '法定代表人 ',
                '经营场所', '变更日期'
            ]

        else:
            values = [
                '旅游社名称', '出资人', '法定代表人', '经营场所', "变更后", '旅游社名称', '出资人',
                '法定代表人 ',
                '经营场所', '变更日期'
            ]
        data = {
            "valueRange": {
                "range": f"{sheet_id}!A1:Z1",  # 表头写入
                "values": [
                    values  # 表头内容
                ]
            }
        }
        response = self.requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            raise Exception("表头添加失败")

    def send_data_in_xlsx(self, sheet_name, data: dict):
        """
            将数据写入到飞书云表格中
        """
        pass


if __name__ == '__main__':
    pass
# fst = FeiShuTools()
# # data = fst.read_data_by_sheet_id("mOr29g")
# # print(data)
# resp = fst.sendTextmessage("123456\n"
#                            "1212121")
# print(resp)
