#5. Perform Operations on Files

#5.1 From the raw data below create a data frame

import pandas as pd
df = pd.DataFrame({'first_name'    : ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                   'last_name'     : ['Miller', 'Jacobson',None, 'Milner', 'Cooze'],
                   'age'           : [42, 52, 36, 24, 73],
                   'preTestScore'  : [4, 24, 31, None, None],
                   'postTestScore' : ["25,000", "94,000", 57, 62, 70]})
print(df)

#5.2 Save the dataframe into a csv file as example.csv

df.to_csv(r'example.csv',sep=',',index=False)

#5.3 Read the example.csv and print the data frame

data = pd.read_csv(r'example.csv',delimiter=',')

print(data)

#5.4 Read the example.csv without column heading

data = pd.read_csv(r'example.csv',delimiter=',',skiprows=1,header=None)

print(data)

#5.5 Read the example.csv and make the index columns as 'First Name’ and 'Last Name'

data = pd.read_csv(r'example.csv',delimiter=',')

data.rename(index={0:'First Name',1:'Last Name'},inplace=True)

data.rename(columns={'first_name':'First Name','last_name':'Last Name'},inplace=True)

print(data)

#5.6 Print the data frame in a Boolean form as True or False. True for Null/ NaN values and false for non-null values

data.isna()

#5.7 Read the dataframe by skipping first 3 rows and print the data frame

data = pd.read_csv(r'example.csv',delimiter=',',skiprows=4,header=None)

print(data)

#5.8 Load a csv file while interpreting "," in strings around numbers as thousands seperators. Check the raw data 'postTestScore' column has, as thousands separator.
# Comma should be ignored while reading the data. It is default behaviour, but you need to give argument to read_csv function which makes sure commas are ignored.

data = pd.read_csv(r'example.csv',delimiter=',',thousands=r',')

print(data)

#6

#6.1 From the raw data below create a Pandas Series

import numpy as np
import pandas as pd

data = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])

#a. Print all elements in lower case
print(data.str.lower())

#b. Print all the elements in upper case
print(data.str.upper())

#c. Print the length of all the elements
print(data.str.len())

#6.2 From the raw data below create a Pandas Series

data = pd.Series(['Atul', 'John ', ' jack ', 'Sam'])
 
#a. Print all elements after stripping spaces from the left and right
print(data.str.strip())

#b. Print all the elements after removing spaces from the left only
print(data.str.lstrip())

#c. Print all the elements after removing spaces from the right only
print(data.str.rstrip())

#6.3 Create a series from the raw data

data = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])

#a. split the individual strings wherever ‘_’ comes and create a list out of it.
list1= data.str.split('_')

#b. Access the individual element of a list
for item in list1:
    print(item)
    
#c. Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements

list2 = data.str.split('_',expand=True)

print(list2)
type(list2)

#6.4 Create a series and replace either X or dog with XX-XX

data = pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])

import re
c = re.compile(r'(X)|(dog)')

print(data.str.replace(c,'XX-XX'))

#6.5 Create a series and remove dollar from the numeric values

data = pd.Series(['12', '-$10', '$10,000'])

print(data.str.replace('$',''))

#6.6 Create a series and reverse all lower case words

data = pd.Series(['india 1998', 'big country', np.nan])

print(data.str[::-1])

#6.7 Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.

data = pd.Series(['1', '2', '1a', '2b', '2003c@'])

print(data.str.isalnum())

#6.8 Create pandas series and print true if value is containing ‘A’

data = pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])

print(data.str.lower().str.contains('a'))

print(data.str.contains('A'))

#6.9 Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values

data = pd.Series(['a', 'a|b', np.nan, 'a|c'])

c = re.compile(r'(a)|(b)|(c)')

print(data.str.contains(c))

#6.10 Create pandas dataframe having keys and ltable and rtable

df1 = pd.DataFrame({'key': ['One', 'Two'], 'ltable': [1, 2] })

df2 = pd.DataFrame({'key': ['One', 'Two'], 'rtable': [4, 5]})

pd.merge(df1,df2,on='key',how='inner')



