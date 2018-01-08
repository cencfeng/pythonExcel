# coding=utf-8
import re
from os.path import os
from xlwt.Workbook import Workbook
mypath = 'D:/alltxt/'
myfiles = os.listdir(mypath)
fileList = []
excellist = []
for f in myfiles:
        if(os.path.isfile(mypath + '/' + f)):
            if os.path.splitext(f)[1] == '.txt':
                fileList.append(f)
            # 添加文件          
for ff in fileList:
    f = open(mypath+ff,'r',encoding='utf-8')
#f = open('D:/alltxt/sndkPicklist_20180102170314_596_359508798.txt', 'r',encoding='utf-8')
    sourceInLines = f.readlines()  
    f.close()
    #d = {}
    for line in sourceInLines:
        lists = []
        temp1 = line.strip('\n')   
        temp2 = temp1.split('|')
        #matchDE = re.match( '^DE', temp1)
        #matchOP = re.match('^OP',temp1)
        #matchWO = re.match('^WO',temp1)        
        if re.match('^WO',temp1):
            #temp2 = temp1.split('|')
            wo = temp2[2]
            sdpn = temp2[3]
            descript = temp2[5]
            orderqty = int(temp2[6])
        if re.match('^OP',temp1):
            #temp2 = temp1.split('|')
            po = temp2[2]
            price = temp2[7]
            unit = temp2[9]       
        if re.match( '^DE', temp1):        
            if 'IC CPU' in temp1:
                iccpu = temp2[1]
                compqty = temp2[4]
                compn = '/'      
            else:
                iccpu = '/'
                compn = temp2[1]
                compqty = temp2[4]
            lists.append(sdpn)
            lists.append(descript)
            lists.append(wo)    
            lists.append(iccpu)
            lists.append(compn)
            lists.append(po)
            lists.append(orderqty)
            lists.append(compqty)
            lists.append(unit+price)
            excellist.append(lists)
    #d = {'SDPN':sdpn,'Descript':descript,'WO':wo,'iccpu':iccpu,'component':compn,'PO':po,'Orderqty':orderqty,'unitprice':unit+price+''}
    #lists.append(d)
#print(excellist)
book = Workbook()
sheet1 = book.add_sheet('Sheet1')
row0 = ['SD P/N','Description','WO#','IC CPU','Component','PO#','Order Qty','Comp qty','Unit price']
for i in range(len(row0)):
    sheet1.write(0,i,row0[i])
for i, li in enumerate(excellist):
    #print(li,'------')
    for j, lj in enumerate(li):      
        sheet1.write(i+1,j,lj)           
book.save('d:/alltxt/result.xls')
#print('生成excel,目录为:',mypath)