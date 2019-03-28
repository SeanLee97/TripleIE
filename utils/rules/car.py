import re

from utils.rules.base import Base


class Car(Base):
    def __init__(self, sentence):
        super(Car, self).__init__(sentence)

    def get_result(self):
        # 公车辆规则
        str = ''

        m_1 = re.search(r'(.*)月+(.*)号+(.*)到(.*)点+', self.sentence)
        m_2 = re.search(r'(.*)月+(.*)号+', self.sentence)
        m_3 = re.search(r'[有]+(.*)', self.sentence)

        if m_1:
            str = m_1.group()
            sentence = self.sentence.replace(str, '车辆')

            return sentence, str, 'car_m1'
        if m_2:
            str = m_2.group()
            sentence = self.sentence.replace(str, '车辆')

            return sentence, str, 'car_m2'
        elif m_3:
            str = m_3.group()
            sentence = self.sentence[:len(self.sentence) - len(str)]

            return sentence, str, 'car'

        else:

            return self.sentence, str, 'car'
