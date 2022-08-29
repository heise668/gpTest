import requests
import sys
import re
import prettytable as pt
import datetime
import urllib.parse
from bs4 import BeautifulSoup


# 牛散股东查询

def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    reponse=requests.get(url,headers=headers)
    # print (reponse.text)

    soup=BeautifulSoup(reponse.text,'html.parser')
    print (soup.title.string)
    item=soup.find_all('table',class_='tb0td1')
    return item


def get_data(url,today):
    new_item=get_html(url)
    dict={}
    # print (new_item[1])

    gdlist=[]
    for item in new_item[1].find_all('tr'):
        td = item.find_all('td')
        # print (td)


        seq=td[0].get_text().strip()
        gpCode=td[1].get_text().strip()
        gpName=td[2].get_text().strip()
        gdType=td[6].get_text().strip()
        date = td[7].get_text().strip()
        name=td[8].get_text().strip()
        gdnum=td[9].get_text().strip()
        gdRatio=td[11].get_text().strip()
        change = td[13].get_text().strip()
        changeNum = td[14].get_text().strip()

        gdlist.append([seq,gpName,gpCode,gdType,date,name,gdnum,gdRatio,change,changeNum])


    # 十大流通股东
    for gd in gdlist:
        print (gd)

if __name__=="__main__":
    url = "http://cwzx.shdjt.com/cwcx.asp?gdmc="

    name='华远国际陆港集团有限公司'
    # print (urllib.parse.quote(name.encode('gb2312')))
    url=url+urllib.parse.quote(name.encode('gb2312'))
    today=str(datetime.date.today().year)
    get_data(url,today)