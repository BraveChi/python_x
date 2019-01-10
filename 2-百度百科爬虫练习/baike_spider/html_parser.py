from bs4 import BeautifulSoup
import re
from urllib import parse

class HtmlParser(object):
    # 从网页中遍历出新的链接
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/*"))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    

   # 找到要获取的内容
    def _get_new_data(self,page_url,soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>.....
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        #<div class="para" label-module="para">
        summary_node = soup.find('div',class_="lemma-summary").find('div',class_="para")
        res_data['summary'] = summary_node.get_text()

        return res_data

    # 解析并返回新的url 和 要取得的数据
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
