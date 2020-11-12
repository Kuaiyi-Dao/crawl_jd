# 京东爬虫
```
# 服务器目录：/root/crawl_jd
# 1、进入虚拟环境
cd /root/crawl_jd
source venv/bin/activate
```

### 一、爬取商品数据
```
# 京东商品显示策略: 一个页面60个商品，分两次向后台请求，一次30个
# 爬取前面30个商品
nohup python front_jd.py > ./log/front_1.log 2>&1 &
# 爬取后面30个商品
nohup python backend_jd.py > ./log/backend_1.log 2>&1 &
```
1. 目前只爬取了('电脑', '手机', '鼠标', '键盘', '显示器') 5个商品
2. 默认只爬取了1-19页的数据，超过19页后存在其他商品(例如搜索电脑20中可能会出现键盘膜、网卡等)
3. 爬取过程中会存在失败的情况，但是比例很低

### 二、爬取评论
```
# 需要在把商品数据爬取完成后再爬取，因为爬取评论需要用到产品的product_id字段
nohup python comment.py > ./log/comment_1.log 2>&1 &
```

### 三、反爬虫
```
# 一个IP短时间内多次请求会请求失败

# 目前采用的方法
1、第一步: 爬取页面的前30个数据, 结束后执行第二步
2、第二步: 爬取页面的后30个数据
3、在请求后，睡眠10-30秒再请求
2、利用代理IP[速度太慢且不稳定，暂时放弃，后续如果需要可以使用付费的代理IP，效果可能会相对好一点]

# 后续措施
1、分布式爬取(比较简单，总体来说就是多个服务器一起爬)
```

### 四、数据表结构
```sql
create database jd_data;

DROP TABLE IF EXISTS `jd_goods`;
-- 产品表
CREATE TABLE `jd_goods` (
  `ID` int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键、递增',
  `product_id` varchar(50) COMMENT '产品ID',
  `product_name` text COMMENT '产品名称',
  `product_url` varchar(255) COMMENT '产品url',
  `product_types` varchar(255) COMMENT '产品类型[自营、本地仓...]',
  `price` float COMMENT '产品价格',
  `total_comment_number` int COMMENT '所有的评价数量',
  `default_good_count` int COMMENT '默认好评',
  `good_rate` int COMMENT '好评率 95表示95%',
  `video_count` int COMMENT '视频嗮单',
  `good_count` int COMMENT '好评',
  `after_count` int COMMENT '追评',
  `general_count` int COMMENT '中评',
  `poor_count` int COMMENT '差评'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `jd_comments`;
-- 评论表
CREATE TABLE `jd_comments` (
  `ID` int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键、递增',
  `product_id` varchar(50) COMMENT '产品ID',
  `content` text COMMENT '评论内容',
  `creation_time` datetime COMMENT '评论时间',
  `user_image_url` varchar(255) COMMENT '用户头像地址',
  `score` int COMMENT '评分[5分是满分]',
  `reply_count` int COMMENT '评论回复数量',
  `useful_vote_count` int COMMENT '评论赞同数量',
  `image_status` char(1) COMMENT '是否有图片[1表示有, 0表示没有]',
  `image_count` int COMMENT '评论中的图片数量',
  `anonymous_flag` char(1) COMMENT '是否匿名评论[0表示不是匿名，1表示是匿名]',
  `plus_available` int COMMENT '会员的京享值',
  `images` text COMMENT '评论中的图片链接，以分号分割',
  `product_color` text COMMENT '产品颜色或者类别',
  `product_size` text COMMENT '产品尺寸',
  `nickname` varchar(255) COMMENT '用户别名',
  `days` int COMMENT '猜测是收货后多少天评价的',
  `after_days` int COMMENT '具体不太清楚，大多数都是0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```


