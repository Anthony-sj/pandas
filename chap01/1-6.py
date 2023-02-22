# 열제거
import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data,index=['서준', '우현', '인아'])

print(df)
print('-------------------')

print()
'''
df4=df.copy()
print(df4)

df4.drop('수학',axis=1,inplace=True) # axis=0 (행) / axis=1 (열)

print(df4)
'''

df5=df.copy()

df5.drop(['영어', '음악'],axis=1,inplace=True)

print(df5)