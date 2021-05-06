import requests
import sys

from bs4 import BeautifulSoup


def get_html(stock):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url = "https://xuangubao.cn/stock/"

    reponse=requests.get(url+stock,headers=headers)
    #print (reponse.text)
    soup=BeautifulSoup(reponse.text,'html.parser')
    title=soup.title.string.split(' ')

    stock_name = title[0]
    item=soup.find_all('div',class_='zhibiao-item')


    dict={}
    dict.update({stock_name:stock})
    #print (new_item)
    for inform in item:
        item_0=inform.find('span',class_='zhibiao-item-label')
        item_1=inform.find('span',class_='zhibiao-item-text')
        #print (item_0.get_text(),item_1.get_text())
        dict.update({item_0.get_text():item_1.get_text()})
        #print (inform.get_te xt())

    #print (dict.items())
    return dict

# 量比 quantity relative ratio




if __name__=="__main__":

    group={'瑞丰光电':'300241.SZ','高新兴':'300098.SZ','北汽蓝谷': '600733.SS',
           '供销大集': '000564.SZ','达安基因':'002030.SZ',
           '海尔智家': '600690.SS','好想你': '002582.SZ','奥马电器': '002668.SZ','世纪华通': '002602.SZ',}
    group2={'方正证券': '601901.SS','上海物贸':'600822.SS','百联股份': '600827.SS','特锐德': '300001.SZ','杭钢股份':'600126.SS',
            '韵达股份': '002120.SZ','岭南控股':'000524.SZ','ST加加':'002650.SZ',
            '*ST力帆': '601777.SS','ST同洲':'002052.SZ','ST双环 ': '000707.SZ',}
    group3={'东方能源': '000958.SZ','中文在线': '300364.SZ','跨境通 ': '002640.SZ','华金资本': '000532.SZ','华发股份': '600325.SS',}
    group_bak={'旋极信息': '300324.SZ','广电运通': '002152.SZ','中光学':'002189.SZ',
               '南天信息': '000948.SZ','神州信息': '000555.SZ',
               '明德生物': '002932.SZ','圣湘生物': '688289.SS','东方生物': '688298.SS',}


    groups={}
    groups.update(group)
    groups.update(group2)
    groups.update(group3)
   # groups.update(group5)
    groups.update(group_bak)

    for name,stock in groups.items():
        stock_item=get_html(stock)

        begin=float(stock_item.get("开盘价"))
        latest=float(stock_item.get("最新"))
        wave=round((latest-begin)/begin*100,2)
        stock_item["波动"]=wave

        low=float(stock_item.get("最低价"))
        high=float(stock_item.get("最高价"))
        wave2=round((high-low)/low*100,2)



        stock_item.pop('换手')
       # stock_item.pop('成交量')
        stock_item.pop('流通股本')
        stock_item.pop('总股本')
        stock_item.pop('市盈率TTM')
        # stock_item.pop('最高价')
        # stock_item.pop('最低价')

        s_rise=float(stock_item.get('涨幅').strip('%'))




        if stock in group.values():
            if s_rise>0:
                print(f'\033[0;46;0m{stock_item} \033[0m')
            else:
                print(f'\033[0;46;0m{stock_item}\033[0m' )
        elif stock in group2.values():
            if s_rise > 0:

                print(f'\033[0;46;0m{stock_item}\033[0m')
            else:
                print(f'\033[0;46;0m{stock_item}\033[0m')

        else:
            if s_rise > 0:
                print(f'\033[0;46;0m{stock_item}\033[0m')
            else:
                print(f'\033[0;46;0m{stock_item}\033[0m')
            #print (stock_item)

