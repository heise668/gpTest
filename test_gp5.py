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
    for inform in new_item:

        #板块信息
        plates=inform.a.attrs['href']
        item_zhuti=inform.find('a', class_='search-zhuti-info')
        zhuti_info=item_zhuti.find('p', class_='search-zhuti-info-name')
        zhuti_desc=item_zhuti.find('div', class_='line-clamp search-zhuti-info-desc')


        banner=zhuti_info.get_text()
        desc=zhuti_desc.get_text().strip()

        if (zhuti_info is not None) & (zhuti_desc is not None):
            print ("板块：",banner,"板块描述：", desc)


        ##板块下的股票信息
        item_stock=inform.find('a', class_='search-zhuti-stock')
        list=[]
        if item_stock is not None:
            item_code=item_stock.attrs['href']
            stock_code=item_code.split('=')[1]
            list.append(stock_code)
            stock=item_stock.find('div', class_='search-zhuti-stock-name')
            stock_desc = item_stock.find('div', class_='line-clamp search-zhuti-stock-desc')
            if (stock is not None) & (stock_desc is not None):
                print("股票：",stock.get_text().strip(),"股票描述：", stock_desc.get_text().strip())

        plate=plates.split('/')
        id=plate[2]
        list=list+get_longtou(id)

        if (len(list) > 0):
            for stock in list:
                stock_item = get_html(stock)
                print(stock_item)
        print('————'*50)
        time.sleep(1);


def get_desc(stock):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url = "https://xuangubao.cn/search/"

    response = requests.get(url + stock + "?tab=0", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    new_item = soup.find_all('div', class_='search-zhuti-item')
    sublist = []
    for inform in new_item:

        # 板块信息
        plates = inform.a.attrs['href']
        item_zhuti = inform.find('a', class_='search-zhuti-info')
        zhuti_info = item_zhuti.find('p', class_='search-zhuti-info-name')
        zhuti_desc = item_zhuti.find('div', class_='line-clamp search-zhuti-info-desc')

        banner = zhuti_info.get_text()
        desc = zhuti_desc.get_text().strip()


        sub={}
        if (banner is not None) & (desc is not None):
            sub['主题']=banner
            sub['描述']=desc
            sublist.append(banner)

    return sublist


def get_longtou(id):
    http = urllib3.PoolManager()

    list =[]
    url="https://flash-api.xuangubao.cn/api/plate/data?fields=jinrilongtou,renqilongtou,hangyelongtou,core_avg_pcp,plate_name,plate_id&plates="

    r=requests.get(url+id)
    response = r.text
    resjson = json.loads(response)
    msg=resjson['data'].get(id)
    hangyelongtou=msg["hangyelongtou"]
    jinrilongtou=msg["jinrilongtou"]
    renqilongtou=msg["renqilongtou"]
    if(hangyelongtou is not None):
        list=list+hangyelongtou
    if (jinrilongtou is not None):
        list=list+jinrilongtou
    if (renqilongtou is not None):
        list=list+renqilongtou
    return list

if __name__=="__main__":

   # 被动元件，5G,AR/VR，无线耳机，智能穿戴
   # 知识产权，国产软件，网络安全，文化传媒
   # 区块链，电子发票，智慧物流，金融科技，比特币，电子货币
   # 环保，垃圾回收，黄河
   # 长三角一体化，黄河流域，雄安新区，自贸区，海南自贸，新疆，西藏，粤港澳
   # 国企改革，深圳国企，上海国企，地方国企，北京国企
   # 应急产业，华铁应急,养老产业，博彩，赛马，电竞
   # 密集调研
   # 新能源汽车，充电桩，特斯拉，蔚来汽车概念股，换电概念


   plate_group = ["供销大集"]
   for plate in plate_group:
        get_data(plate)