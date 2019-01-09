import re
from urllib import request

class Spider():

    url = 'https://www.douyu.com/g_wzry'
    root_pattern = '(<div class="mes">[\s\S]*?<p>)([\s\S]*?)(</p>[\s\S*?]</div>)'
    name_pattern = '<span class="dy-name ellipsis fl">([\s\S]*?)</span>'
    fr_pattern = '<span class="dy-num fr">([\s\S]*?)</span>'

    # 从目标网页读取内容
    # 方法前面加下划线，是私有方法的意思
    def _fetch_content(self):
        # 组装header 信息，模拟浏览器访问
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # 组装一个请求
        req = request.Request(url=Spider.url, headers = headers)
        # 访问
        r = request.urlopen(req)
        # 读取页面html的内容
        htmls = r.read()
        # byte 字节转字符串
        htmls = str(htmls, encoding='utf-8')
        # 返回
        return htmls

    # 使用正则进行Html 分析、提取
    def __analysis(self, htmls):
        # 
        root_html = re.findall(Spider.root_pattern, htmls)
        # 用列表来存储内容
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html[1])
            fr = re.findall(Spider.fr_pattern, html[1])
            anchor = {'name':name, 'number':fr}
            anchors.append(anchor)
            
        return anchors

    # 数据列表整理
    def __refine(self, anchors):
        l = lambda anchor:{
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
            }
        # map 和 lambda 的写法
        return map(l, anchors)

    # 排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    # 排序key
    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    # 展现
    def __show(self, anchors):
        # i = 0
        # for anchor in anchors:
        #     i = i+1
        #     print(str(i) + ' ' + anchor['name'] + '------' + anchor['number'])

        for rank in range(0, len(anchors)):
            print('rank ' + str(rank+1) 
                + ' : ' + anchors[rank]['name']
                + '   ' + anchors[rank]['number'])
    

    def go(self):
        htmls = self._fetch_content() # 访问网页
        anchors = self.__analysis(htmls) # 分析网页
        anchors = self.__refine(anchors) # 数据整理
        anchors = self.__sort(anchors) # 排序
        self.__show(anchors) # 展现
    

spider = Spider()
spider.go()