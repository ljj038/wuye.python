##wuye.python#
### Python 安装 MySQLdb 模块
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

### Python 安装 pandas 模块
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

### Python 安装 Imaging 模块

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
