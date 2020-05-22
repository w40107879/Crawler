# !/usr/bin/python
# coding:utf-8

import requests as rq
from bs4 import BeautifulSoup
import io
import re
from selenium import webdriver
import json
import codecs

url = "https://www.cwb.gov.tw/V8/C/W/week.html"
# 先安裝PhantomJS，並確定安裝路徑 (https://phantomjs.org/download.html)
# 這是使用selenium來自動啟動PhantomJS渲染頁面，這樣才取得到HTML
driver = webdriver.PhantomJS(
    executable_path=r'C:\Users\User\Desktop\side-project\phantomjs\bin\phantomjs.exe')
# get網址
driver.get(url)

# 解析頁面
soup = BeautifulSoup(driver.page_source, "lxml")

# 先宣告空陣列，等等放所有天氣資訊
finalList = []

 # 取得表格
for table in soup.select('table'): 
    #一周有7天
    for d in range(1, 8):

        #取得日期
        date = soup.select('thead')[0].select('span')[d].text

        # 取得所有縣市 共22個
        for tbodyCount in range(len(soup.select('tbody'))):  

            #取得城市
            city = table.select('a')[tbodyCount].find('span').text

            #白天
            day = ''

            #夜晚
            night = ''

            #第一天的時候
            if d == 1:
                #第1個城市的時候
                if tbodyCount == 0:
                    # 這邊是xpath寫法，如果想快速了解的話，先在安裝chrome擴充安裝selenium IDE ，直接啟動去取得xpath就知道了

                    # 這是取的第一個城市的第一個白天氣候
                    day = driver.find_element_by_xpath("//table[@id='table1']/tbody/tr/td/span/img").get_attribute("title") #取得img的title內容

                    # 這是取的第一個城市的第一個夜晚氣候
                    night = driver.find_element_by_xpath("//table[@id='table1']/tbody/tr[2]/td/span/img").get_attribute("title")
                #其餘2-22個城市
                else:
                    day = driver.find_element_by_xpath("//table[@id='table1']/tbody["+str(tbodyCount+1)+"]/tr/td/span/img").get_attribute("title")
                    night = driver.find_element_by_xpath("//table[@id='table1']/tbody["+str(tbodyCount+1)+"]/tr[2]/td/span/img").get_attribute("title")
            #其餘2-7天
            else:
                #概念同上
                if tbodyCount == 0:
                    day = driver.find_element_by_xpath("//table[@id='table1']/tbody/tr/td["+str(d)+"]/span/img").get_attribute("title")
                    night = driver.find_element_by_xpath("//table[@id='table1']/tbody/tr[2]/td["+str(d)+"]/span/img").get_attribute("title")
                else:
                    day = driver.find_element_by_xpath("//table[@id='table1']/tbody["+str(tbodyCount+1)+"]/tr/td["+str(d)+"]/span/img").get_attribute("title")
                    night = driver.find_element_by_xpath("//table[@id='table1']/tbody["+str(tbodyCount+1)+"]/tr[2]/td["+str(d)+"]/span/img").get_attribute("title")

            finalList.append({
                "city": city,
                "date": date,
                "day": day,
                "night": night
            })


# 參考來源:https://blog.csdn.net/u014431852/article/details/53058951
fp = codecs.open('WeatherList.txt', 'w', 'utf-8')
for item in finalList:
    fp.write(json.dumps(item,ensure_ascii=False))
fp.close()

