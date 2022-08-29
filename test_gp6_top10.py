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

    group={'瑞丰光电':'300241.SZ','高新兴':'300098.SZ','北汽蓝谷': '600733.SS',
           '供销大集': '000564.SZ','海尔智家': '600690.SS','好想你': '002582.SZ','奥马电器': '002668.SZ','世纪华通': '002602.SZ',}
    group2={'方正证券': '601901.SS','上海物贸':'600822.SS','百联股份': '600827.SS','特锐德': '300001.SZ','杭钢股份':'600126.SS',
            '韵达股份': '002120.SZ','岭南控股':'000524.SZ','ST加加':'002650.SZ',
            '*ST力帆': '601777.SS','ST同洲':'002052.SZ','ST双环 ': '000707.SZ',}
    group3={'中文在线': '300364.SZ','跨境通 ': '002640.SZ','华金资本': '000532.SZ','华发股份': '600325.SS',}
    group_bak={'旋极信息': '300324.SZ','广电运通': '002152.SZ','中光学':'002189.SZ',
               '南天信息': '000948.SZ','神州信息': '000555.SZ',
               '明德生物': '002932.SZ','圣湘生物': '688289.SS','东方生物': '688298.SS',}


    group.update(group2)
    group.update(group3)
    # groups.update(group5)
    group.update(group_bak)
    code=group.get('四维图新').split('.')[0]

    url=f"http://stock.quote.stockstar.com/share/circulate_{code}.shtml"
    print (url)

    get_data(url)