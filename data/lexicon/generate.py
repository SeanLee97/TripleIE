years = ['大前年', '前年', '去年', '上一年', '前一年', '今年']
days = ['大前天', '前天', '昨天', '今天']
day_CNs = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
           '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
           '二十一', '二十二', '二十三', '二十四', '二十五', '二十六', '二十七', '二十八', '三十', '三十一']
day_zones = ['上午', '下午', '晚上']
time_CNs = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']
time_Nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
clock_h_CNs = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
               '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
               '二十一', '二十二', '二十三']
clock_m_CNs = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
               '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
               '二十一', '二十二', '二十三', '二十四', '二十五', '二十六', '二十七', '二十八', '二十九', '三十',
               '三十一', '三十二', '三十三', '三十四', '三十五', '三十六', '三十七', '三十八', '三十九', '四十',
               '四十一', '四十二', '四十三', '四十四', '四十五', '四十六', '四十七', '四十八', '四十九', '五十',
               '五十一', '五十二', '五十三', '五十四', '五十五', '五十六', '五十七', '五十八', '五十九']

# 随机生成年份月份格式:去年三月 去年3月
print('=======list_year_month=======')
list_year_month = []
for year in years:
    for time_CN in time_CNs:
        str_CN = year + time_CN + '月'
        list_year_month.append(str_CN)
    for time_Num in time_Nums:
        str_Num = year + time_Num + '月'
        list_year_month.append(str_Num)
with open('lexicon.txt', 'a+', encoding='utf-8') as f:
    for item in list_year_month:
        line = item + '\n'
        f.write(line)

# 随机生成日期时区时间格式: 昨天上午 昨天下午 昨天晚上
print('=======list_day_zone_time=======')
list_day_zone = []
for day in days:
    for day_zone in day_zones:
        string = day + day_zone
        list_day_zone.append(string)
with open('lexicon.txt', 'a+', encoding='utf-8') as f:
    for item in list_day_zone:
        line = item + '\n'
        f.write(line)

# 随机生成月份日期格式:三月一日 三月1日 3月一日 3月1日
print('=======list_month_day=======')
list_month_day = []
# 三月一日 三月1日
for time_CN in time_CNs:
    for i in range(1, 32):
        str_CN_NUM = time_CN + '月' + str(i) + '日'
        list_month_day.append(str_CN_NUM)

    for day_CN in day_CNs:
        str_CN_CN = time_CN + '月' + day_CN + '日'
        list_month_day.append(str_CN_CN)

# 3月一日 3月1日
for time_Num in time_Nums:
    for day_CN in day_CNs:
        str_Num_CN = time_Num + '月' + day_CN + '日'
        list_month_day.append(str_Num_CN)

    for i in range(1, 32):
        str_NUM_NUM = time_Num + '月' + str(i) + '日'
        list_month_day.append(str_NUM_NUM)
with open('lexicon.txt', 'a+', encoding='utf-8') as f:
    for item in list_month_day:
        line = item + '\n'
        f.write(line)

# 随机生成时间格式:0点0分
# print('=======list_time=======')
# list_time = []
# for i in range(0, 24):
#     list_time.append(str(i) + '点')
#     list_time.append(str(i) + '时')
#     for clock_m_CN in clock_m_CNs:
#         string = str(i) + '点' + clock_m_CN + '分'
#         list_time.append(string)
#         string = str(i) + '时' + clock_m_CN + '分'
#         list_time.append(string)
#     for m in range(1, 60):
#         string_num = str(i) + '点' + str(m) + '分'
#         list_time.append(string_num)
#         string_num = str(i) + '时' + str(m) + '分'
#         list_time.append(string_num)
#
# for clock_h_CN in clock_h_CNs:
#     list_time.append(clock_h_CN + '点')
#     list_time.append(clock_h_CN + '时')
#     for clock_m_CN in clock_m_CNs:
#         string = clock_h_CN + '点' + clock_m_CN + '分'
#         list_time.append(string)
#         string = clock_h_CN + '时' + clock_m_CN + '分'
#         list_time.append(string)
#     for m in range(1, 60):
#         string_num = clock_h_CN + '点' + str(m) + '分'
#         list_time.append(string_num)
#         string_num = clock_h_CN + '时' + str(m) + '分'
#         list_time.append(string_num)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_time:
#         line = item + '\n'
#         f.write(line)

# 随机生成日期时区时间格式: 昨天上午0点 昨天下午0点 昨天晚上0点
print('=======list_day_zone_time=======')
list_day_zone_time = []
for day in days:
    for i in range(0, 24):
        list_day_zone_time.append(day + str(i) + '点')
        list_day_zone_time.append(day + str(i) + '时')
        for clock_m_CN in clock_m_CNs:
            string = day + str(i) + '点' + clock_m_CN + '分'
            list_day_zone_time.append(string)
            string = day + str(i) + '时' + clock_m_CN + '分'
            list_day_zone_time.append(string)
        for m in range(1, 60):
            string_num = day + str(i) + '点' + str(m) + '分'
            list_day_zone_time.append(string_num)
            string_num = day + str(i) + '时' + str(m) + '分'
            list_day_zone_time.append(string_num)

    for clock_h_CN in clock_h_CNs:
        list_day_zone_time.append(day + clock_h_CN + '点')
        list_day_zone_time.append(day + clock_h_CN + '时')
        for clock_m_CN in clock_m_CNs:
            string = day + clock_h_CN + '点' + clock_m_CN + '分'
            list_day_zone_time.append(string)
            string = day + clock_h_CN + '时' + clock_m_CN + '分'
            list_day_zone_time.append(string)
        for m in range(1, 60):
            string_num = day + clock_h_CN + '点' + str(m) + '分'
            list_day_zone_time.append(string_num)
            string_num = day + clock_h_CN + '时' + str(m) + '分'
            list_day_zone_time.append(string_num)
for day_zone in list_day_zone:
    for i in range(0, 24):
        list_day_zone_time.append(day_zone + str(i) + '点')
        list_day_zone_time.append(day_zone + str(i) + '时')
        for clock_m_CN in clock_m_CNs:
            string = day_zone + str(i) + '点' + clock_m_CN + '分'
            list_day_zone_time.append(string)
            string = day_zone + str(i) + '时' + clock_m_CN + '分'
            list_day_zone_time.append(string)
        for m in range(1, 60):
            string_num = day_zone + str(i) + '点' + str(m) + '分'
            list_day_zone_time.append(string_num)
            string_num = day_zone + str(i) + '时' + str(m) + '分'
            list_day_zone_time.append(string_num)

    for clock_h_CN in clock_h_CNs:
        list_day_zone_time.append(day_zone + clock_h_CN + '点')
        list_day_zone_time.append(day_zone + clock_h_CN + '时')
        for clock_m_CN in clock_m_CNs:
            string = day_zone + clock_h_CN + '点' + clock_m_CN + '分'
            list_day_zone_time.append(string)
            string = day_zone + clock_h_CN + '时' + clock_m_CN + '分'
            list_day_zone_time.append(string)
        for m in range(1, 60):
            string_num = day_zone + clock_h_CN + '点' + str(m) + '分'
            list_day_zone_time.append(string_num)
            string_num = day_zone + clock_h_CN + '时' + str(m) + '分'
            list_day_zone_time.append(string_num)
with open('lexicon.txt', 'a+', encoding='utf-8') as f:
    for item in list_day_zone_time:
        line = item + '\n'
        f.write(line)

# 随机生成月份日期时间格式:三月一日0点 三月1日0点 3月一日0点 3月1日0点
# print('=======list_month_day_time=======')
# list_month_day_time = []
# for month_day in list_month_day:
#     for time in list_time:
#         string = month_day + time
#         list_month_day_time.append(string)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_month_day_time:
#         line = item + '\n'
#         f.write(line)

# 随机生成日期时区格式: 1日上午 一日下午 一日晚上
# print('=======list_day_zone=======')
# list_day_zone = []
# for i in range(1, 32):
#     for day_zone in day_zones:
#         str_num_zone = str(i) + '日' + day_zone
#         list_day_zone.append(str_num_zone)
#
# for day_CN in day_CNs:
#     for day_zone in day_zones:
#         str_CN_zone = day_CN + '日' + day_zone
#         list_day_zone.append(str_CN_zone)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_day_zone:
#         line = item + '\n'
#         f.write(line)

# 随机生成日期时间格式: 1日0点 一日0点 一日0点
# print('=======list_day_time=======')
# list_day_time = []
# for i in range(1, 32):
#     for time in list_time:
#         string = str(i) + '日' + time
#         list_day_time.append(string)
#
# for day_CN in day_CNs:
#     for time in list_time:
#         str_CN_zone = day_CN + '日' + time
#         list_day_zone.append(str_CN_zone)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_day_time:
#         line = item + '\n'
#         f.write(line)

# 随机生成日期时区时间格式: 1日上午0点 一日下午0点 一日晚上0点
# print('=======list_day_zone_time=======')
# list_day_zone_time = []
# for day_zone in list_day_zone:
#     for time in list_time:
#         string = day_zone + time
#         list_day_zone_time.append(string)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_day_zone_time:
#         line = item + '\n'
#         f.write(line)

# 随机生成月份日期时区格式: 三月1日上午 3月1日下午 三月一日晚上
# print('=======list_month_day_zone=======')
# list_month_day_zone = []
# for month_day in list_month_day:
#     for day_zone in day_zones:
#         str_zone = month_day + day_zone
#         list_month_day_zone.append(str_zone)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_month_day_zone:
#         line = item + '\n'
#         f.write(line)

# 随机生成月份日期时区时间格式: 三月1日上午0点 三月1日下午0点 三月1日晚上0点
# print('=======list_month_day_zone_time=======')
# list_month_day_zone_time = []
# for month_day_zone in list_month_day_zone:
#     for time in list_time:
#         string = month_day_zone + time
#         list_month_day_zone_time.append(string)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_month_day_zone_time:
#         line = item + '\n'
#         f.write(line)

# 随机生成年份月份日期格式: 去年三月1日 去年3月1日 去年三月一日
print('=======list_year_month_day=======')
list_year_month_day = []
for year in years:
    for month_day in list_month_day:
        str_year = year + month_day
        list_year_month_day.append(str_year)
with open('lexicon.txt', 'a+', encoding='utf-8') as f:
    for item in list_year_month_day:
        line = item + '\n'
        f.write(line)

# 随机生成年份月份日期时区时间格式: 去年三月1日上午0点 去年三月1日下午0点 去年三月1日晚上0点
# print('=======list_year_month_day_time=======')
# list_year_month_day_time = []
# for year_month_day in list_year_month_day:
#     for time in list_time:
#         string = year_month_day + time
#         list_year_month_day_time.append(string)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_year_month_day_time:
#         line = item + '\n'
#         f.write(line)

# 随机生成年份月份日期时区格式: 去年三月1日上午 去年3月1日下午 去年三月一日晚上
print('=======list_year_month_day_zone=======')
list_year_month_day_zone = []
for year_month_day in list_year_month_day:
    for day_zone in day_zones:
        str_year = year_month_day + day_zone
        list_year_month_day_zone.append(str_year)
with open('lexicon.txt', 'a+', encoding='utf-8') as f:
    for item in list_year_month_day_zone:
        line = item + '\n'
        f.write(line)

# 随机生成年份月份日期时区时间格式: 去年三月1日上午0点 去年三月1日下午0点 去年三月1日晚上0点
# print('=======list_year_month_day_zone_time=======')
# list_year_month_day_zone_time = []
# for year_month_day_zone in list_year_month_day_zone:
#     for time in list_time:
#         string = year_month_day_zone + time
#         list_year_month_day_zone_time.append(string)
# with open('lexicon.txt', 'a+', encoding='utf-8') as f:
#     for item in list_year_month_day_zone_time:
#         line = item + '\n'
#         f.write(line)
