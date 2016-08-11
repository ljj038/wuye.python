## Pythong mysql 操作流程
![mysql](https://github.com/zhaoyingnan911/wuye.python/blob/master/images/python-mysql.png?raw=true)

## 开发时应注意
```php
	conn = MySQLdb.Connect(...)
    # 关闭自动提交
    conn.autocommit(False)
	try:
		cursor = conn.cursor()
		sql = '...'
		cursor.execute(sql)
		# 提交
		conn.comit()
	except MySQLdb.Error, e:
		# log
		conn.rollback()
```
## 对于事务的理解

* 原子性:事务中包括的诸多操作要么都做，要么都不做
	* A有一百元 B有一百元 A给B转账五十元(A账户减去50 B账户加上50) 这两要么都执行 要么都不执行
* 一致性:事务必须使数据库从一致性状态到另一个一致性状态
	* A给B转账之前 两个人一共200 转账之后两个人还是200
* 隔离性:一个事务的执行不能被其他的事务干扰(相对于多个事务同时执行)
	* A在B转100 同时又给 C转100 B和C都会加100 A只减去100 这种情况就是因为两个事务没有隔离造成的 隔离性就是确保这种情况不会发生
* 持久性:事务一但提交 它对数据库的改变就是永久性的
	* 事务执行成功后会永久性的保存在数据库中 不会丢失
