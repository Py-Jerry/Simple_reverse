#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/1 23:08
# @Author  : Soin
# @File    : __init__.py.py
# @Software: PyCharm
import requests
import time
from loguru import logger
from pymongo import MongoClient
import redis

redis_client = redis.Redis(
    host='localhost',
    db=1
)

class MongoTools:
    def __init__(self, db_):
        mongo_client = MongoClient()
        self.db = mongo_client[db_]



logger.add(
    "./logs/spider.log",
    rotation="00:00",  # 每天创建新日志文件
    retention="7 days",  # 保留 7 天
    encoding="utf-8",
    enqueue=True,  # 多线程安全
    backtrace=True,
    diagnose=False,
    level="INFO",
    format="[<green>{time:YYYY-MM-DD HH:mm:ss}</green>] "
           "[<level>{level}</level>] "
           "{message}"
)


class RetryRequest:
    def __init__(self, max_retries=5, timeout=10, backoff=1.5):
        """
        初始化请求类
        :param max_retries: 最大重试次数
        :param timeout: 超时时间（秒）
        :param backoff: 每次重试的退避倍数（例如 1.5 表示每次等待时间 ×1.5）
        """
        self.max_retries = max_retries
        self.timeout = timeout
        self.backoff = backoff
        self.session = requests.Session()

    def _request(self, method, url, **kwargs):
        """
        通用请求方法，包含重试逻辑
        """
        for attempt in range(1, self.max_retries + 1):
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    timeout=self.timeout,
                    **kwargs
                )
                # 如果状态码为 200~399，说明请求成功
                if 200 <= response.status_code < 400:
                    return response
                else:
                    logger.warning(f"[{method.upper()}] 请求失败：{response.status_code}，第 {attempt} 次重试...")
            except requests.RequestException as e:
                logger.warning(f"[{method.upper()}] 异常：{e}，第 {attempt} 次重试...")

            # 若非最后一次尝试则等待一段时间
            if attempt < self.max_retries:
                sleep_time = self.backoff ** (attempt - 1)
                time.sleep(sleep_time)

        logger.error(f"[{method.upper()}] 请求失败，已重试 {self.max_retries} 次。")
        return None

    def get(self, url, **kwargs):
        """
        GET 请求
        """
        return self._request("get", url, **kwargs)

    def post(self, url, **kwargs):
        """
        POST 请求
        """
        return self._request("post", url, **kwargs)

    def close(self):
        """关闭会话"""
        self.session.close()
