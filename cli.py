# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:author: seanlee
:description: 结合LTP平台实现简单三元组抽取
:ctime: 2018.07.23 16:14
:mtime: 2018.07.23 16:14
"""

import logging
import argparse
from ie import TripleIE

def parse_args():
    parser = argparse.ArgumentParser('TripleIE')
    parser.add_argument('--data', type=str, default='data/question.txt',
                            help='the path to the data')
    parser.add_argument('--out', type=str, default='output/output.txt',
                            help='the path to output')
    parser.add_argument('--ltp', type=str, default='ltp_data',
                            help='the path to LTP model')
    parser.add_argument('--clean', action='store_true',
                            help='output the clean relation(no tips)')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    IE = TripleIE(args.data, args.out, args.ltp, args.clean)
    IE.run()
