
'''
URL 管理器
'''
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 向url管理器中添加一个url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 添加一组待爬取的urls
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #  判断是否有新的待爬取的url
    def has_new_url(self):
       return len(self.new_urls) != 0

    # 得到一个新的url，使用set 的pop 方法
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

