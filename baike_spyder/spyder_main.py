# coding=utf-8
from baike_spyder import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)  #将root url 放入url 管理器
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  #拿到一个url
                print('当前爬取第', count, '个url')
                html_cont = self.downloader.download(new_url) #下载页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)  #解析下载好的数据
                self.urls.add_new_urls(new_urls) #将获取的新的urls 放入url管理器
                self.outputer.collect_data(new_data)  #输出器来收集数据
                if count == 1:
                    break
                count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html()

if __name__=='__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'    #设置入口url
    obj_spider = SpiderMain()  #创建一个spider对象
    obj_spider.craw(root_url) #调用spider的craw方法来启动爬虫

