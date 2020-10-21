# -*- coding: utf-8 -*- 
# @Time : 2020/10/6 10:36 AM
# @Author : wd
# @File : comment.py
# 获取商品的评论
import time
import random
import json
from utils import get_front_url_content, get_data_from_html
from bs4 import BeautifulSoup
from mysql import fetch_product_id, insert_jd_comments_data


def get_review_url(product_id, page):
    """
    根据产品ID获取商品的评论数量, 这里的pagesize修改了也无效
    :param product_id: 产品ID
    :return:
    """
    origin_url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId" \
                 "=" + str(product_id) + "&score=0&sortType=5&page=" + str(page) + "&pageSize=10"
    return origin_url


def get_data_by_key_from_dict(key, _dict):
    """
    根据key从dict中获取数据
    :param key:
    :param _dict:
    :return:
    """
    if key in _dict:
        return _dict[key]
    else:
        return None


def main():
    """
    主函数
    :return:
    """
    product_ids = fetch_product_id()
    for item in product_ids:
        product_id = item['product_id']
        page = 0
        count = 0
        while True:
            result = []
            review_url = get_review_url(product_id, page)
            page = page + 1
            origin_data = get_front_url_content(review_url)
            if origin_data is None:
                continue
            if count > 5:
                break
            try:
                review_data = json.loads(origin_data[origin_data.index('(') + 1: -2])
            except:
                count = count + 1
                continue
            comments = review_data['comments']
            if len(comments) == 0:
                break
            for comment in comments:
                content = get_data_by_key_from_dict('content', comment)
                creation_time = get_data_by_key_from_dict('creationTime', comment)

                user_image_url = get_data_by_key_from_dict('userImageUrl', comment)
                score = get_data_by_key_from_dict('score', comment)
                reply_count = get_data_by_key_from_dict('replyCount', comment)
                useful_vote_count = get_data_by_key_from_dict('usefulVoteCount', comment)
                image_status = get_data_by_key_from_dict('imageStatus', comment)
                anonymous_flag = get_data_by_key_from_dict('anonymousFlag', comment)
                plus_available = get_data_by_key_from_dict('plusAvailable', comment)
                image_count = 0
                if image_status is not None and int(image_status) == 1:
                    image_count = get_data_by_key_from_dict('imageCount', comment)
                images = ''
                if int(image_count) > 0:
                    for image in comment['images']:
                        images = images + image['imgUrl'] + ';'
                product_color = get_data_by_key_from_dict('productColor', comment)
                product_size = get_data_by_key_from_dict('productSize', comment)
                nickname = get_data_by_key_from_dict('nickname', comment)
                days = get_data_by_key_from_dict('days', comment)
                after_days = get_data_by_key_from_dict('afterDays', comment)
                result.append((product_id, content, creation_time, user_image_url, score, reply_count, useful_vote_count,
                               image_count, anonymous_flag, plus_available, images, product_color,
                               product_size, nickname, days, after_days))
            result = tuple(result)
            insert_jd_comments_data(result)
            time.sleep(random.randint(10, 30))


if __name__ == '__main__':
    main()
