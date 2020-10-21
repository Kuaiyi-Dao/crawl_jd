# -*- coding: utf-8 -*- 
# @Time : 2020/10/6 10:29 AM
# @Author : wd
# @File : utils.py
import requests
import random
import json
from setting import USER_AGENTS, PROXIES
from bs4 import BeautifulSoup


def get_front_url_content(url):
    """
    获取url页面的内容
    :param url:
    :return:
    """
    origin_content = None
    request = requests.session()
    request.keep_alive = False
    rand_number = random.randint(0, len(USER_AGENTS) - 1)
    user_agent = USER_AGENTS[rand_number]
    rand_number = random.randint(0, len(PROXIES) - 1)
    ip_port = PROXIES[rand_number]['ip_port']
    headers = {
        'Connection': 'close',
        'user-agent': user_agent
    }
    proxies = {
        'http': 'http://' + ip_port + '/',
        'https': 'https://' + ip_port + '/'
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        origin_content = response.text
    return origin_content


def get_backend_url_content(url):
    """
    获取url页面的内容
    :param url:
    :return:
    """
    origin_content = None
    request = requests.session()
    request.keep_alive = False
    rand_number = random.randint(0, len(USER_AGENTS) - 1)
    user_agent = USER_AGENTS[rand_number]
    rand_number = random.randint(0, len(PROXIES) - 1)
    ip_port = PROXIES[rand_number]['ip_port']
    headers = {
        'Connection': 'close',
        'user-agent': user_agent,
        'referer': 'https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&wq=%E7%94%B5%E8%84%91&pvid=2bb21d9e57f7476290fc3d989f716ca9'
    }
    proxies = {
        'http': 'http://' + ip_port + '/',
        'https': 'https://' + ip_port + '/'
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        origin_content = response.text
    return origin_content


def get_review_number_url(product_id):
    """
    根据产品ID获取商品的评论数量
    :param product_id:
    :return:
    """
    origin_url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + str(product_id)
    return origin_url


def get_data_from_html(html):
    """
    从源码中提取数据
    :param html:
    :return:
    """
    soup = BeautifulSoup(html)
    goods_list = soup.find_all('li', class_='gl-item')
    data = []
    for goods in goods_list:
        price = goods.find('div', class_='p-price').i.get_text()  # 价格
        p_name = goods.find('div', class_='p-name')
        name = p_name.em.get_text().replace('\n', ' ')  # 商品名称
        url = p_name.a.get('href')  # 商品url
        types = goods.find('div', class_='p-icons').get_text().replace('\n', ' ')  # 商品类型[自营、本地仓...]
        product_id = url[url.index('com/') + 4: -5]
        review_number_url = get_review_number_url(product_id)
        if review_number_url is None:
            continue
        review_data = get_front_url_content(review_number_url)
        try:
            review_data = json.loads(review_data[review_data.index(':') + 1: -1])
        except:
            continue
        total_comment_number = review_data[0]['CommentCount']
        default_good_count = review_data[0]['DefaultGoodCount']
        good_rate = review_data[0]['GoodRateShow']
        video_count = review_data[0]['VideoCount']
        good_count = review_data[0]['GoodCount']
        after_count = review_data[0]['AfterCount']
        general_count = review_data[0]['GeneralCount']
        poor_count = review_data[0]['PoorCount']
        data.append((product_id, name, price, url, types, total_comment_number, default_good_count, good_rate,
                     video_count, good_count, after_count, general_count, poor_count))

    return data

