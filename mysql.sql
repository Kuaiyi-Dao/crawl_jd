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

