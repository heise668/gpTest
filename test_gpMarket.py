import requests
import sys
import json
from bs4 import BeautifulSoup

def get_html(stock):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url = "https://api-ddc-wscn.xuangubao.cn/market/real?fields=prod_name,last_px,px_change,px_change_rate,high_px,low_px,open_px,preclose_px,business_amount,business_balance,market_value,turnover_ratio,dyn_pb_rate,amplitude,pe_rate,bps,hq_type_code,trade_status,bid_grp,offer_grp,business_amount_in,business_amount_out,circulation_value,securities_type,update_time,price_precision&prod_code="

    reponse=requests.get(url+stock,headers=headers)
    # print (reponse.text)
    data=json.loads(reponse.text)
    print(data)
    return data


'''	
0	"prod_name" 名称
1	"last_px" 最新价
2	"px_change"  换手率
3	"px_change_rate" 量比
4	"high_px" 最高价
5	"low_px" 最低价
6	"open_px" 开盘价
7	"preclose_px" 昨日收盘价
8	"market_value" 总市值
9	"turnover_ratio" 
10	"dyn_pb_rate" 
11	"amplitude"
12	"pe_rate"
13	"bps"
14	"hq_type_code"
15	"trade_status"
16	"bid_grp"
17	"offer_grp"
18	"business_amount_in"
19	"business_amount_out"
20	"circulation_value"
21	"securities_type"
22	"update_time"
23	"price_precision"
24	"delisting_date"
'''

if __name__=="__main__":

    group={'东方能源': '000958.SZ'}



    groups={}
    groups.update(group)

    for name,stock in groups.items():
        stock_item=get_html(stock)

