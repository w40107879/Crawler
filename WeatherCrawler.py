# !/usr/bin/python
# coding:utf-8

import requests as rq
from bs4 import BeautifulSoup
import io
import re
import time
from  selenium import webdriver
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
tStart = time.time()#計時開始
fp = io.open("marryData-List.txt", "ab+")
# second = sleeptime(0,0,10);
# i = 7



url = "https://www.cwb.gov.tw/V8/C/W/week.html"
driver = webdriver.PhantomJS(executable_path=r'C:\Users\User\Desktop\side-project\phantomjs\bin\phantomjs.exe')
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")

# print(soup)
i=1
finalList = []


while(i<=3):
    for table in soup.select('table'):
        final = {}
        for city in table.select('a'):
            
            final["city"] = city.text
            finalList.append(final["city"])
        for date in soup.select('thead')[0].select('span'):
            final["data"] = date.text
            finalList.append(final["data"])
            
        # for date in soup.select('thead').select('#day'+str(i)):
        
        #     print(date.select('span'))
        
    i = i + 1
    print(finalList)
# for panel in soup.findAll('div', {'class': 'panel'}):
    
    # for city in panel.select('table'):
    #     print(soup.select('table'))
    # for headersCounty in panel.findAll('li', {'class': 'right'}):
    #     for city in headersCounty.findAll('a', {'data-toggle': 'collapse'}):
    #         print(city.text)
    # for date in soup.findAll('span', {'class': 'daily'}):
    #     print(date.text)
    #     break

# for week in soup.findAll('li', {'class': 'date'}):
#     print(week)

# while (i<=33):
#     nextlink = "https://www.marry.com.tw/venue-shop-kwbt2004mmir0mmpg"+str(i)+"mm"
#     nl_response = rq.get(nextlink) # 用 requests 的 get 方法把網頁抓下來
#     soup = BeautifulSoup(nl_response.text, "lxml") # 指定 lxml 作為解析器

#     for url in soup.findAll('a', {'class': 'shop_name'}):
#         response = rq.get(url.get('href')) # 用 requests 的 get 方法把網頁抓下來
#         html_doc = response.text # text 屬性就是 html 檔案
#         soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
        
#         if soup.select('h1') != []:
#             company = soup.select('h1')[0].find('a').text
#             # 判斷是否有H1
#             if company != '' :
#                 print('名稱:',company)
#                 table = soup.findAll('table', {'class': 'hall'})
#                 if table != []:   
#                     thead = ",".join([p.text.strip() for p in soup.select('table')[0].findAll('thead')[0].findAll('th')]) 
#                     tbody = ",".join([p.text.strip() for p in soup.select('table')[0].findAll('tbody')[0].findAll('td')])    
#                     fp.write(company.encode('utf-8') + '?'.encode('utf-8'))  
#                     fp.write(thead.encode('utf-8')+ '?'.encode('utf-8')) 
#                     fp.write(tbody.encode('utf-8')+ '\n'.encode('utf-8')) 
                            
#                     time.sleep(sleeptime(0,1,0))
#                 else:
#                     fp.write(company.encode('utf-8') + '?'.encode('utf-8')+ '\n'.encode('utf-8'))
#                     time.sleep(sleeptime(0,1,0))
#             else:
#                 print('沒有名稱')
#     i = i + 1
# tEnd = time.time()#計時結束
fp.close()
# print ("It cost %f sec" % (tEnd - tStart))#會自動做近位

