#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/25 11:52
# @Author  : Soin
# @File    : 立社采集.py
# @Software: PyCharm
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from loguru import logger
import sys
from threading import Thread
import time
import random
import requests
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import datetime
import os
# ------------------------- 日志输出到 Tkinter -------------------------
class TkinterLogger:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)
        self.text_widget.update_idletasks()

    def flush(self):
        pass

info_data_list = [
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
all_data = []


# 创建一个全局 session，带自动重试
def create_retry_session(retries=5, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504)):
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    return session


session = create_retry_session()

def inside_apply(areacode, region_name, area):
    """
    按地区抓取全部分页数据
    """
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': f'https://publicity.mr.mct.gov.cn/web/inside_apply/{areacode}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    }

    page = 1

    while True:
        params = {'page': str(page), 'pagesize': '20', 'areacode': str(areacode)}
        try:
            resp = session.get('https://publicity.mr.mct.gov.cn/web/data/inside_apply',
                               params=params, headers=headers, timeout=10)
            resp.raise_for_status()
            resp_data = resp.json().get('resp_data', {})
            data_list = resp_data.get('list', [])
            if not data_list:
                break  # 没数据就退出循环

            for d in data_list:
                all_data.append({
                    "地区名称": region_name,
                    "城市名称": area,
                    '旅游社名称': d['name'],
                    '原许可证编号': d['old_licence'],
                    '新许可证编号': d['new_licence'],
                    "出资人": d['shareholder_info'],
                    "法定代表人": d['corporation_name'],
                    '经营场所': d['address'],
                    '许可日期': d['approved_date'],
                })

            logger.info(f"✅ [{region_name} - {area}] 第{page}页 数据共{len(data_list)}条")
            page += 1
            time.sleep(random.uniform(0.3, 0.8))  # 随机等待防封
        except Exception as e:
            logger.error(f"❌ 请求失败 {region_name}-{area} 第{page}页: {e}")
            break

def inside_change(areacode, region_name, area):
    """
    按地区抓取全部分页数据
    """
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': f'https://publicity.mr.mct.gov.cn/web/inside_apply/{areacode}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    }
    page = 1
    while True:
        params = {'page': str(page), 'pagesize': '20', 'areacode': str(areacode)}
        try:
            resp = session.get('https://publicity.mr.mct.gov.cn/web/data/inside_change',
                               params=params, headers=headers, timeout=10)
            resp.raise_for_status()
            resp_data = resp.json().get('resp_data', {})
            data_list = resp_data.get('list', [])
            if not data_list:
                break  # 没数据就退出循环
            for d in data_list:
                all_data.append({
                    "地区名称": region_name,
                    "城市名称": area,
                    '旅游社名称(变更前)': d['old_name'],
                    "出资人(变更前)": d['old_shareholder_info'],
                    "法定代表人(变更前)": d['old_corporation_name'],
                    '经营场所(变更前)': d['old_address'],
                    '旅游社名称(变更后)': d['new_name'],
                    "出资人(变更后)": d['new_shareholder_info'],
                    "法定代表人(变更后)": d['new_corporation_name'],
                    '经营场所(变更后)': d['new_address'],
                    '变更日期': d['create_time'],
                })

            logger.info(f"✅ [{region_name} - {area}] 第{page}页 数据共{len(data_list)}条")
            page += 1
            time.sleep(random.uniform(0.3, 0.8))  # 随机等待防封
        except Exception as e:
            logger.error(f"❌ 请求失败 {region_name}-{area} 第{page}页: {e}")
            break


def get_inside_apply():
    logger.success("正在采集立社信息。。。。。")
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = []
        for info_data in info_data_list:
            region_name = info_data["name"]
            for info in info_data["sub"]:
                futures.append(
                    executor.submit(
                        inside_apply,
                        areacode=info["area_code"],
                        region_name=region_name,
                        area=info["area"],
                    )
                )
        for f in futures:
            f.result()

    # 1️⃣ 生成主 Excel 文件
    timestamp = datetime.datetime.now().strftime("%Y年%m月%d日%H时%M分%S秒")
    base_name = f"{timestamp}_立社信息.xlsx"
    pd.DataFrame(all_data).to_excel(base_name, index=False)
    logger.success(f"✅ 所有数据已保存到 {base_name}")

    # 2️⃣ 创建对应文件夹
    output_dir = os.path.splitext(base_name)[0]  # 去掉扩展名作为文件夹名
    os.makedirs(output_dir, exist_ok=True)

    # 3️⃣ 拆分 Excel 按城市保存
    df = pd.read_excel(base_name)
    grouped = df.groupby("城市名称")

    for city, city_df in grouped:
        city_file = os.path.join(output_dir, f"{city}.xlsx")
        city_df.to_excel(city_file, index=False)
        logger.info(f"📁 已保存城市文件: {city_file}")

    # 4️⃣ 删除原始总文件
    try:
        os.remove(base_name)
        logger.success(f"🗑️ 已删除原始汇总文件: {base_name}")
    except Exception as e:
        logger.error(f"⚠️ 删除原文件失败: {e}")

    # 5️⃣ 清空数据缓存
    all_data.clear()
    logger.success(f"🎉 数据处理完成！所有文件已保存在: {output_dir}")



def get_inside_change():
    logger.info("正在采集变更信息。。。。。")
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = []
        for info_data in info_data_list:
            region_name = info_data["name"]
            for info in info_data["sub"]:
                futures.append(
                    executor.submit(
                        inside_change,
                        areacode=info["area_code"],
                        region_name=region_name,
                        area=info["area"],
                    )
                )
        for f in futures:
            f.result()

    # 1️⃣ 保存总表
    timestamp = datetime.datetime.now().strftime("%Y年%m月%d日%H时%M分%S秒")
    base_name = f"{timestamp}_立社变更信息.xlsx"
    pd.DataFrame(all_data).to_excel(base_name, index=False)
    logger.success(f"✅ 所有变更数据已保存到 {base_name}")

    # 2️⃣ 创建文件夹（以文件名去掉后缀为名）
    output_dir = os.path.splitext(base_name)[0]
    os.makedirs(output_dir, exist_ok=True)

    # 3️⃣ 按城市名称拆分 Excel
    df = pd.read_excel(base_name)
    if "城市名称" not in df.columns:
        logger.warning("⚠️ 未找到 '城市名称' 列，无法拆分省份文件。")
    else:
        grouped = df.groupby("城市名称")
        for city, city_df in grouped:
            city_file = os.path.join(output_dir, f"{city}.xlsx")
            city_df.to_excel(city_file, index=False)
            logger.info(f"📁 已保存城市变更文件: {city_file}")

    # 4️⃣ 删除原始总文件
    try:
        os.remove(base_name)
        logger.success(f"🗑️ 已删除原始汇总文件: {base_name}")
    except Exception as e:
        logger.error(f"⚠️ 删除原文件失败: {e}")

    # 5️⃣ 清空缓存
    all_data.clear()
    logger.success(f"🎉 变更数据处理完成！所有文件已保存在: {output_dir}")
# ------------------------- Tkinter GUI -------------------------
def run_in_thread(target_func):
    t = Thread(target=target_func)
    t.daemon = True
    t.start()


def create_gui():
    root = tk.Tk()
    root.title("立社采集工具")
    root.geometry("700x500")

    # 按钮区域
    frame = tk.Frame(root)
    frame.pack(pady=10)

    btn_apply = tk.Button(
        frame, text="采集立社", width=20, height=2, command=lambda: run_in_thread(get_inside_apply)
    )
    btn_apply.grid(row=0, column=0, padx=10)

    btn_change = tk.Button(
        frame, text="采集变更", width=20, height=2, command=lambda: run_in_thread(get_inside_change)
    )
    btn_change.grid(row=0, column=1, padx=10)

    # 日志框
    log_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=85, height=25, font=("Consolas", 10))
    log_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # 把 loguru 输出重定向到日志框
    sys.stdout = TkinterLogger(log_box)
    sys.stderr = TkinterLogger(log_box)
    logger.remove()
    logger.add(sys.stdout, level="INFO")

    root.mainloop()


if __name__ == "__main__":
    create_gui()