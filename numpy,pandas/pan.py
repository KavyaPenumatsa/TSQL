import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,5,6,np.nan,8,9,10])
print(s)

d = pd.date_range('20211101',periods=10)

df = pd.DataFrame(np.random.rand(10,4),index = d,columns= ['A','B','C','D'])

df1 = pd.DataFrame({'A':[1,2,3,4],
                   'B':pd.Timestamp('20211102'),
                   'C':pd.Series(1,index=list(range(4)), dtype='float32'),
                   'D':np.array([5]*4,dtype='int32'),
                   'E':pd.Categorical(['true','false','true','false']),
                   'F': 'Kavya'})
print(df1)
print(df.describe())
df.sort_index
print(df.head())
print(df.tail())
print(df.index)
print(df.columns)
print(df.to_numpy())
print(df.sort_index(axis=1,ascending=False))
print(df.sort_values(by='C'))
print(df['C'])
print(df[0:3])
print(df.loc[d[0]])
print(df.loc['2021-11-05 ':'2021-11-10 ',['A' , 'C']])
print(df.at[d[0],'C'])
print(df.iloc[3:5 , 0:2])
print(df['A']> 0)
df2 = df.reindex(index=d[0:4],columns = list(df.columns) + ['E'])
df2.loc[d[0]:d[1], 'E'] = 1
print(df2.isnull())
print(df2.dropna())
print(df2)
print(df2.fillna(value=2))
print(pd.isna(df2))
print(df.mean(1))

s = pd.Series([1,2,3,np.nan,4,5,6,7,8,9],index = d).shift(2)
print(s)
print(df.sub(s,axis='index'))
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))
print(s.value_counts())
s = pd.Series(['Kavya' , 'Python' , 'Pycharm' , np.nan , 'cricket ' , 'world'])
print(s.str.lower())
df3 = pd.DataFrame(np.random.randn(10,4))
print(df3)
df4 = [df3[:3], df[3:7], df[7:]]


print(pd.concat(df4))
left = pd.DataFrame({'A': [1,2], 'B': [3,4]})
right = pd.DataFrame({'A': [3,2], 'D': [4,5]})
print(left)
print(pd.merge(left , right ,on ='A'))
print(df)
print(df.groupby('A').sum())
