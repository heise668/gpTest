import requests
import sys
import re
import prettytable as pt
from bs4 import BeautifulSoup


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
    item=soup.find('table',class_='globalTable trHover')
    return item


def get_data(url):
    new_item=get_html(url)
    dict={}
    # print (new_item.find_all('td'))
    gdlist=[]
    for item in new_item.find_all('tr'):
        td=item.find_all('td')
        n0 = td[0].get_text().strip()
        n1 = td[1].get_text().strip()
        n2 = td[2].get_text().strip()
        n3 = td[3].get_text().strip()
        n4 = td[4].get_text().strip()
        n5 = td[5].get_text().strip()

        # print (n0,n1,n2,n3,n4,n5)
        gdlist.append([n0,n1,n2,n3,n4,n5])


    tb = pt.PrettyTable()
    tb.field_names = ["序号", "股东名称", "持股数(万股)", "占总股本比例(%)","变动类型", "变动数量(万股)"]
    for i in gdlist[1:]:
        tb.add_row(i)
    print(tb)


if __name__=="__main__":
    # url = "http://stock.quote.stockstar.com/share/circulate_300241.shtml"

    group = {'君正集团': '601216.SS','东旭光电': '000413.SZ','许继电气': '000400.SZ','友好集团':'600778.SS',
             '文投控股': '600715.SS','ST加加': '002650.SZ','深粮控股':'000019.SZ',
             '上海环境': '601200.SS', '海尔智家': '600690.SS', '瑞丰光电': '300241.SZ',
             '百联股份':'600827.SS', '国芳集团': '601086.SS','岭南控股':'000524.SZ'}

    code=group.get('ST加加').split('.')[0]

    url=f"http://stock.quote.stockstar.com/share/circulate_{code}.shtml"
    print (url)

    get_data(url)