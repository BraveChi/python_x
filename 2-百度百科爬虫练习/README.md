这个爬虫比上一个斗鱼人气值的要更好一些，用到了模块和分层，及beautifulSoup框架来代替正则表达式
------------------------------
业务流程图
![Image Text](https://github.com/BraveChi/python_x/blob/master/2-%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91%E7%88%AC%E8%99%AB%E7%BB%83%E4%B9%A0/%E7%AE%80%E5%8D%95%E7%88%AC%E8%99%AB%E6%9E%B6%E6%9E%84%E6%B5%81%E7%A8%8B%E5%9B%BE.jpg)

# 一、安装beautifulSoup

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

1、进入python3的Scripts目录下，使用pip 命令安装
    $ easy_install beautifulsoup4
    $ pip install beautifulsoup4

2、其他知识点：python -m pip install --upgrade pip  更新pip 安装工具

3、导入bs4
from bs4 import BeautifulSoup

# 目标地址：
https://baike.baidu.com/item/Python/407313


# 二、错误信息：
1、UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 62: illegal multibyte sequence

因为windows默认是GBK,需要在打开文件时指定编码：f = open("out.html","w",encoding='utf-8')
