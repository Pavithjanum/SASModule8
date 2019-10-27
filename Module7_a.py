import pandas as pd

#1
df1 = pd.DataFrame({'float_col':[0.1,0.2,0.2,10.1,None],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}) 

#2
df2 = df1.ix[:,['float_col','int_col']]

print(df2)

df2 = df1.loc[:,['float_col','int_col']]

print(df2)
print(df1[:][['float_col','int_col']])

#3
df3 = df2[df2['float_col']>0.15]

print(df3)

df4 = df2[df2['float_col']==0.1]

print(df4)

#4
df5 = df2[(df2['float_col']>0.1)&(df2['int_col']>2)]

print(df5)

#5
df6 = df2[(df2['float_col']>0.1)|(df2['int_col']>2)]

print(df6)

#6
df7 = df2[~(df2['float_col']>0.1)]

print(df7)

#7

df8 = df2.copy()

df8.rename(columns={'int_col':'new_name'},inplace=True)

print(df8)

#8
df7.rename(columns={'int_col':'new_name'},inplace=True)

print(df7)

#9
df2.drop(df2.index[df2['float_col'].isna()],inplace=True)

print(df2)

 

#10

df1['float_col'] = df1['float_col'].fillna(df1['float_col'].mean())
print(df1)

#11
df1['str_col'] = df1['str_col'].apply(lambda x:'map_'+x if x!=None else None)

df1.drop(df1.index[df1['str_col'].isna()],inplace=True)

print(df1)

#12

grp = df1.groupby('str_col')

grp.mean()['float_col']

#13

df1.cov()

#14

df1.corr()

#15 

x = pd.DataFrame({'float_col':[0.1,0.2,0.2,10.1,None],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}) 

other = pd.DataFrame({'some_val':[1,2],'str_col':['a','b']})

print(other)

print(pd.merge(x,other,how='inner',on='str_col'))

print(pd.merge(x,other,how='outer',on='str_col'))

print(pd.merge(x,other,how='left',on='str_col'))

print(pd.merge(x,other,how='right',on='str_col'))


#16

import os

os.getcwd()

os.chdir(r'C:\Users\376020\Desktop\Masters\Python\Module7')

with open('body.txt','r') as body:

    temp = body.read().splitlines()

with open('names.txt','r') as f1:

    data=f1.read().splitlines()

    for name in data:

        temp1=name.split(' ')

        fname = temp1[0]+'.txt'

        print(fname)

        with open(fname,'a') as out:

            outc = 'Hello '+temp1[0]+' '+temp[0]

            out.write(outc)
