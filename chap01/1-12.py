# 열 추가

import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data)

print(df)
print('===========================================')


df['국어'] = 80
df['미술'] = 90

print(df)

#행 추가

print('행 추가')

df.loc[3]=0
# print(df)

df.loc[4] = ['동규',90,80,70,60,70,90]
# print(df)

df.loc['행5']= df.loc[3]
print(df)