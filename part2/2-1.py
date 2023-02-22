# 엑셀파일 부르기

import pandas as pd

df1=pd.read_excel('./남북한발전전력량.xlsx',engine='openpyxl')

print(df1)
print()

df2=pd.read_excel('./남북한발전전력량.xlsx',engine='openpyxl',header=None)

print(df2)
print()




      
      
      