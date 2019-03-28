import re

from utils.rules.base import Base


class Population(Base):
    def __init__(self, sentence):
        super(Population, self).__init__(sentence)

    def get_result(self):
        # 时间规则
        str = ''
        m_1 = re.search(r'(大前天|前天|昨天|今天|上午|下午|晚上)(.+?)到(大前天|前天|昨天|今天|上午|下午|晚上)?(.+?)点?', self.sentence)
        m_2 = re.search(r'(大前年|前年|去年|上一年|前一年|今年)(.+?)到(大前年|前年|去年|上一年|前一年|今年)?(.+?)月?', self.sentence)

        if m_1:
            str = m_1.group()
            sentence = self.sentence.replace(str, '')
        elif m_2:
            str = m_2.group()
            sentence = self.sentence.replace(str, '')
        else:
            sentence = self.sentence

        return sentence, str, 'population'
