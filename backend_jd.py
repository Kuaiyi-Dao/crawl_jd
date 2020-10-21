# -*- coding: utf-8 -*- 
# @Time : 2020/10/6 10:36 AM
# @Author : wd
# @File : backend_jd.py
# 爬取一个页面的后面30条数据
import time
import random
from utils import get_backend_url_content, get_data_from_html
from mysql import insert_jd_goods_data


def get_url_by_keyword(keyword, page):
    """
    根据关键词组合url
    :param keyword:
    :return:
    """
    origin_url = "https://search.jd.com/s_new.php?keyword=" + keyword + "&wq=电脑&page=" + str(page)
    return origin_url


def main():
    """
    主函数
    :return:
    """
    keywords = ['电脑', '手机', '鼠标', '键盘', '显示器']
    for keyword in keywords:
        for page in range(1, 20):
            page = 2 * page
            url = get_url_by_keyword(keyword, page)
            html = get_backend_url_content(url)
            if html is None:
                continue
            data = get_data_from_html(html)
            data = tuple(data)
            insert_jd_goods_data(data)
            time.sleep(random.randint(10, 30))


if __name__ == '__main__':
    main()
