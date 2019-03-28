# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:author: seanlee97
:description: 结合LTP平台实现简单三元组抽取
:ctime: 2018.07.23 16:14
:mtime: 2018.07.23 16:14
"""

import logging
import os
import sys
from importlib import reload

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf8")

from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer
from tqdm import tqdm
import utils as U
from utils.rules import Main


class TripleIE(object):
    def __init__(self, in_file_path, out_file_path, model_path, clean_output=False):
        self.logger = logging.getLogger("TripleIE")

        self.in_file_path = in_file_path
        self.out_file_path = out_file_path
        self.model_path = model_path
        self.clean_output = clean_output  # 输出是否有提示

        self.out_handle = None

        self.segmentor = Segmentor()
        self.segmentor.load(os.path.join(self.model_path, "cws.model"))
        self.postagger = Postagger()
        self.postagger.load(os.path.join(self.model_path, "pos.model"))
        self.parser = Parser()
        self.parser.load(os.path.join(self.model_path, "parser.model"))
        self.recognizer = NamedEntityRecognizer()
        self.recognizer.load(os.path.join(self.model_path, "ner.model"))

    def run(self, in_file_path=None, out_file_path=None):
        if in_file_path is not None:
            self.in_file_path = in_file_path
        if out_file_path is not None:
            self.out_file_path = out_file_path

        self.out_handle = open(self.out_file_path, 'a', encoding="utf-8")

        with open(self.in_file_path, "r", encoding="utf-8") as rf:
            self.logger.info("loadding input file {}...".format(self.in_file_path))
            text = ""
            for index, line in enumerate(rf):
                line = line.strip()
                text = line

                text = U.rm_html(text)
                sentences = U.split_by_sign(text)

                self.logger.info("detect {} sentences".format(len(sentences)))
                self.logger.info("start to extract...")
                for sentence in tqdm(sentences):
                    # 匹配规则
                    sentence, rule_str, rule_type = Main(sentence).select_rules()
                    # print(sentence)
                    # print(rule_str)
                    # print(rule_type)
                    # exit()
                    self.extract(sentence, index + 1, rule_str, rule_type)

                    if rule_type == 'company' or rule_type == 'movie':
                        self.extract(rule_str, index + 1, '', '')

                    elif rule_type == 'car':
                        rule_str = '车辆' + rule_str
                        self.extract(rule_str, index + 1, '', '')

                    elif rule_type == 'company_m5' or rule_type == 'movie_m5':
                        if rule_type == 'company_m5':
                            rule_str = '公司' + rule_str
                        elif rule_type == 'movie_m5':
                            rule_str = '电影' + rule_str
                        self.extract(rule_str, index + 1, '', '')

            self.logger.info("done with extracting...")
            self.logger.info("output to {}".format(self.out_file_path))

        # close handle
        self.out_handle.close()

    def extract(self, sentence, index, rule_str, rule_type):
        words = self.segmentor.segment(sentence)
        postags = self.postagger.postag(words)
        ner = self.recognizer.recognize(words, postags)
        arcs = self.parser.parse(words, postags)
        sub_dicts = self._build_sub_dicts(words, postags, arcs)

        # print('\t'.join(words))
        # print('\t'.join(postags))
        # print('\t'.join(ner))
        # print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
        # print(sub_dicts)

        for idx in range(len(postags)):

            if postags[idx] == 'v':
                sub_dict = sub_dicts[idx]
                # 主谓宾
                if 'SBV' in sub_dict and 'VOB' in sub_dict:
                    e1 = self._fill_ent(words, postags, sub_dicts, sub_dict['SBV'][0])
                    r = words[idx]
                    e2 = self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
                    if self.clean_output:
                        self.out_handle.write("%s\t%s, %s, %s\n" % (index, e1, r, e2))
                    else:
                        self.out_handle.write("%s\t主谓宾\t(%s, %s, %s)\n" % (index, e1, r, e2))
                    self.out_handle.flush()
                # 定语后置，动宾关系
                if arcs[idx].relation == 'ATT':
                    if 'VOB' in sub_dict:
                        e1 = self._fill_ent(words, postags, sub_dicts, arcs[idx].head - 1)
                        r = words[idx]
                        e2 = self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
                        temp_string = r + e2
                        if temp_string == e1[:len(temp_string)]:
                            e1 = e1[len(temp_string):]
                        if temp_string not in e1:
                            if self.clean_output:
                                self.out_handle.write("%s\t%s, %s, %s\n" % (index, e1, r, e2))
                            else:
                                self.out_handle.write("%s\t主谓宾\t(%s, %s, %s)\n" % (index, e1, r, e2))

                            self.out_handle.flush()
                # 时间关系
                nt_index = self._has_t(postags)
                if nt_index > -1 and 'VOB' in sub_dict:
                    e1 = words[nt_index]
                    r = words[idx]
                    e2 = words[sub_dict['VOB'][0]]
                    if self.clean_output:
                        self.out_handle.write("%s\t%s, %s, %s\n" % (index, e1, r, e2))
                    else:
                        self.out_handle.write("%s\t时间关系\t(%s, %s, %s)\n" % (index, e1, r, e2))
                    self.out_handle.flush()

                if rule_str and rule_type != 'company' and rule_type != 'car' and rule_type != 'movie':
                    e1 = rule_str
                    r = words[idx]
                    e2 = words[sub_dict['VOB'][0]] if 'VOB' in sub_dict else ''
                    if self.clean_output:
                        self.out_handle.write("%s\t%s, %s, %s\n" % (index, e1, r, e2))
                    else:
                        self.out_handle.write("%s\t附加关系\t(%s, %s, %s)\n" % (index, e1, r, e2))
                    self.out_handle.flush()

            # 抽取命名实体有关的三元组
            try:
                if ner[idx][0] == 'S' or ner[idx][0] == 'B':
                    ni = idx
                    if ner[ni][0] == 'B':
                        while len(ner) > 0 and len(ner[ni]) > 0 and ner[ni][0] != 'E':
                            ni += 1
                        e1 = ''.join(words[idx:ni + 1])
                    else:
                        e1 = words[ni]
                    if arcs[ni].relation == 'ATT' and postags[arcs[ni].head - 1] == 'n' and ner[
                        arcs[ni].head - 1] == 'O':
                        r = self._fill_ent(words, postags, sub_dicts, arcs[ni].head - 1)
                        if e1 in r:
                            r = r[(r.idx(e1) + len(e1)):]
                        if arcs[arcs[ni].head - 1].relation == 'ATT' and ner[arcs[arcs[ni].head - 1].head - 1] != 'O':
                            e2 = self._fill_ent(words, postags, sub_dicts, arcs[arcs[ni].head - 1].head - 1)
                            mi = arcs[arcs[ni].head - 1].head - 1
                            li = mi
                            if ner[mi][0] == 'B':
                                while ner[mi][0] != 'E':
                                    mi += 1
                                e = ''.join(words[li + 1:mi + 1])
                                e2 += e
                            if r in e2:
                                e2 = e2[(e2.idx(r) + len(r)):]
                            if r + e2 in sentence:
                                if self.clean_output:
                                    self.out_handle.write("%s\t%s, %s, %s\n" % (index, e1, r, e2))
                                else:
                                    self.out_handle.write("%s\t主谓宾\t(%s, %s, %s)\n" % (index, e1, r, e2))

                                self.out_handle.flush()
            except:
                pass

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

    def _build_sub_dicts(self, words, postags, arcs):
        sub_dicts = []
        for idx in range(len(words)):
            sub_dict = dict()
            for arc_idx in range(len(arcs)):
                if arcs[arc_idx].head == idx + 1:
                    if arcs[arc_idx].relation in sub_dict:
                        sub_dict[arcs[arc_idx].relation].append(arc_idx)
                    else:
                        sub_dict[arcs[arc_idx].relation] = []
                        sub_dict[arcs[arc_idx].relation].append(arc_idx)
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
        if postags[word_idx] == 'v':
            if 'VOB' in sub_dict:
                postfix += self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
            if 'SBV' in sub_dict:
                prefix = self._fill_ent(words, postags, sub_dicts, sub_dict['SBV'][0]) + prefix

        return prefix + words[word_idx] + postfix
