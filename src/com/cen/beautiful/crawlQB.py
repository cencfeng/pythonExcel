# coding=utf-8
from bs4 import BeautifulSoup
from urllib.request import *
from _io import open
class Spider:
    def __init__(self):
        self.page = 1
        # 记录访问的页码
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        # 伪装浏览器君
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        # 存储段子

    def get_stories(self):
        try:
            url = 'https://www.qiushibaike.com/text/page/' + str(self.page)
            request = Request(url, headers = self.headers)
            self.page += 1
            response = urlopen(request)
            content = response.read().decode("UTF-8").replace("<br/>", "\n")
            res = BeautifulSoup(content,'html.parser',from_encoding='utf-8')
            self.stories = res.find_all(name="div",attrs={"class":"content"})         
        except Exception as e:
            if hasattr(e, "reason"):
                print ("获取失败，错误原因", e.reason) 
                # 错误信息
                return None
    def start(self):
        f = open('D:/content.txt','w',encoding ='utf-8')
        i = 1
        while True:
            if self.page <= 10:
                self.get_stories()          
                for story in self.stories:
                    f.write(str(i)+'. ')
                    i += 1
                    for lj in range(0,len(story.get_text().strip()),100):
                        f.write(story.get_text().strip()[lj:lj+100]+'\n')
                        f.write('\n')
                    #f.write(story.get_text())'''
        f.close()
spider = Spider()
spider.start()