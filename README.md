##wuye.python
### 1. Python 相关模块的安装
#### Python 安装 MySQLdb 模块
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
* 安装pip
```python
sudo mkdir pip
cd pip/
ls
sudo wget https://bootstrap.pypa.io/get-pip.py
ls
sudo python get-pip.py
```

---

#### Python 安装 pandas 模块
```python
# To install pandas from source you need Cython,must install Cython fisrt
sudo pip install cython
cd /usr/local
sudo wget https://github.com/pydata/pandas/archive/master.zip
sudo unzip master.zip
sudo mv pandas-master/ pandas
cd pandas/
sudo python setup.py install
```

---

#### Python 安装 Imaging 模块

```python
cd /usr/local
# 安装所需要的库
# JPEG
wget  http://www.ijg.org/files/jpegsrc.v9b.tar.gz
tar -xzf jpegsrc.v9b.tar.gz
cd jpeg-9b/
./configure && make && make test && make install

# ZLIB
wget http://zlib.net/zlib-1.2.8.tar.gz
tar -xzf zlib-1.2.8.tar.gz
cd zlib-1.2.8/
./configure && make && make install

# FREETYPE2
wget http://download.savannah.gnu.org/releases/freetype/freetype-2.6.5.tar.gz
tar -xzf freetype-2.6.5.tar.gz
cd freetype-2.6.5/
./configure && make && make install

# LITTLECMS
tar -xzf lcms2-2.8.tar.gz 
cd lcms2-2.8/
./configure && make && make install

# 检查是否安装了支持的库
cd /usr/local/Imaging-1.1.7/

rm -rf /usr/local/lib/python2.7/dist-packages/PIL
rm -rf /usr/local/lib/python2.7/dist-packages/PIL.pth
python setup.py build
python setup.py install
```

---
#### Python 安装 redis 模块
* [下载地址](https://pypi.python.org/pypi/redis/2.10.5#downloads)

```python
	sudo wget https://pypi.python.org/packages/68/44/5efe9e98ad83ef5b742ce62a15bea609ed5a0d1caf35b79257ddb324031a/redis-2.10.5.tar.gz#md5=3b26c2b9703b4b56b30a1ad508e31083
	sudo tar -xzf redis-2.10.5.tar.gz
	cd redis-2.10.5/
	sudo python setup.py build
	sudo python setup.py install
```

---

#### Python 安装 pymongo 模块
* [下载地址](https://pypi.python.org/pypi/pymongo/3.3.0)

```python
    cd /usr/local
    sudo wget https://pypi.python.org/packages/31/63/5a7826bdee88db6d49ef1737a17de63cf6f50f8cb04f2a0339f048cb33b5/pymongo-3.3.0.tar.gz#md5=42cd12a5014fb7d3e1987ca04f5c651f
    sudo tar -xzf pymongo-3.3.0.tar.gz
    cd pymongo-3.3.0
    sudo python setup.py build
    sudo python setup.py install
```

---

#### Python 安装 beautifulsoup4 模块
* [下载地址](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/)

```python
	sudo wget https://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/beautifulsoup4-4.1.0.tar.gz
	sudo tar -xzf beautifulsoup4-4.1.0.tar.gz
	cd beautifulsoup4-4.1.0/
	sudo python setup.py build
	sudo python setup.py install
```

---

### 2. 其他
#### Pythong mysql 操作流程
![mysql](https://github.com/zhaoyingnan911/wuye.python/blob/master/images/python-mysql.png?raw=true)

---

#### Python mysql 开发时应注意
```python
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

---

#### 对于事务的理解
```python
* 原子性:事务中包括的诸多操作要么都做，要么都不做
	* A有一百元 B有一百元 A给B转账五十元(A账户减去50 B账户加上50) 这两要么都执行 要么都不执行
* 一致性:事务必须使数据库从一致性状态到另一个一致性状态
	* A给B转账之前 两个人一共200 转账之后两个人还是200
* 隔离性:一个事务的执行不能被其他的事务干扰(相对于多个事务同时执行)
	* A在B转100 同时又给 C转100 B和C都会加100 A只减去100 这种情况就是因为两个事务没有隔离造成的 隔离性就是确保这种情况不会发生
* 持久性:事务一但提交 它对数据库的改变就是永久性的
	* 事务执行成功后会永久性的保存在数据库中 不会丢失
```

---

#### matchObj.groups(), matchOb.lastGroupName 和 matchObj.group(group1[,group2,...]) 使用
```python                                                              
# 当使用分组时 match 为一个元组 此时用 groups() 获取该元组 用group() 获取单个或多个指定的元组
# 当未使用分组时 match 为一个字符串 可以使用 group() 直接获取该匹配                          
pattern = re.compile(r'(\d)(\d)(\d)(?P<lastGroupName>\d)')                                   
match = pattern.match('1982')                                                                
print(match.groups())                                                                        
print(match.group(1, 3))  # 若结果为元组时 元组的第一个元素为被操作的字符串                  
print(match.lastgroup)  # 获取最后一个组的组名                                               
```

---

#### matchObj.groupdict() 使用  
```python                                                          
match = re.match(r'(?P<firstName>\w+) (?P<lastName>\w+)', 'zhaoyingnan zhaoyn')
print(match.groupdict())  # {'lastName': 'zhaoyn', 'firstName': 'zhaoyingnan'}
```

---

#### matchObj.search(string[, startpos[, endpos]]) 使用
```python
# startpos 和 endpos 代表从 string 的 startpos 索引开始匹配 到 endpos 结束 索引从0开始
pattern = re.compile(r'dog', re.I)  # 创建一个pattern对象
match = pattern.search('adogs', 1, 4)  # 从 adogs 的索引为1的位置开始匹配 到索引位置为4时结束匹配
print(match.group(0))  # dog      
print(match.start())  # 1 返回开始位置的索引值     
print(match.end())  # 4 返回结束位置的索引值            
print(match.span())  # (1, 4) 返回开始和结束位置的索引值的元组
```

---

#### matchObj.sub(pattern, replace or function, str, count=0, flags=0) 使用
```python
# sub(pattern, replace or function, str, count=0, flags=0) 字符串替换 返回替换后的字符串
str1 = 'Baked Beans And Spam'                 
print(re.sub(r'\sand\s', ' & ', str1, flags=re.I))  # Baked Beans & Spam                                                                                     
print(re.sub(r'\d+', add, '1 2 3'))  # 2 4 6
```

---

### 3. IDE 相关
#### PyCharm 安装 ideaVim 插件
```python
操作步骤：File->Settings->Plugins->Browse repositories->输入 ideaVim -> install->重启 PyCharm
切换 vim：Tools->Vim Emulator(Ctrl+Alt+v)
```
---

#### PyCharm 主题模式的切换
```python
File->Settings->Appearance->Theme->选择想要的->重启
```