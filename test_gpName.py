import requests
import sys
import re
import urllib3
import json
import time, datetime
from bs4 import BeautifulSoup
from test_gp2 import get_html


# 搜索页面
def get_data(stock):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url = "https://xuangubao.cn/search/"

    reponse=requests.get(url+stock+"?tab=0",headers=headers)
    soup = BeautifulSoup(reponse.text, 'html.parser')

    new_item = soup.find_all('div', class_='search-zhuti-item')
    dict={}
    inform=new_item[0]
    #板块信息
    for item in new_item:
        plates=item.a.attrs['href']
        item_zhuti = item.find('a', class_='search-zhuti-info')
        zhuti_info = item_zhuti.find('p', class_='search-zhuti-info-name')
        zhuti_desc = item_zhuti.find('div', class_='line-clamp search-zhuti-info-desc')

        banner = zhuti_info.get_text()
        desc = zhuti_desc.get_text().strip()

        if (zhuti_info is not None) & (zhuti_desc is not None):
            print("板块：", banner, "板块描述：", desc)

    ##板块下的股票信息
    item_stock=inform.find('a', class_='search-zhuti-stock')
    if item_stock is not None:
        item_code=item_stock.attrs['href']
        stock_code=item_code.split('=')[1]

        stock=item_stock.find('div', class_='search-zhuti-stock-name')
        if (stock is not None) :
           stock_name=stock.get_text().strip()

    dict[stock_name]=stock_code
    return dict



if __name__=="__main__":

   plate_group = ["易联众"]
   for plate in plate_group:
        gp=get_data(plate)
        print(gp)