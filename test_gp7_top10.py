import datetime

import requests
from bs4 import BeautifulSoup
from test_gpName import get_data as gp_search
from test_gp2 import get_html as get_price
# 十大股东
#http://stock.quote.stockstar.com/share/holdertop10_600153.shtml

#十大流通股东
#http://stock.quote.stockstar.com/share/circulate_600021.shtml

def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    reponse=requests.get(url,headers=headers)
    # print (reponse.text)

    soup=BeautifulSoup(reponse.text,'html.parser')
    print (soup.title.string)
    item=soup.find('table',class_='tb0td1')
    return item


def get_data(url,year):
    new_item=get_html(url)
    dict={}
    # print (new_item.find_all('td'))
    circulation = []
    holdertop=[]
    for item in new_item.find_all('tr'):
        td = item.find_all('td')

        seq=td[0].get_text().strip()
        gdType=td[6].get_text().strip()
        date = td[7].get_text().strip()
        name=td[8].get_text().strip()
        gdnum=td[9].get_text().strip()
        gdRatio=td[11].get_text().strip()
        change = td[13].get_text().strip()
        changeNum = td[14].get_text().strip()

        if gdType == '十大流通股东':
            circulation.append([seq, gdType, date, name, gdnum, gdRatio, change, changeNum])
        elif gdType == '十大股东':
            holdertop.append([seq, gdType, date, name, gdnum, gdRatio, change, changeNum])


    # 十大股东
    for gd in holdertop[0:10]:
        print (gd)

    # 十大流通股东
    for gd in circulation[0:20]:
        print (gd)


if __name__=="__main__":
    url = "http://cwzx.shdjt.com/gpdmgd.asp?gpdm="

    name="游族网络"
    gp=gp_search(name)
    print (get_price(gp.get(name)))

    code=gp.get(name).split('.')[0]

    url=url+code
    year=str(datetime.date.today().year)
    get_data(url,year)