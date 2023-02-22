# 데이터 프레임 연산
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]

print(df.head()) # 첫 ()행만 표시 디폴트=5행
print()

addition=df+10 # 모든 원소에 더해짐
print(addition.head())




