# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense

import pandas as pd

import numpy as np
import tensorflow as tf



seed = 0
np.random.seed(seed)
tf.random.set_seed(3)            # tensorflow에서 초기값은 주로 랜덤값을 사용하고 결과값을 고정하기 위해 seed를 고정

Data_set = pd.read_csv("../Dataset/datalabel.csv", encoding='utf-8')    # 취업 관련 항목 데이터 모음
New_set = pd.read_csv("../Dataset/testdata.csv", encoding='utf-8')         # 합격 여부를 알고 싶은 데이터
data_column = Data_set.columns
New_column = New_set.columns

X = Data_set[data_column[0:-1]]        # 인덱스를 제외한 속성부분을 지정
Y = Data_set[data_column[-1]]          # 합격여부를 가르키는 클래스 부분
new_data = New_set[New_column[0:10]]  # 합격 여부를 알고 싶은 데이터의 속성

model = Sequential()
model.add(Dense(300, input_dim=10, activation='sigmoid'))
model.add(Dense(260, activation='relu'))
model.add(Dense(230, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(170, activation='relu'))
model.add(Dense(150, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(80, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])    # 모델 엮기
hist = model.fit(X, Y, epochs=1200, batch_size=100)   # 모델 학습 약 250~300번 정도에서 정확도 변화가 줄어들기 때문에 300으로 지정

print("\n Accuracy: %.2f%%" % (model.evaluate(X, Y, batch_size=100)[1] * 100))    # 모델 평가

model.predict(new_data)        # 학습이 완료된 모델 사용

#  model.save('./model.h5')

'''
fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()
'''