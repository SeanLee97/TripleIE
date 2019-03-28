import re

from utils.rules.base import Base


class Company(Base):
    def __init__(self, sentence):
        super(Company, self).__init__(sentence)

    def get_result(self):
        # 公司规则
        str = ''
        m_1 = re.search(
            r'(.*)月*(.*)(工作时长|工作年限)(.*)(大于|小于|大于等于|小于等于|等于|不等于|不大于|不小于|超过|不足|不超过|低于|高于|不低于|不高于)+\d*(小时|年)+',
            self.sentence)
        m_2 = re.search(
            r'(.*)月*(.*)(工作时长|工作年限)(.*)(大于|小于|大于等于|小于等于|等于|不等于|不大于|不小于|超过|不足|不超过|低于|高于|不低于|不高于)+\w', self.sentence)
        m_3 = re.search(
            r'(.*)月*(.*)(工作时长|工作年限)(.*)(大于|小于|大于等于|小于等于|等于|不等于|不大于|不小于|超过|不足|不超过|低于|高于|不低于|不高于)+(\d+)', self.sentence)
        m_4 = re.search(r'(.*)月+(.*)日+', self.sentence)
        m_5 = re.search(r'[有]+(.*)', self.sentence)

        if m_1:
            str = m_1.group()
            sentence = self.sentence.replace(str, '公司')

            return sentence, str, 'company'
        elif m_2:
            str = m_2.group()
            sentence = self.sentence.replace(str, '公司')

            return sentence, str, 'company'
        elif m_3:
            str = m_3.group()
            sentence = self.sentence.replace(str, '公司')

            return sentence, str, 'company'
        elif m_4:
            str = m_4.group()
            sentence = self.sentence.replace(str, '公司')

            return sentence, str, 'company_m4'
        elif m_5:
            str = m_5.group()
            str_rt = self.sentence[:len(self.sentence) - len(str)]
            sentence = '公司' + str

            return sentence, str_rt, 'company_m5'
        else:
            sentence = self.sentence

            return sentence, str, 'company'
