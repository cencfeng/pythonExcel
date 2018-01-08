# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
from _io import open
def getHTML(url):  
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}  
    req = urllib.request.Request(url, headers=headers)  
    return urllib.request.urlopen(req)
crawl_url = 'https://www.qiushibaike.com/text'
res = BeautifulSoup(getHTML(crawl_url),'html.parser',from_encoding='utf-8')
contenttext = res.find_all(name="div",attrs={"class":"content"})
f = open('D:/content.txt','w',encoding ='utf-8')
for i in contenttext:
    f.write(i.get_text())
f.close()


