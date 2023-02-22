# 범위 데이터프레임 선택

import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)

print(df)
print()

g = df.loc[['서준','우현'],['음악','체육']]
print(g)
print()

h = df.iloc[[0,1],[2,3]]
print(h)
print()

i = df.loc['서준':'우현','음악':'체육']
print(i)
print()

j = df.iloc[0:1+1,2:3+1]
print(j)
print()

