import requests
import sys
import re

from bs4 import BeautifulSoup


# 7x24快讯页面


def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    reponse=requests.get(url,headers=headers)
    # print (reponse.text)

    soup=BeautifulSoup(reponse.text,'html.parser')
    print (soup.title.string)
    item=soup.find_all('li',class_='item_376tg')
    return item

def get_data(url):
    new_item=get_html(url)
    dict={}
   # print (new_item)
    for inform in new_item:
        item_0=inform.find('a', class_='link_xsH6g')
        print("快讯：",item_0.get_text().strip())
        item_1=inform.find_all('div', class_='stock stock-group-item-container')
        if len(item_1)>0:
            result = [span.get_text() for span in item_1]
            print("\t 关联:",result)

if __name__=="__main__":
    url = "https://xuangubao.cn/live/"  #7x24快讯
    get_data(url)