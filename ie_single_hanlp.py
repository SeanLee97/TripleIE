# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:author: wangjian
:description: 结合LTP平台实现简单三元组抽取
"""

import logging

from utils.hanlp_util import HaNLPUtil
from utils.rules import Main


class TripleIEHaNLP(object):
    def __init__(self, sentence):
        self.logger = logging.getLogger("TripleIE")

        self.sentence = sentence
        self.clean_output = False  # 输出是否有提示
        self.triples = []
        self.v = ['v', 'vyou', 'vd', 'vf', 'vg', 'vi', 'vl', 'vn', 'vshi', 'vx']

    def run(self):
        self.logger.info("start to extract...")
        # 匹配规则
        sentence, rule_str, rule_type = Main(self.sentence).select_rules()
        self.extract(sentence, rule_str, rule_type)

        if rule_type == 'company' or rule_type == 'movie':
            self.extract(rule_str, '', '')

        elif rule_type == 'car':
            rule_str = '车辆' + rule_str
            self.extract(rule_str, '', '')

        elif rule_type == 'company_m5' or rule_type == 'movie_m5' or rule_type == 'population_m5':
            if rule_type == 'company_m5':
                rule_str = '公司' + rule_str
            elif rule_type == 'movie_m5':
                rule_str = '电影' + rule_str
            elif rule_type == 'population_m5':
                rule_str = '人口' + rule_str

            self.extract(rule_str, '', '')

        self.logger.info("done with extracting...")

        return self.triples

    def extract(self, sentence, rule_str, rule_type):
        HaUtil = HaNLPUtil(sentence)
        words = HaUtil.get_words()
        postags = HaUtil.get_postags()
        arcs = HaUtil.get_dependency_parser()
        sub_dicts = self._build_sub_dicts(words, arcs)

        arcs = arcs.getWordArray()
        for idx in range(len(postags)):
            if str(postags[idx]) in self.v:
                sub_dict = sub_dicts[idx]
                # 主谓宾
                if 'SBV' in sub_dict and 'VOB' in sub_dict:
                    e1 = self._fill_ent(words, postags, sub_dicts, sub_dict['SBV'][0])
                    r = words[idx]
                    e2 = self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
                    if self.clean_output:
                        self.triples.append("%s, %s, %s\n" % (e1, r, e2))
                    else:
                        self.triples.append("主谓宾 (%s, %s, %s)\n" % (e1, r, e2))
                # 定语后置，动宾关系
                if arcs[idx].DEPREL == 'ATT':
                    if 'VOB' in sub_dict:
                        e1 = self._fill_ent(words, postags, sub_dicts, arcs[idx].HEAD.ID - 1)
                        r = words[idx]
                        e2 = self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
                        temp_string = r + e2
                        if temp_string == e1[:len(temp_string)]:
                            e1 = e1[len(temp_string):]
                        if temp_string not in e1:
                            if self.clean_output:
                                self.triples.append("%s, %s, %s\n" % (e1, r, e2))
                            else:
                                self.triples.append("主谓宾 (%s, %s, %s)\n" % (e1, r, e2))
                # 时间关系
                nt_index = self._has_t(postags)
                if nt_index > -1 and 'VOB' in sub_dict:
                    e1 = words[nt_index]
                    r = words[idx]
                    e2 = words[sub_dict['VOB'][0]]
                    if self.clean_output:
                        self.triples.append("%s, %s, %s\n" % (e1, r, e2))
                    else:
                        self.triples.append("时间关系 (%s, %s, %s)\n" % (e1, r, e2))

                if rule_str and rule_type != 'company' and rule_type != 'car' and rule_type != 'movie':
                    e1 = rule_str
                    r = words[idx]
                    e2 = words[sub_dict['VOB'][0]] if 'VOB' in sub_dict else ''
                    if self.clean_output:
                        self.triples.append("%s, %s, %s\n" % (e1, r, e2))
                    else:
                        self.triples.append("附加关系 (%s, %s, %s)\n" % (e1, r, e2))

    def _has_t(self, postags):
        for (index, postag) in enumerate(postags):
            if postag == 'nt':
                return index

        return -1

    """
    :decription: 为句子中的每个词语维护一个保存句法依存儿子节点的字典
    :args:
        words: 分词列表
        postags: 词性列表
        arcs: 句法依存列表
    """

    def _build_sub_dicts(self, words, arcs):
        sub_dicts = []
        for idx in range(len(words)):
            sub_dict = dict()
            for arc_idx, arc in enumerate(arcs.iterator()):
                if arc.HEAD.ID == idx + 1:
                    if arc.DEPREL in sub_dict:
                        sub_dict[arc.DEPREL].append(arc_idx)
                    else:
                        sub_dict[arc.DEPREL] = []
                        sub_dict[arc.DEPREL].append(arc_idx)
            sub_dicts.append(sub_dict)
        return sub_dicts

    """
    :decription:完善识别的部分实体
    """

    def _fill_ent(self, words, postags, sub_dicts, word_idx):
        sub_dict = sub_dicts[word_idx]
        prefix = ''
        if 'ATT' in sub_dict:
            for i in range(len(sub_dict['ATT'])):
                prefix += self._fill_ent(words, postags, sub_dicts, sub_dict['ATT'][i])

        postfix = ''
        if str(postags[word_idx]) in self.v:
            if 'VOB' in sub_dict:
                postfix += self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
            if 'SBV' in sub_dict:
                prefix = self._fill_ent(words, postags, sub_dicts, sub_dict['SBV'][0]) + prefix

        return prefix + words[word_idx] + postfix


if __name__ == "__main__":
    IE = TripleIEHaNLP('1986年上海有人口')
    print(IE.run())
