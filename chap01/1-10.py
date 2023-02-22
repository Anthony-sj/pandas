# 원소 선택

import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data)

# print(df)
# print()



print(df)
print()

# c=df.loc['서준',['음악','체육']]

# print(c)
# print(type(c))

# d=df.iloc[0,[2,3]]
# print(d)
# print(type(d))

e=df.loc['서준','음악':'체육']
f=df.iloc[0,2:3]
print(e)
print()
print(f)

'''


a=df.loc['서준','음악'] #a=df.loc[행인덱스,열인덱스] 
print(a)
print()

b=df.iloc[0,2]
print(b)
'''