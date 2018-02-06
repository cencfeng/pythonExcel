# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
from _io import open
from logging import exception
import time
class Crawqsbk:
    def __init__(self):
        self.i = 1
        self.contenttext = []
        self.subcontext = []
        self.crawl_url = 'https://www.qiushibaike.com/text/page/'
        self.sub_url = 'https://www.qiushibaike.com'
        
    def getHTML(self,url):  
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req = urllib.request.Request(url, headers=headers)  
        return urllib.request.urlopen(req)
    
    def getData(self):
        try:
            res = BeautifulSoup(self.getHTML(self.crawl_url+str(self.i)),'html.parser',from_encoding='utf-8')
            self.i += 1
            self.contenttext = res.find_all(name="a",attrs={"class":"contentHerf"})    
        except (ValueError):
            print (ValueError)
            return None
    def getSubData(self,suburl):
        try:
            subtxt = BeautifulSoup(self.getHTML(suburl),'html.parser',from_encoding='utf-8')
            self.subcontext = subtxt.find_all(name="div",attrs={"class":"content"})
        except (ValueError):
            print (ValueError)
            return None  
    def start(self):
        f = open('D:/crawlast.txt','w',encoding ='utf-8')
        ii = 1
        while self.i <=10:
            time.sleep(0.2)
            self.getData()
            for li in self.contenttext:
                f.write(str(ii)+'. ')
                ii += 1
                if 'contentForAll' in str(li):
                    suburl = self.sub_url+li.get('href')
                    time.sleep(0.2)
                    self.getSubData(suburl)         
                    for m in self.subcontext:
                        for lj in range(0,len(m.get_text().strip()),100):
                            f.write(m.get_text().strip()[lj:lj+100]+'\n')
                            f.write('\n')
                else:
                    for lj in range(0,len(li.get_text().strip()),100):
                        f.write(li.get_text().strip()[lj:lj+100]+'\n')
                        f.write('\n') 
        f.close()
craw = Crawqsbk()
craw.start()