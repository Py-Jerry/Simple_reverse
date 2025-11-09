#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/6 23:51
# @Author  : Soin
# @File    : autospider_incognito_per_page.py
# @Software: PyCharm

import re
import time
from DrissionPage import Chromium, ChromiumOptions

def extract_phone(text: str):
    """
    从文本中提取电话号码（例如 347-702-2746 或带/不带区号的美国格式）。
    返回匹配的列表，未找到返回空列表。
    """
    pattern = re.compile(r'(?:(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})')
    matches = pattern.findall(text)
    return matches or []


def spiders(yema, retry=3, headless=True):
    """
    为每一页新建一个无痕浏览器实例来抓取，然后关闭它。
    retry: 如果页面无结果或报错，重试次数（重新创建浏览器并再试）。
    headless: 是否以无头模式运行（True: 无头，False: 可见）
    """
    if retry < 0:
        print(f"⚠ 第 {yema} 页多次重试失败，已跳过。")
        return

    print(f"🌸 开始处理第 {yema} 页（剩余重试：{retry}）...")

    # 每次新建 ChromiumOptions 并开启 incognito
    co = ChromiumOptions()
    co.incognito(True)         # 无痕模式
    # co.headless(headless)      # 是否无头，按需要改为 False 观察浏览器
    browser = None
    page = None

    try:
        browser = Chromium(co)       # 启动一个新的 Chromium 实例（无痕）
        # 新建一个 tab / page（在无痕浏览器中）
        page = browser.new_tab()
        url = f'https://www.us168168.com/job?page={yema}'
        page.get(url)

        # 查找目标元素
        item_div = page.eles('xpath://div[@class="universal-list-module-item left universal-list-module-item"]')
        if not item_div:
            # 页面可能没加载出内容，关闭并重试（重新建浏览器）
            print(f"⚠ 第 {yema} 页未找到任何 item，准备重试（剩余 {retry-1} 次）...")
            # 先确保关闭资源，再递归重试
            try:
                if page:
                    page.close()
            except Exception:
                pass
            try:
                if browser:
                    browser.close()
            except Exception:
                pass
            try:
                if browser:
                    browser.quit()
            except Exception:
                pass
            time.sleep(0.8)
            return spiders(yema, retry - 1, headless=headless)

        # 处理每个 item，提取电话或写入 no_phone.txt
        for item in item_div:
            text = item.text.replace("\n", "")
            phones = extract_phone(text)
            if not phones:
                with open("no_phone.txt", "a", encoding="utf-8") as f:
                    f.write(text + "\n")
            else:
                with open("phone.txt", "a", encoding="utf-8") as f:
                    for p in phones:
                        f.write(p + "\n")

        print(f"✅ 第 {yema} 页处理完成，条目数：{len(item_div)}")

    except Exception as e:
        print(f"❌ 第 {yema} 页发生异常：{e}，准备重试（剩余 {retry-1} 次）")
        # 出错时关闭并重试
        try:
            if page:
                page.close()
        except Exception:
            pass
        try:
            if browser:
                browser.close()
        except Exception:
            pass
        try:
            if browser:
                browser.quit()
        except Exception:
            pass
        time.sleep(1)
        return spiders(yema, retry - 1, headless=headless)

    finally:
        # 最终确保资源被释放
        try:
            if page:
                page.close()
        except Exception:
            pass
        try:
            if browser:
                browser.close()
        except Exception:
            pass
        try:
            if browser:
                browser.quit()
        except Exception:
            pass
        # 短暂休眠，避免短时间内频繁创建浏览器导致系统压力过大
        time.sleep(0.4)


if __name__ == '__main__':
    # 从 1 到 628 页（含）
    for yema in range(1, 629):
        spiders(yema, retry=3, headless=True)
