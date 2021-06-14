# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv('../Dataset/datalog.csv')

col_list = ['학점', '토익', '토스', 'OPIC', '외국어', '해외경험', '인턴', '수상경력']

#  ["Index","학점", "토익", "토스", "OPIC", "외국어", "자격증", "해외경험", "인턴", "수상경력","봉사","합격여부"]
#  Index,학점,토익,토스,OPIC,외국어,자격증,해외경험,인턴,수상경력,봉사,합격여부
#  index,grades,toeic,tos,opic,foreign_lang,certificate,foreign_exp,intern,prize,volunteer,label

grades_list = []
toeic_list = []
tos_list = []
opic_list = []
foreignl_list = []
certificate_list = list(data['자격증'])
foreigne_list = []
intern_list = []
prize_list = []
volunteer_list = list(data['봉사'])
label = list(data['합격여부'])

all_save = []

for x in col_list:

    if x == '학점':
        for y in data[x]:
            if y >= 3.0:
                grades_list.append(1)
            else:
                grades_list.append(0)

    elif x == '토익':
        for y in data[x]:
            if y >= 600:
                toeic_list.append(1)
            else:
                toeic_list.append(0)

    elif x == '토스':
        for y in data[x]:
            if y:
                tos_list.append(1)
            else:
                tos_list.append(0)

    elif x == 'OPIC':
        for y in data[x]:
            if y:
                opic_list.append(1)
            else:
                opic_list.append(0)

    elif x == '외국어':
        for y in data[x]:
            if y:
                foreignl_list.append(1)
            else:
                foreignl_list.append(0)

    elif x == '해외경험':
        for y in data[x]:
            if y:
                foreigne_list.append(1)
            else:
                foreigne_list.append(0)

    elif x == '인턴':
        for y in data[x]:
            if y:
                intern_list.append(1)
            else:
                intern_list.append(0)

    elif x == '수상경력':
        for y in data[x]:
            if y:
                prize_list.append(1)
            else:
                prize_list.append(0)

all_save.append(grades_list)
all_save.append(toeic_list)
all_save.append(tos_list)
all_save.append(opic_list)
all_save.append(foreignl_list)
all_save.append(certificate_list)
all_save.append(foreigne_list)
all_save.append(intern_list)
all_save.append(prize_list)
all_save.append(volunteer_list)
all_save.append(label)

re_data = pd.DataFrame(all_save)
re_data = re_data.transpose()

re_data.to_csv('../Dataset/optmiz_data.csv')