# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv('../Dataset/datalog.csv')

print(data['label'].value_counts())

'''
1    336
0    296
Name: label, dtype: int64
'''