'''
下载网页的三种方法
'''
from urllib import request
import http.cookiejar
# 1
url = ''
response = request.urlopen(url)
response.read()

#2
data = {'name':'name','pw':'123'}
headers = {}
req = request.Request(url, data, headers=headers)
html = request.urlopen(req).read()

#3
# 创建一个cookie 容器
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)

# 设置代理
proxy = request.ProxyHandler({'http':'5.22.195.215:80'})
proxy_opener = request.build_opener(proxy)
request.install_opener(proxy_opener)

response = request.urlopen(url)
