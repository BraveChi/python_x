
'''
html输出器
'''
class HtmlOutputer(object):
    # 使用list 存储数据
    def __init__(self):
        self.datas = []

    # 将数据存入
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    # 格式化输出
    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            # fout.write('<td>%s</td>' % data['url'])
            fout.write("<td><a href='%s'>%s</a></td>" % (data['url'], data['title']))
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')

        fout.write('</html>')
        fout.close
