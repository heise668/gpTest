import requests
import sys
import re
import json
from bs4 import BeautifulSoup


# 7x24快讯页面


def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    reponse=requests.get(url,headers=headers)
    # print (reponse.text)
    item=json.loads(reponse.text)

    return item

def get_data(url):
    new_item=get_html(url)
    data={}
   # print (new_item)
    QuotationCodeTable=new_item.get("QuotationCodeTable")
    data=QuotationCodeTable.get('Data')
    print (data[0])

if __name__=="__main__":

    gpname="机器人"

    url = "http://searchapi.eastmoney.com/api/suggest/get?" + \
          "input="+gpname+\
          "&type=14&token=D43BF722C8E33BDC906FB84D85E326E8&markettype=&mktnum=&jys=&classify=&securitytype=&status=&count=5&_=1646361422994"

    get_data(url)