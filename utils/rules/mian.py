import re
from utils.rules.population import Population
from utils.rules.temperature import Temperature
from utils.rules.company import Company
from utils.rules.car import Car
from utils.rules.movie import Movie


class Main():
    def __init__(self, sentence):
        self.sentence = sentence

    def select_rules(self):
        # 人口
        m_population = re.search(r'(.+?)(人口|男女比例)(.*)', self.sentence)
        if m_population:
            return Population(self.sentence).get_result()

        # 天气
        m_temperature = re.search(r'(.+?)(气温|最低气温|最高气温)(.*)', self.sentence)
        if m_temperature:
            return Temperature(self.sentence).get_result()

        # 公司
        m_company = re.search(r'(.*)(工作|工作时长|工作年限|员工|科大讯飞|泰山集团|股价|涨跌|成交量|负面舆情数|评论数|热门帖子|帖子评论量|营业额)(.*)', self.sentence)
        if m_company:
            return Company(self.sentence).get_result()

        # 车辆
        m_car = re.search(r'(.*)(车|车辆|车主|车速|车辆信息)(.*)', self.sentence)
        if m_car:
            return Car(self.sentence).get_result()

        # 电影
        m_car = re.search(r'(.*)(电影|评分|评论|单日票房|实时票房|电影单价|电影票销售数量|每日销售量|每日总票房|单张利润|销售额|片长|订单)(.*)', self.sentence)
        if m_car:
            return Movie(self.sentence).get_result()

        return self.sentence, '', None
