import re

from utils.rules.base import Base


class Movie(Base):
    def __init__(self, sentence):
        super(Movie, self).__init__(sentence)

    def get_result(self):
        # 电影规则
        str = ''
        m_1 = re.search(
            r'(.*)月*(.*)(评分|评论|单日票房|实时票房|电影单价|电影票销售数量|每日销售量|每日总票房|单张利润|销售额|片长)(.*)(大于|小于|大于等于|小于等于|等于|不等于|不大于|不小于|超过|不足|不超过|低于|高于|不低于|不高于)+\d*(小时|年)+',
            self.sentence)
        m_2 = re.search(
            r'(.*)月*(.*)(评分|评论|单日票房|实时票房|电影单价|电影票销售数量|每日销售量|每日总票房|单张利润|销售额|片长)(.*)(大于|小于|大于等于|小于等于|等于|不等于|不大于|不小于|超过|不足|不超过|低于|高于|不低于|不高于)+\w',
            self.sentence)
        m_3 = re.search(
            r'(.*)月*(.*)(评分|评论|单日票房|实时票房|电影单价|电影票销售数量|每日销售量|每日总票房|单张利润|销售额|片长)(.*)(大于|小于|大于等于|小于等于|等于|不等于|不大于|不小于|超过|不足|不超过|低于|高于|不低于|不高于)+(\d+)',
            self.sentence)
        m_4 = re.search(r'(.*)月+(.*)日+', self.sentence)
        m_5 = re.search(r'[有]+(.*)', self.sentence)

        if m_1:
            str = m_1.group()
            sentence = self.sentence.replace(str, '电影')

            return sentence, str, 'movie'
        elif m_2:
            str = m_2.group()
            sentence = self.sentence.replace(str, '电影')

            return sentence, str, 'movie'
        elif m_3:
            str = m_3.group()
            sentence = self.sentence.replace(str, '电影')

            return sentence, str, 'movie'
        elif m_4:
            str = m_4.group()
            sentence = self.sentence.replace(str, '电影')

            return sentence, str, 'movie_m4'
        elif m_5:
            str = m_5.group()
            str_rt = self.sentence[:len(self.sentence) - len(str)]
            sentence = '电影' + str

            return sentence, str_rt, 'company_m5'
        else:
            sentence = self.sentence

            return sentence, str, 'movie'
