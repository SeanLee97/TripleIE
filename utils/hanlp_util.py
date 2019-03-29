from pyhanlp import *


class HaNLPUtil():
    def __init__(self, sentence):
        self.sentence = sentence
        self.segment = None
        self.words = []
        self.postags = []
        self.individual_dict = {}
        self.__init_util()

    def __init_util(self):
        # 进行分词
        self.segment = HanLP.segment(self.sentence)
        # 获取单词
        for term in self.segment:
            self.words.append(term.word)
            self.postags.append(term.nature)

    # 获取分词结果
    def get_terms(self):
        return self.segment

    # 获取分词中的单词列表
    def get_words(self):
        return self.words

    # 获取词性
    def get_postags(self):
        return self.postags

    # 获取依存句法分析
    # CONLL标注格式包含10列，分别为：
    # ———————————————————————————
    # ID   FORM    LEMMA   CPOSTAG POSTAG  FEATS   HEAD    DEPREL  PHEAD   PDEPREL
    # ———————————————————————————
    #
    # 只用到前８列，其含义分别为：
    #
    # 1    ID      当前词在句子中的序号，１开始.
    # 2    FORM    当前词语或标点
    # 3    LEMMA   当前词语（或标点）的原型或词干，在中文中，此列与FORM相同
    # 4    CPOSTAG 当前词语的词性（粗粒度）
    # 5    POSTAG  当前词语的词性（细粒度）
    # 6    FEATS   句法特征，在本次评测中，此列未被使用，全部以下划线代替。
    # 7    HEAD    当前词语的中心词
    # 8    DEPREL  当前词语与中心词的依存关系
    #
    # 在CONLL格式中，每个词语占一行，无值列用下划线'_'代替，列的分隔符为制表符'\t'，行的分隔符为换行符'\n'；句子与句子之间用空行分隔。
    # 依存标签
    # HED = "核心关系"
    # SBV = "主谓关系"
    # VOB = "动宾关系"
    # IOB = "间宾关系"
    # FOB = "前置宾语"
    # DBL = "兼语"
    # ATT = "定中关系"
    # ADV = "状中结构"
    # CMP = "动补结构"
    # COO = "并列关系"
    # POB = "介宾关系"
    # LAD = "左附加关系"
    # RAD = "右附加关系"
    # IS = "独立结构"
    # WP = "标点符号"

    # v	动词
    # vd	副动词
    # vf	趋向动词
    # vg	动词性语素
    # vi	不及物动词（内动词）
    # vl	动词性惯用语
    # vn	名动词
    # vshi	动词“是”
    # vx	形式动词
    # vyou	动词“有”

    def get_dependency_parser(self):
        parse = JClass('com.hankcs.hanlp.dependency.nnparser.NeuralNetworkDependencyParser')

        return parse.compute(self.segment)

    def get_ner(self):
        NLPTokenizer = HanLP.newSegment("crf")

        return NLPTokenizer.seg(self.sentence)


if __name__ == '__main__':
    HaUtil = HaNLPUtil("周星驰出演过哪些电影")
    print(HaUtil.get_ner())
    exit()
    for term in HaUtil.get_terms():
        print(term.nature)
        exit()
