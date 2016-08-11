##wuye.python#
##Python 安装 MySQLdb
* [下载地址](https://pypi.python.org/pypi/MySQL-python) 选择合适的版本

```php
unzip MySQL-python-1.2.5.zip
cd MySQL-python-1.2.5/
# 可能会报错
python setup.py build
python setup.py install
# 至此就安装完成了
```
* 提示 [mysql_config: not found]

```php
sudo apt-get install libmysqlclient-dev
ls /usr/bin/mysql_config
```
* 提示 setuptools未安装

```php
wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz
tar -xzf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11/
python setup.py build
python setup.py install
```
* 提示 [error: Setup script exited with error: command 'gcc' failed with exit status 1]

```php
sudo apt-get install libmysqlclient-dev
```
