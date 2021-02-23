import requests
import sys
import re
import prettytable as pt
import datetime
import urllib.parse
from bs4 import BeautifulSoup


# 牛散列表

def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    reponse=requests.get(url,headers=headers)
    # print (reponse.text)
    reponse.encoding = 'gbk'
    soup=BeautifulSoup(reponse.text,'html.parser')

    print (soup.title.string)
    item=soup.find_all('td',class_='tdlefttop')
    return item


def get_data(url):
    new_item=get_html(url)
    nslist=[]
    # print (new_item)

    for item in new_item:
        ns=item.get_text().strip()
        nslist.append(ns.split('.')[1])

    return nslist


def get_list():
    list=['杭州阿里巴巴创业投资管理有限公司',]


if __name__=="__main__":
    url = "http://cwzx.shdjt.com/top500.asp"


    nslist=get_data(url)
    print (nslist)