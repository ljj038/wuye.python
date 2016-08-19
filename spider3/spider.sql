CREATE TABLE `spider_article` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`username` varchar(20) NOT NULL DEFAULT '' COMMENT '发表用户的昵称',
	`groupname` varchar(50) NOT NULL DEFAULT '' COMMENT '网站的名称',
	`sourcename` varchar(50) NOT NULL DEFAULT '' COMMENT '原文的地址',
	`title` varchar(100) NOT NULL DEFAULT '' COMMENT '标题',
	`content` TEXT COMMENT '内容',
	`createtime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`),
	key `d_k` (`title`, `username`, `sourcename`, `groupname`, `createtime`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
