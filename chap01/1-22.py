import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]

print(df.tail())
print()

addition=df+10

print(addition.tail())
print()

subtaction=addition-df
print(subtaction.tail())




