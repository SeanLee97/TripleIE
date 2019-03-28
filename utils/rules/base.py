import abc


class Base():
    def __init__(self, sentence):
        self.sentence = sentence

    # 获取规则
    @abc.abstractmethod
    def get_result(self):
        pass
