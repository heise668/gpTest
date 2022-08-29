import urllib3
import requests
import json
from bs4 import BeautifulSoup


def get_html(stock):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url = "https://xuangubao.cn/stock/"

    reponse=requests.get(url+stock,headers=headers)
    reponse.raise_for_status()

    soup=BeautifulSoup(reponse.text,'html.parser')
    stock_name=soup.title.string[0:4]

    item=soup.find_all('div',class_='zhibiao-item')


    dict={}
    dict.update({stock_name:stock})
    #print (new_item)
    for inform in item:
        item_0=inform.find('span',class_='zhibiao-item-label')
        item_1=inform.find('span',class_='zhibiao-item-text')
        #print (item_0.get_text(),item_1.get_text())
        dict.update({item_0.get_text():item_1.get_text()})
        #print (inform.get_text())

   # print (dict.items())

    return dict




#  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
requests.packages.urllib3.disable_warnings()
# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# 通过request()方法创建一个请求：
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

#7x24快讯api接口
url='https://api.xuangubao.cn/api/pc/msgs?subjids=9,10,162,723,35,469,821&limit=30'


#r = http.request('GET', url,  headers=headers)

r = requests.get(url , headers=headers)

#print(r.status) # 200
data=r.text
#reponse = json.dumps(r.data.decode(),ensure_ascii=False)
#print (reponse)

resjson=json.loads(data)
#print (resjson['NewMsgs'][0])
#print(type(resjson))

msg=resjson['NewMsgs']
print (len(msg))
for items in msg[0:]:
    title=items['Title']
    BkjInfoArr=items['BkjInfoArr']
    stock=items['Stocks']
    print (title,"\t=group=",BkjInfoArr)
    if stock is  not None:
        for stock_item in stock:
           #print(get_html(stock_item['Symbol']))
            dict_stock=get_html(stock_item['Symbol'])
            print ("\t相关股票:",stock_item['Name'],stock_item['Symbol'],"最新：",dict_stock["最新"],dict_stock["涨幅"])


