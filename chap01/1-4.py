# 데이터 프레임 행/열이름 변경
import pandas as pd

# df1 = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], #2차원 배열
#                    # index=['준서', '예은'], # 행 인덱스 배열
#                    # columns=['나이', '성별', '학교'])  #열 이름 배열
#                    )
# print(df1)

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], #2차원 배열
                   index=['준서', '예은'], # 행 인덱스 배열
                   columns=['나이', '성별', '학교'])  #열 이름 배열
# print(df)
print('-----------------')
df.rename(columns={'나이':'연령'},inplace=True)
df.rename(index={'준서':'학생1'},inplace=True)

print(df)
# print(df.index)
# print(df.columns)

# df.index=['학생1','학생2']
# df.columns = ['연령', '남녀', '소속']

# print(df)
# print(df.index)
# print(df.columns)