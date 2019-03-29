import re

with open('question.txt', 'r', encoding='utf-8') as f:
    questions = f.readlines()

def select_question(question):
    global normalize_list
    # 是否为并列问题, 拆分成多个问题, '和'关键字
    m_and_1 = re.search(r'(.*)(和)+(.*)', question)
    if m_and_1:
        question_list = deal_and_question(question)
        return question_list

    return []


# 是否为并列问题, 拆分成多个问题, '和'关键字
def deal_and_question(question):
    prefix = ''
    question_list = []
    rule_1 = r'(总)*(农村人口|城镇人口|男性人口|女性人口|男女比例|人口|销售额|销量|营业额|利润|订单量|订单id|合同id|合同金额)+'
    rule_2 = r'(总)+(农村人口|城镇人口|男性人口|女性人口|男女比例|人口|销售额|销量|营业额|利润|订单量|订单id|合同id|合同金额)+'

    q_list = question.split('和')
    for i, q in enumerate(q_list):
        m_i = re.search(rule_1, q)
        if i == 0:
            if m_i:
                # 获取公共前缀
                prefix = q[:len(q) - len(m_i.group())]
                question_0 = prefix + m_i.group()
                # 将总人口替换成人口
                m = re.search(rule_2, question_0)
                if m:
                    before = question_0[:len(question_0) - len(m.group())]
                    after = m.group().replace('总', '')
                    question_list.append(before + after)
                else:
                    question_list.append(prefix + m_i.group())
        else:
            if m_i:
                question_n = prefix + m_i.group()
                # 将总人口替换成人口
                m = re.search(rule_2, question_n)
                if m:
                    before = question_n[:len(question_n) - len(m.group())]
                    after = m.group().replace('总', '')
                    question_list.append(before + after)
                else:
                    question_list.append(prefix + m_i.group())

    return question_list


def replace_words(question):
    # 人口
    question = question.replace('农村的人口', '农村人口')
    question = question.replace('城镇的人口', '城镇人口')
    question = question.replace('男性的人口', '男性人口')
    question = question.replace('女性的人口', '女性人口')
    question = question.replace('多少人', '人口')
    question = question.replace('人口数', '人口')
    question = question.replace('人口数量', '人口')
    question = question.replace('人口总数', '人口')
    question = question.replace('人数', '人口')
    question = question.replace('人的数量', '人口')
    question = question.replace('人的总数', '人口')
    question = question.replace('人口的数量', '人口')

    question = question.replace('销售数量', '销量')
    question = question.replace('销售的数量', '销量')
    question = question.replace('销售数', '销量')

    question = question.replace('订单数量', '订单量')
    question = question.replace('订单的数量', '订单量')

    question = question.replace('负面舆情数量', '负面舆情数')
    question = question.replace('负面舆情的数量', '负面舆情数')

    question = question.replace('评论数量', '评论数')
    question = question.replace('评论的数量', '评论数')

    question = question.replace('点赞数量', '点赞量')
    question = question.replace('点赞的数量', '点赞量')

    question = question.replace('阅读数量', '阅读量')
    question = question.replace('阅读的数量', '阅读量')

    question = question.replace('转发数数量', '转发数')
    question = question.replace('转发的数量', '转发数')

    question = question.replace('有多少', '')
    question = question.replace('有哪些', '')
    question = question.replace('哪些', '')
    question = question.replace('那些', '')
    question = question.replace('哪个', '')
    question = question.replace('那个', '')
    question = question.replace('所有', '')
    question = question.replace('打开', '')
    question = question.replace('查找', '')
    question = question.replace('查询', '')
    question = question.replace('找出', '')
    question = question.replace('查查', '')
    question = question.replace('查看', '')
    question = question.replace('看看', '')
    question = question.replace('筛选', '')
    question = question.replace('选择', '')
    question = question.replace('选出', '')
    question = question.replace('筛选出', '')

    question = question.replace('的', '有')

    return question


normalize_list = []
for question in questions:
    question_format = question.strip()
    question_format = replace_words(question_format)
    q_list = select_question(question_format)
    if len(q_list):
        for q in q_list:
            normalize_list.append(q)
    else:
        normalize_list.append(question_format)

with open('normalize.txt', 'a+', encoding='utf-8') as f:
    for line in normalize_list:
        line = line.replace('总', '')
        f.write(line + '\n')
