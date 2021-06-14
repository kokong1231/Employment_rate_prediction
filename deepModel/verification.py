# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense

import pandas as pd

import numpy as np
import tensorflow as tf


seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)            # tensorflow에서 초기값은 주로 랜덤값을 사용하고 결과값을 고정하기 위해 seed를 고정

model = Sequential()        # 모델 구성
model.add(Dense(30, input_dim=10, activation='sigmoid'))    # 학습 항목은 총 10개 합격과 불합격 여부를 확인해야 하기 때문에
model.add(Dense(1, activation='sigmoid'))                   # sigmoid를 사용한 학습

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])    # 모델 엮기
hist = model.fit(X, Y, epochs=300, batch_size=10)   # 모델 학습 약 250~300번 정도에서 정확도 변화가 줄어들기 때문에 300으로 지정

print("\n Accuracy: %.2f%%" % (model.evaluate(X, Y, batch_size=253)[1]))    # 모델 평가

test_a = np.loadtxt("../Dataset/a.csv", delimiter=",")
test_b = np.loadtxt("../Dataset/b.csv", delimiter=",")
test_c = np.loadtxt("../Dataset/c.csv", delimiter=",")
test_d = np.loadtxt("../Dataset/d.csv", delimiter=",")
test_e = np.loadtxt("../Dataset/e.csv", delimiter=",")
test_f = np.loadtxt("../Dataset/f.csv", delimiter=",")
test_g = np.loadtxt("../Dataset/g.csv", delimiter=",")
test_h = np.loadtxt("../Dataset/h.csv", delimiter=",")
test_i = np.loadtxt("../Dataset/i.csv", delimiter=",")
test_j = np.loadtxt("../Dataset/j.csv", delimiter=",")

tesa = test_a[:,1:11]
tesb = test_b[:,1:11]
tesc = test_c[:,1:11]
tesd = test_d[:,1:11]
tese = test_e[:,1:11]
tesf = test_f[:,1:11]
tesg = test_g[:,1:11]
tesh = test_h[:,1:11]
tesi = test_i[:,1:11]
tesj = test_j[:,1:11]

f = yhat * 100

compare_data = model.predict(X)      # 비교하기 위한 데이터
f_f = compare_data * 100
save = []           # 비슷한 학생의 취업가능성 배열로 저장
save_index = []     # 비슷한 학생의 스팩의 인덱스 값 저장
index_count = 0     # 인덱스 값 초기화
count = 0           # 10명의 학생에 대한 카운터

for x in f_f:                           # 수집한 데이터에서 취업 가능성이 +-5 근처인 학생을 찾기
    if (float(x) - 5) <= float(f[count]) <= (float(x) + 5):
        save.append(x)
        save_index.append(index_count)
        count += 1

        if count == 10:
            break

    index_count += 1

for i in range(10):
    print("\n %d 번째 학생의 취업가능성 : %.2f%%" %(i+1, f[i]), "\n --비슷한 스팩의 학생 취업가능성 : %.2f%%" % (save[i]))
    print(Data_set[save_index[i]])          # 비슷한 학생의 스팩 출력
    print("비슷한 학생의 스팩")

list_test = [tesa, tesb, tesc, tesd, tese, tesf, tesg, tesh, tesi, tesj]
ddd = 0
sumsum = 0

for y in list_test:
    t_data = model.predict(y)
    test = t_data * 100
    ddd += 1

    print("=============", ddd, "=============")

    for te in range(20):
        print("\n %d 번째 : %.2f%%" % (te + 1, test[te]))
        sumsum += test[te]

    average_s = int(sumsum / 10)
    ttemp = average_s * 10
    tttemp = sumsum - ttemp
    ttttemp = tttemp / 10

    print('===================================')
    print('avg : ', average_s)
    print('t : ', int(tttemp))
    print(ttttemp)
    sumsum = 0
