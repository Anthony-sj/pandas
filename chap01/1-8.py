# 열 선택

import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data,index=['서준', '우현', '인아'])

print(df)
print()
math1=df['수학']
print(math1)
print()
print(type(math1))

english=df.영어 # 추천하지 않는 방법
print(english)
print()
print(type(english))
