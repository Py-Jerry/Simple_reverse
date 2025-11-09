#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/4 23:40
# @Author  : Soin
# @File    : scheduled_start.py
# @Software: PyCharm
from publicity.Spider.tools import redis_client

redis_client.set("scheduled_start", 1234567)