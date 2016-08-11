CREATE TABLE `zhs_account` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`acctid` int(11) NOT NULL DEFAULT '0',
	`money` int(11) NOT NULL DEFAULT '0',
	PRIMARY KEY (`id`),
	KEY `ix_fatherid` (`acctid`,`money`)
) ENGINE=InnoDB AUTO_INCREMENT=3275 DEFAULT CHARSET=utf8;
