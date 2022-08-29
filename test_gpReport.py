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
    data=new_item.get("data")

    for item in data:
        SECURITY_CODE=item.get("SECURITY_CODE")
        SECURITY_NAME_ABBR=item.get("SECURITY_NAME_ABBR")
        REPORT_DATE_NAME=item.get("REPORT_DATE_NAME")
        TOTALOPERATEREVE=item.get("TOTALOPERATEREVE")
        TOTALOPERATEREVE=round(TOTALOPERATEREVE/100000000,3)

        print (SECURITY_NAME_ABBR,REPORT_DATE_NAME,TOTALOPERATEREVE)

if __name__=="__main__":
    url = "http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/ZYZBAjaxNew?type=1&code=SZ002932"
    get_data(url)