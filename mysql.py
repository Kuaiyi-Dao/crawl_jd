# -*- coding: utf-8 -*- 
# @Time : 2020/10/6 9:11 PM
# @Author : wd
# @File : mysql.py
import pymysql


def get_conn():
    """
    获取数据库连接句柄
    :return:
    """
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='ya3Er1ea6ho@hgh8',
        database='jd_data',
        charset='utf8',
        connect_timeout=60,
        cursorclass=pymysql.cursors.DictCursor)
    return conn


def insert_jd_goods_data(data):
    """
    插入产品数据
    :param data:
    :return:
    """
    sql = "INSERT INTO jd_goods (product_id, product_name, price, product_url, product_types, total_comment_number, " \
          "default_good_count, good_rate, video_count, good_count, after_count, general_count, poor_count) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.executemany(sql, data)
        conn.commit()
    except Exception as e:
        print('insert fail')
        conn.rollback()


def insert_jd_comments_data(data):
    """
    插入产品的评论数据
    :param data:
    :return:
    """
    sql = "INSERT INTO jd_comments (product_id, content, creation_time, user_image_url, score, reply_count," \
          "useful_vote_count, image_count, anonymous_flag, plus_available, images, product_color, product_size, " \
          "nickname, days, after_days) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.executemany(sql, data)
        conn.commit()
    except Exception as e:
        print('insert fail')
        conn.rollback()


def fetch_product_id():
    """
    获取产品ID
    :return:
    """
    sql = "SELECT product_id from jd_goods WHERE ID > 2;"
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print('fetch data fail')
