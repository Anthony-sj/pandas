# 리스트 시리즈 변환 (정수인덱스 부여) pd.Series(list)
import pandas as pd

list_data = ['2019-01-02', 3.14, 'abc', 100, True]

sr=pd.Series(list_data)

print(sr)

idx=sr.index

val=sr.values

print(idx)
print()
print(val)