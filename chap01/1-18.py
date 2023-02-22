# 행 인덱스를 기준으로 데이터 프레임 정렬

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df=pd.DataFrame(dict_data,index=['r0','r1','r2'])

print(df)
print()

ndf2=df.sort_values(by='c1',ascending=False)
# ndf2=df.sort_values(by=['c1','c2'],ascending=False)
print(ndf2)

# ndf=df.sort_index(ascending=False) # 내림차순
# print(ndf)
# print()

# ndf1=df.sort_index(ascending=True) # 오름차순
# print(ndf1)