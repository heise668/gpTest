import urllib3
import requests
import json
import time, datetime


#  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
requests.packages.urllib3.disable_warnings()
# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# 通过request()方法创建一个请求：
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }

#涨停板
url='https://flash-api.xuangubao.cn/api/pool/detail?pool_name=limit_up'
r = requests.get(url)
data=r.text
reponse = json.dumps(data,ensure_ascii=False)
#print (reponse)

resjson=json.loads(data)
#print (resjson['data'][0])

msg=resjson['data']
print (len(msg))

#
{'break_limit_down_times': 0,
 'break_limit_up_times': '1 开板数',
 'buy_lock_volume_ratio': 0.0172829274,
 'change_percent': '0.1(百分比)',
 'first_break_limit_down': 0,
  'first_break_limit_up': '1574045715(首次开板时间)',
  'first_limit_down': 0,
  'first_limit_up': '1574045682(首次涨停时间)',
  'is_new_stock': False,
  'issue_price': '18.1(发行价)',
  'last_break_limit_down': 0,
  'last_break_limit_up': '1574045715(首次开板时间)',
  'last_limit_down': 0,
  'last_limit_up': '1574059842(最后涨停时间)',
  'limit_down_days': 0,
  'limit_timeline':
  	{'items': [{'timestamp': 1574045682, 'status': 1}, {'timestamp': 1574045715, 'status': 2}, {'timestamp': 1574059842, 'status': 1}]},
  'limit_up_days': '2(涨停天数)',
  'listed_date': '1451491200(上市时间)',
  'm_days_n_boards_boards': 2,
  'm_days_n_boards_days': '2(连板天数)',
  'mtm': 0,
  'nearly_new_acc_pcp': 0,
  'nearly_new_break_days': 0,
  'new_stock_acc_pcp': -0.1674033149,
  'new_stock_break_limit_up': 0,
  'new_stock_limit_up_days': 0,
  'new_stock_limit_up_price_before_broken': 0,
  'non_restricted_capital': 2229111827.25,
  'price': 15.07,
  'sell_lock_volume_ratio': 0,
  'stock_chi_name': '盛天网络',
  'surge_reason': {
  			'symbol': '300494.SZ',
  			'stock_reason': '公司获第8批IDC、CDN、VPN、ISP牌照；为超过50000家网吧提供娱乐内容分发平台，上线游戏联运平台“易乐玩”',
  			'related_plates':
                [{'plate_id': 58759122, 'plate_name': 'VPN', 'plate_reason': '市场出现外网浏览器'},
  				{'plate_id': 18621010, 'plate_name': '游戏', 'plate_reason': 'Google Stadia云游戏19号上线'}]},
  'symbol': '300494.SZ',
  'total_capital': 3616800000,
  'turnover_ratio': 0.2339360118,
  'volume_bias_ratio': 5.6719043404,
  'yesterday_break_limit_up_times': 0,
  'yesterday_first_limit_up': '1573781403(昨天涨停时间)',
  'yesterday_last_limit_up': 1573781403,
  'yesterday_limit_down_days': 0,
  'yesterday_limit_up_days': '1(昨日涨停天数)'}
#

for items in msg[0:]:
    #print (items)

    stock_chi_name=items['stock_chi_name'] #股票名称
    stock_code=items['symbol']
    price=items['price']  #目前价格
    surge_reason=items['surge_reason']  #涨停理由
    # stock_reason=surge_reason['stock_reason']
    # related_plates = surge_reason['related_plates']
    limit_up_days=items['limit_up_days'] #涨停天数
    m_days_n_boards_days=items['m_days_n_boards_days'] #(连板天数),
    first_limit_up=items['first_limit_up'] #(首次z涨停时间)

    #使用time
    timeStamp = first_limit_up
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    #print(otherStyleTime)  # 2013--10--10 23:40:00

    # platelist=[]
    # for related_plate in related_plates:
    #     platelist.append(related_plate["plate_name"])
    # print(otherStyleTime,stock_chi_name,stock_code,price,limit_up_days,"reason=",stock_reason,",plate=",platelist)
    print(otherStyleTime, stock_chi_name, stock_code, price, limit_up_days )



