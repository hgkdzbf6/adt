/*
Navicat MySQL Data Transfer

Source Server         : localhost 
Source Server Version : 50629
Source Host           : localhost:3306
Source Database       : think.admin

Target Server Type    : MYSQL
Target Server Version : 50629
File Encoding         : 65001

Date: 2017年9月29日08:42:12
*/

/*SET FOREIGEN_KEY_CHECKS=0;*/

-- ----------------------------
-- Table structure for system_auth
-- ----------------------------

DROP TABLE IF EXISTS `system_auth`;
CREATE TABLE `system_auth`(
	`id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
	`title` varchar(20) NOT NULL COMMENT '权限名称',
	`status` tinyint(1) unsigned DEFAULT '1' COMMENT '状态：（1，禁用；2，启用）',
	`sort` smallint(6) unsigned DEFAULT '0' COMMENT '排序权重',
	`desc` varchar(255) DEFAULT NULL COMMENT '备注说明',
	`create_by` bigint(11) unsigned DEFAULT '0' COMMENT '创建人',
	`create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
	PRIMARY KEY (`id`),
	UNIQUE KEY `index_system_auth_title` (`title`) USING BTREE,
	KEY `index_system_auth_status` (`status`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='系统权限表';

-- ----------------------------
-- Records of system_auth_node
-- ----------------------------

-- ----------------------------
-- Table structure for system_log
-- ----------------------------
DROP TABLE IF EXISTS `system_log`;
CREATE TABLE `system_log` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `ip` char(15) NOT NULL DEFAULT '' COMMENT '操作者IP地址',
  `node` char(200) NOT NULL DEFAULT '' COMMENT '当前操作节点',
  `username` varchar(32) NOT NULL DEFAULT '' COMMENT '操作人用户名',
  `action` varchar(200) NOT NULL DEFAULT '' COMMENT '操作行为',
  `content` text NOT NULL COMMENT '操作内容描述',
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='系统操作日志表';

-- ----------------------------
-- Records of system_log
-- ----------------------------

-- ----------------------------
-- Table structure for system_menu
-- ----------------------------
DROP TABLE IF EXISTS `system_menu`;
CREATE TABLE `system_menu` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `pid` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '父id',
  `title` varchar(100) NOT NULL DEFAULT '' COMMENT '名称',
  `node` varchar(200) NOT NULL DEFAULT '' COMMENT '节点代码',
  `icon` varchar(100) NOT NULL DEFAULT '' COMMENT '菜单图标',
  `url` varchar(400) NOT NULL DEFAULT '' COMMENT '链接',
  `params` varchar(500) DEFAULT '' COMMENT '链接参数',
  `target` varchar(20) NOT NULL DEFAULT '_self' COMMENT '链接打开方式',
  `sort` int(11) unsigned DEFAULT '0' COMMENT '菜单排序',
  `status` tinyint(1) unsigned NOT NULL DEFAULT '1' COMMENT '状态(0:禁用,1:启用)',
  `create_by` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '创建人',
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `index_system_menu_node` (`node`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8 COMMENT='系统菜单表';

-- ----------------------------
-- Table structure for system_user_simple
-- ----------------------------
DROP TABLE IF EXISTS `system_user_simple`;
CREATE TABLE `system_user_simple` (
	`id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
	`username` varchar(50) NOT NULL DEFAULT '' COMMENT '用户登录名',
	`password` char(100) NOT NULL DEFAULT '' COMMENT '用户登录密码',
	`phone` varchar(16) DEFAULT NULL COMMENT '电话号码',
	`email` varchar(50) DEFAULT NULL COMMENT '邮箱', 
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10001 DEFAULT CHARSET=utf8 COMMENT='简化系统用户表';


ALTER TABLE `adt_ecust`.`system_user_simple` 
ADD UNIQUE INDEX `username_UNIQUE` (`username` ASC),
ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);


-- ----------------------------
-- Records of system_user
-- ----------------------------
INSERT INTO `system_user_simple` VALUES ('10000', 'zbf', 'e028cb83e104a5814d539f77f66f0352', 
'13888888888','hgkdzbf6@qq.com');

-- ----------------------------
-- Table structure for system_user
-- ----------------------------
DROP TABLE IF EXISTS `system_user`;
CREATE TABLE `system_user` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL DEFAULT '' COMMENT '用户登录名',
  `password` char(32) NOT NULL DEFAULT '' COMMENT '用户登录密码',
  `qq` varchar(16) DEFAULT NULL COMMENT '联系QQ',
  `mail` varchar(32) DEFAULT NULL COMMENT '联系邮箱',
  `phone` varchar(16) DEFAULT NULL COMMENT '联系手机号',
  `desc` varchar(255) DEFAULT '' COMMENT '备注说明',
  `login_num` bigint(20) unsigned DEFAULT '0' COMMENT '登录次数',
  `login_at` datetime DEFAULT NULL,
  `status` tinyint(1) unsigned NOT NULL DEFAULT '1' COMMENT '状态(0:禁用,1:启用)',
  `authorize` varchar(255) DEFAULT NULL,
  `is_deleted` tinyint(1) unsigned DEFAULT '0' COMMENT '删除状态(1:删除,0:未删)',
  `create_by` bigint(20) unsigned DEFAULT NULL COMMENT '创建人',
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_system_user_username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10001 DEFAULT CHARSET=utf8 COMMENT='系统用户表';

-- ----------------------------
-- Records of system_user
-- ----------------------------
INSERT INTO `system_user` VALUES ('10000', 'zbf', 'e028cb83e104a5814d539f77f66f0352', 
'786100557', '786100557@Qq.com', '13888888855', 
'dfgsdfgsfd','27039', '2017-08-23 16:15:57',
'1', '301,302,303,304', '0', null, 
'2015-11-13 15:14:22');

-- ----------------------------
-- Table structure for system_user_charge
-- ----------------------------

DROP TABLE IF EXISTS `system_user_charge`;
CREATE TABLE `system_user_charge`(
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '充值记录id',
  `user_id` bigint(20) unsigned NOT NULL COMMENT '用户id',
  `consume` float unsigned DEFAULT 0,
  `charge` float unsigned DEFAULT 0,
  `overage` float DEFAULT 0 NOT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `desc` varchar(255) DEFAULT '' COMMENT '备注说明',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='用户充值消费记录';

-- ----------------------------
-- Records of system_user_charge
-- ----------------------------


-- ----------------------------
-- Table structure for system_common_sensitive_words
-- ----------------------------

DROP TABLE IF EXISTS `system_common_sensitive_words`;
CREATE TABLE `system_common_sensitive_words`(
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '敏感词id', 
  `word` varchar(30) NOT NULL COMMENT '敏感词',
  `advice_id` bigint(20) unsigned NOT NULL COMMENT '建议id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='敏感词表';

-- ----------------------------
-- Records of system_common_sensitive_words
-- ----------------------------

-- ----------------------------
-- Table structure for system_common_sensitive_words
-- ----------------------------
DROP TABLE IF EXISTS `system_common_sensitive_words`;
CREATE TABLE `system_common_sensitive_words`(
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '敏感词id', 
  `word` varchar(30) NOT NULL COMMENT '敏感词',
  `advice_id` bigint(20) unsigned NOT NULL COMMENT '建议id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='敏感词表';
ALTER TABLE `system_common_sensitive_words` ADD UNIQUE( `id`, `word`);

INSERT INTO `system_common_sensitive_words` VALUES (
	1,'这是一个测试',1
);

-- ----------------------------
-- Table structure for system_other_sensitive_words
-- ----------------------------
DROP TABLE IF EXISTS `system_other_sensitive_words`;
CREATE TABLE `system_other_sensitive_words`(
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '敏感词id', 
  `district_id` smallint(6) unsigned NOT NULL COMMENT '地区id',
  `category_id` smallint(6) unsigned NOT NULL COMMENT '范畴id',
  `word` varchar(30) NOT NULL COMMENT '敏感词',
  `advice_id` bigint(20) unsigned NOT NULL COMMENT '建议id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='敏感词表';
ALTER TABLE `system_other_sensitive_words` ADD UNIQUE( `id`, `word`);

INSERT INTO `system_other_sensitive_words` VALUES (
	1,1,1,'这是一个测试',1
);
-- ----------------------------
-- Table structure for system_category
-- ----------------------------
DROP TABLE IF EXISTS `system_category`;
CREATE TABLE  `system_category`(
  `id` smallint(6) unsigned NOT NULL COMMENT '范畴id',
  `category` varchar(20) NOT NULL COMMENT '范畴说明',
  PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='范畴表';


-- ----------------------------
-- Records of system_category
-- ----------------------------

-- INSERT INTO `system_category` VALUES('1','服装/鞋帽/饰品');
-- INSERT INTO `system_category` VALUES('2','电子电器（非医疗）');
-- INSERT INTO `system_category` VALUES('3','家具家装');
-- INSERT INTO `system_category` VALUES('4','母婴玩具');
-- INSERT INTO `system_category` VALUES('5','影视/文化/娱乐');
-- INSERT INTO `system_category` VALUES('6','食品（非保健食品）');
-- INSERT INTO `system_category` VALUES('7','保健食品');
-- INSERT INTO `system_category` VALUES('8','药品/医疗器械');
-- INSERT INTO `system_category` VALUES('9','医疗机构/医疗服务');
-- INSERT INTO `system_category` VALUES('10','化妆品（个人护理）');
-- INSERT INTO `system_category` VALUES('11','汽车');
-- INSERT INTO `system_category` VALUES('12','旅游');
-- INSERT INTO `system_category` VALUES('13','房地产');
-- INSERT INTO `system_category` VALUES('14','教育/培训');
-- INSERT INTO `system_category` VALUES('15','投资');
-- INSERT INTO `system_category` VALUES('16','法律/财税/咨询');
-- INSERT INTO `system_category` VALUES('17','信息服务');
-- INSERT INTO `system_category` VALUES('1000','其他');

-- ----------------------------
-- Table structure for system_district
-- ----------------------------
DROP TABLE IF EXISTS `system_district`;
CREATE TABLE  `system_district`(
  `id` smallint(6) unsigned NOT NULL COMMENT '地区id',
  `district` varchar(10) NOT NULL COMMENT '地区',
  PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='地区表';

-- ----------------------------
-- Records of system_district
-- ----------------------------
-- INSERT INTO `system_district` VALUES('1','全国');
-- INSERT INTO `system_district` VALUES('2','北京');
-- INSERT INTO `system_district` VALUES('3','上海');
-- INSERT INTO `system_district` VALUES('4','广东');
-- INSERT INTO `system_district` VALUES('5','江苏');
-- INSERT INTO `system_district` VALUES('6','浙江');
-- INSERT INTO `system_district` VALUES('7','河北');
-- INSERT INTO `system_district` VALUES('8','四川');
-- INSERT INTO `system_district` VALUES('9','福建');
-- INSERT INTO `system_district` VALUES('10','安徽');
-- INSERT INTO `system_district` VALUES('11','湖南');
-- INSERT INTO `system_district` VALUES('1000','其他');

-- ----------------------------
-- Table structure for system_clause
-- ----------------------------
DROP TABLE IF EXISTS `system_clause`;
CREATE TABLE  `system_clause`(
  `id` smallint(6) unsigned NOT NULL COMMENT '条文id',
  `clause` varchar(2000) NOT NULL COMMENT '地区',
  PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='条文表';


-- ----------------------------
-- Records of system_clause
-- ----------------------------




-- ----------------------------
-- Table structure for system_image
-- ----------------------------
DROP TABLE IF EXISTS `system_image`;
CREATE TABLE  `system_image`(
  `id` smallint(6) unsigned NOT NULL AUTO_INCREMENT COMMENT 'image id',
  `image` varchar(2000) NOT NULL COMMENT 'image data',
  PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='image info';

