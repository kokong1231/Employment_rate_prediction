from keras.models import load_model
import pandas as pd


model = load_model('./model.h5')
new_set = pd.read_csv("../Dataset/testdata.csv", encoding='utf-8')    # 취업 관련 항목 데이터 모음

data_column = new_set.columns
new_data = new_set[data_column[0:10]]  # 합격 여부를 알고 싶은 데이터의 속성

value = model.predict_classes(new_data)

for x in range(16):
    print(x+1, '=', 'Predict : ' + str(value[x]))