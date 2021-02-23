import requests
import sys
import re
import prettytable as pt
import datetime
import urllib.parse
from bs4 import BeautifulSoup


# 热点解读

def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    reponse=requests.get(url,headers=headers)
    print (reponse.text)

    soup=BeautifulSoup(reponse.text,'html.parser')
    print (soup.title.string)
    item=soup.find_all('table',class_='tb0td1')
    return item


def get_data(url):
    new_item=get_html(url)
    dict={}
    # print (new_item[1])

    gdlist=[]

if __name__=="__main__":
    url = "https://xuangubao.cn/top-gainer"

    get_data(url)