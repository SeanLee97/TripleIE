# -*- coding: utf-8 -*-

"""
:author: lxm
:description: 工具包
:ctime: 2018.07.13 17:13
:mtime: 2018.07.13 17:13
"""

import re

def rm_signs(raw):
    return re.sub(r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", raw)

def rm_html(raw):
    dr = re.compile(r'<[^>]+>',re.S)
    return dr.sub('',raw)

def split_by_sign(raw, regex=r'[\s+\!！。？\n\t]'):
    arr = re.split(regex, raw)
    return list(filter(lambda x: len(x.strip()) > 0, arr))

if __name__ == '__main__':
    arr = split_by_sign('''成年大白鲨平均体长在4～5.9米之间，平均重量为2000公斤，已知最大的大白鲨长度达7.2米，体重3200公斤，雌性比雄性要大一些。
        它拥有乌黑的眼睛、凶恶的牙齿和双颚，跟食人鲳差不多，一般体灰色、淡蓝色或淡褐色，腹部呈淡白色，背腹体色界限分明，体型大者色较淡；
        身体硕重，尾呈新月形，牙大且有锯齿缘，呈三角形。在所有的鲨鱼之中，大白鲨是唯一的可以把头部直立于水面之上的鲨鱼，这赋予它们在水面之上寻找潜在猎物的优势。 [1] 大白鲨还可潜入海底1200米深的地方。''')
    print(arr, len(arr))
