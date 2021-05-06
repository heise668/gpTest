import datetime

import requests
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
    item=soup.find('table',class_='tb0td1')
    return item


def get_data(url,today):
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

        if today in date:
            if gdType=='十大流通股东':
                circulation.append([seq,gdType,date,name,gdnum,gdRatio,change,changeNum])
            elif gdType =='十大股东':
                holdertop.append([seq,gdType,date,name,gdnum,gdRatio,change,changeNum])

    # 十大股东
    for gd in holdertop[0:10]:
        print (gd)

    # 十大流通股东
    for gd in circulation:
        print (gd)


if __name__=="__main__":
    url = "http://cwzx.shdjt.com/gpdmgd.asp?gpdm="

    group = {'好想你':'002582.SZ','丰华股份':'600615.SS','东旭光电': '000413.SZ',
             '申华控股':'600653.SS','许继电气': '000400.SZ','友好集团':'600778.SS',
             '文投控股': '600715.SS','ST加加': '002650.SZ','深粮控股':'000019.SZ',
             '上海环境': '601200.SS', '海尔智家': '600690.SS', '瑞丰光电': '300241.SZ',
             '百联股份':'600827.SS', '国芳集团': '601086.SS','岭南控股':'000524.SZ',
             '杭钢股份': '600126.SS','海通证券': '600837.SS','国联证券': '601456.SS','国金证券': '600109.SS',
             '海汽集团': '603069.SS','炼石航空':'000697.SZ','本钢板材':'000761.SZ',
        'ST同洲':'002052.SZ','ST华仪':'600290.SS','ST银河': '000806.SZ','ST庞大': '601258.SS',
             'ST东网': '002175.SZ','韵达股份': '002120.SZ','易联众':'300096.SZ','尚品宅配':'300616.SZ',
             'ST双环': '000707.SZ','ST海源':'002529.SZ','ST西发':'000752.SZ','ST河化':'000953.SZ',
        '东旭蓝天': '000040.SZ','南宁百货':'600712.SS','奥马电器': '002668.SZ','南天信息': '000948.SZ',
        '东百集团':'600693.SS','博实股份': '002698.SZ','供销大集': '000564.SZ','小商品城':'600415.SS',
        '芒果超媒': '300413.SZ','青海春天':'600381.SS','长航凤凰':'000520.SZ','会稽山':'601579.SS'}


    code=group.get('韵达股份').split('.')[0]

    url=url+code
    today=str(datetime.date.today().year)
    get_data(url,today)