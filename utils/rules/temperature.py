import re

from utils.rules.base import Base


class Temperature(Base):
    def __init__(self, sentence):
        super(Temperature, self).__init__(sentence)

    def get_result(self):
        # 气温规则
        str = ''
        m_1 = re.search(
            r'(最低气温|最高气温)(.+?)(大于|小于|大于等于|小于等于|等于|不等于|不大于|不小于|超过|不足|不超过)?(.+?)(\d+)度*', self.sentence)

        if m_1:
            str = m_1.group()
            str = str[:4]

        return self.sentence, str, 'temperature'
