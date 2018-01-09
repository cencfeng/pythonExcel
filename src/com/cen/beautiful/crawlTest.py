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
f = open('D:/content22.txt','w',encoding ='utf-8')
i = 1
for li in contenttext:
    f.write(str(i)+'. ')
    i += 1
    for lj in range(0,len(li.get_text().strip()),100):
        f.write(li.get_text().strip()[lj:lj+100]+'\n')
        f.write('\n')
    #print('sssss')  
    #f.write(li.get_text().strip()+'\n\n')
f.close()
#tests = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
#for i in range(0,len(tests),10):
    #print(tests[i:i+10])

