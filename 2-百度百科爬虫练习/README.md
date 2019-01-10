安装beautifulSoup

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

1、进入python3的Scripts目录下，使用pip 命令安装
    $ easy_install beautifulsoup4
    $ pip install beautifulsoup4

2、其他知识点：python -m pip install --upgrade pip  更新pip 安装工具

3、导入bs4
from bs4 import BeautifulSoup

目标地址：
https://baike.baidu.com/item/Python/407313


错误信息：
1、UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 62: illegal multibyte sequence

因为windows默认是GBK,需要在打开文件时指定编码：f = open("out.html","w",encoding='utf-8')