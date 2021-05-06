import test_gp2 as gp2

class gpgroup:
    def __init__(self,name):
        self.name=name

    def get_group(self):

        if (self.name=='5G'):
            g1=['瑞丰光电','风华高科','宏达电子','德赛电池','漫步者','宁波韵升','长盈精密']
            return g1

        #工业大麻
        gydm={'康恩贝', '顺灏股份','龙津药业','紫鑫药业', '聆达股份','劲嘉股份',}
        #食品饮料
        g_food=['ST加加','永辉超市']

        # 被动元件，5G,AR/VR，无线耳机，智能穿戴
        g_5g=['瑞丰光电','风华高科','宏达电子','德赛电池','漫步者','宁波韵升','长盈精密']
        g_bdyj=[]
        g_ar=[]
        g_airpod=[]
        # 知识产权，国产软件，网络安全，文化传媒
        g_k=['光一科技',]
        # 区块链，电子发票，智慧物流，金融科技，比特币，电子货币
        g_btc=['奥马电器','南天信息','飞天诚信','广电运通','深大通']
        # 环保，垃圾回收，黄河
        # 长三角一体化，黄河流域，雄安新区，自贸区，海南自贸，新疆，西藏，粤港澳
        # 国企改革，深圳国企，上海国企，地方国企，北京国企
        # 应急产业，华铁应急,养老产业，博彩，赛马，电竞
        # 密集调研
        # 新能源汽车，充电桩，特斯拉，蔚来汽车概念股，换电概念
        #

    def get_code(self):
        group = {'海汽集团': ':603069.SS', '上海物贸': '600822.SS', '百联股份': '600827.SS', '山东药玻': '600529.SS',
             '韵达股份': '002120.SZ', '岭南控股': '000524.SZ', '海尔智家': '600690.SS', '方正证券': '601901.SS',
             '申华控股': '600653.SS', '杭钢股份': '600126.SS', '特锐德': '300001.SZ', '三峡水利': '600116.SS',
             '星期六': '002291.SZ', '跨境通 ': '002640.SZ', '东方能源': '000958.SZ',
             'ST同洲': '002052.SZ', 'ST华仪': '600290.SS', 'ST银河': '000806.SZ', 'ST双环 ': '000707.SZ',
             '*ST实达': '600734.SS', 'ST加加': '002650.SZ',
             '瑞丰光电': '300241.SZ', '风华高科': '000636.SZ', '宏达电子': '300726.SZ', '德赛电池': '000049.SZ',
             '漫步者 ': '002351.SZ', '宁波韵升': '600366.SS', '长盈精密': '300115.SZ',
             '康恩贝': '600572.SS', '顺灏股份': '002565.SZ', '龙津药业': '002750.SZ', '紫鑫药业': '002118.SZ', '聆达股份': '300125.SZ',
             '劲嘉股份': '002191.SZ', '光一科技': '300356.SZ', '朗科科技': '300042.SZ', '一汽解放': '000800.SZ',
             '北汽蓝谷': '600733.SS', '徐工机械': '000425.SZ', '精测电子': '300567.SZ','神州信息': '000555.SZ',
             '中光学': '002189.SZ', '中威电子': '300270.SZ', '冰山冷热': '000530.SZ', '海容冷链': '603187.SS',
             '永辉超市': '601933.SS', '*ST力帆': '601777.SS', '奥马电器': '002668.SZ', '南天信息': '000948.SZ', '深大通': '000038.SZ',
             'ST东网': '002175.SZ','炼石航空':'000697.SZ','易联众':'300096.SZ','小商品城':'600415.SS','好想你': '002582.SZ',
             '山西证券': '002500.SZ', '华泰证券': '601688.SS', '财通证券': '601108.SS', '中信证券': '600030.SS', '国泰君安': '601211.SS',
             '中信建投': '601066.SS', '东方财富': '300059.SZ', '国联证券': '601456.SS', '国金证券': '600109.SS','招商证券': '600999.SS',
                 '华林证券': '002945.SZ','东兴证券': '601198.SS',
                 '尚品宅配':'300616.SZ','会稽山':'601579.SS','葛洲坝': '600068.SS','旋极信息': '300324.SZ','广电运通': '002152.SZ',
                '华金资本': '000532.SZ','华发股份': '600325.SS','世联行': '002285.SZ',
                 '世纪华通': '002602.SZ', '顺网科技': '300113.SZ',}


        if self.name in group.keys():
            return {self.name:group.get(self.name)}
        else:
            return self.name





if __name__=="__main__":

    list=['北汽蓝谷']
    for v in list:

        g=gpgroup(v)
        group=g.get_code()
        print (group)