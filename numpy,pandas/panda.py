import numpy as np
import pandas as pd

my_tuple = list(zip(*[[1,2,3,4,5,17,18,19],[11,12,13,6,7,8,9,10]]))
index = pd.MultiIndex.from_tuples(my_tuple,names = ['First','Second'])
df = pd.DataFrame(np.random.randn(8,2), index = index , columns = ['A','B'])
df2 = df[:4]
print(df2)
a = df2.stack()
a = df2.unstack()
print(a)
df = pd.DataFrame({'A':['a','b','c','d'] * 3,
                   'B': ['A','B','C'] * 4,
                   'C': ['P' ,'P', 'P','Q','Q','Q'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)
print(pd.pivot_table(df,values='D',index=['A','B'], columns = ['C']))

dates = pd.date_range('3/3/2020',periods = 100,freq ='S')
ts = pd.Series(np.random.randint(0,500,len(dates)),index=dates)
print(ts)
ts.resample('5min').sum()
dates = pd.date_range('3/3/2020',periods = 5,freq ='S')
ts = pd.Series(np.random.randn(len(dates)),dates)
print(ts)
ts_utc = ts.tz_localize('UTC')
print(ts_utc)
print(ts_utc.tz_convert('US/Eastern'))
dates = pd.date_range('3/3/2020',periods = 5,freq ='M')
ts = pd.Series(np.random.randn(len(dates)),dates)
print(ts)
ps = ts.to_period()
print(ps)
print(ps.to_timestamp())
df1 = pd.DataFrame({'id': [1,2,3,4,5,6],
                    'grade': ['a','b','c','b','a','e']})
print(df1)
df['Grade'] = df['grade'].astype("category")
df['Grade'].cat.categories = ["good" ,'very bad', 'very good', 'excellent']
df['Grade'] = df['Grade'].cat.set_categories(["good" ,"very bad", "very good", "excellent",
                                              "medium"])
print(df['Grade'])