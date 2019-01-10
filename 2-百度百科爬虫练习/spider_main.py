from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer
'''
爬虫入口类，调度程序
'''
class SpiderMain(object):

    def __init__(self):
        # 初始化url管理器
        self.urls = url_manager.UrlManager()
        # 初始化下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 初始化解析器
        self.parse = html_parser.HtmlParser()
        # 初始化输入器
        self.outputer = html_outputer.HtmlOutputer()

    # 爬虫调度方法
    def craw(self, root_url):
        count = 1
        # 1、将入口url 添加到url管理器中，开始循环处理
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 2、获得一个要爬取的url
                new_url = self.urls.get_new_url()
                print ('craw %d : %s' % (count, new_url))
                # 3、下载这个url的内容
                html_cont = self.downloader.download(new_url)
                # 4、解析下载的内容，并返回 和 新的爬取的url
                new_urls, new_data = self.parse.parse(new_url, html_cont)
                # 5、将新的url放入到url管理器中
                self.urls.add_new_urls(new_urls)
                # 6、将数据放入到输出器中
                self.outputer.collect_data(new_data)

                # 设定爬取的数量，跳出循环，终止爬取
                if count == 10:
                    break
                
                count = count + 1
            except:
                print('craw failed')
        # 7、格式化输入
        self.outputer.output_html()


if __name__ =='__main__':
    # 入口url
    root_url = "https://baike.baidu.com/item/Python/407313"
    # 启动爬虫
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)