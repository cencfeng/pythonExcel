# coding=utf-8
from bs4 import BeautifulSoup
from xlwt.Workbook import Workbook
import urllib.request
import re
class Crawzhilian:
    def __init__(self):
        self.p = 1
        self.craw_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=java&isadv=0&sg=608d559fcd2d4519a5875099f573169d&p='

    def getHTML(self,url):  
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req = urllib.request.Request(url, headers=headers)  
        return urllib.request.urlopen(req)
    def getData(self):
        try:
            res = BeautifulSoup(self.getHTML(self.craw_url+str(self.p)),'html.parser',from_encoding='utf-8')
            self.p += 1
            d_gsmc = res.select("table.newlist > tr > td.gsmc")
            d_zwmc = res.select("table.newlist > tr > td.zwmc > div > a")
            d_zwyx = res.select("table.newlist > tr > td.zwyx")
            d_gzdd = res.select("table.newlist > tr > td.gzdd")
            d_gxsj = res.select("table.newlist > tr > td.gxsj > span")
            dzip = zip(d_gsmc,d_zwmc,d_zwyx,d_gzdd,d_gxsj)
            #print(type(dzip))
            return dzip
            #for gsmc,zwmc,zwyx,gzdd,gxsj in zip(d_gsmc,d_zwmc,d_zwyx,d_gzdd,d_gxsj):
                #print(gsmc.get_text(),zwmc.get_text(),zwyx.get_text()+gzdd.get_text()+gxsj.get_text()+zwmc.get('href'))
            #return zip(d_gsmc,d_zwmc,d_zwyx,d_gzdd,d_gxsj)
        except (ValueError):
            print (ValueError)
            return None
    '''def getSubdata(self,sub_url):
        res = BeautifulSoup(self.getHTML(sub_url),'html.parser',from_encoding='utf-8')
        zwms = res.select("div[class='terminalpage-main clearfix'] > div.tab-cont-box > div.tab-inner-cont")
        #zwms = res.find_all(re.compile(r'<!-- SWSStringCutStart -->(.*?)<!-- SWSStringCutEnd -->'))
        #print(zwms[0].get_text().replace('\n','').strip())
        return zwms[0].get_text().strip('\n').strip()'''
    def start(self):
        book = Workbook()
        sheet1 = book.add_sheet('Sheet1')
        i = 0
        while self.p <= 5:   
            zipd = self.getData()
            #print(type(list(zipd)))
            for gsmc,zwmc,zwyx,gzdd,gxsj in zipd:
                sheet1.write(i,0,gsmc.get_text())
                sheet1.write(i,1,zwmc.get_text())
                sheet1.write(i,2,zwyx.get_text())
                sheet1.write(i,3,gzdd.get_text())
                sheet1.write(i,4,gxsj.get_text())
                sheet1.write(i,5,zwmc.get('href'))
                #self.sub_url.append(zwmc.get('href'))
                #zwms = self.getSubdata(zwmc.get('href'))
                #sheet1.write(i,5,self.getSubdata(zwmc.get('href')))    #太慢
                i += 1
                #print(type(zwmc))
                #return
        sheet1.col(0).width = 256*40
        sheet1.col(1).width = 256*25
        sheet1.col(5).width = 256*60
        book.save('d:/gup/danwei.xls')
        #print(gsmc.get_text(),zwmc.get_text(),zwyx.get_text()+gzdd.get_text()+gxsj.get_text()+zwmc.get('href'))
craw = Crawzhilian()
craw.start()