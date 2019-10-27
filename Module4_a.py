# 1
# Extract data from the given CSV file and store the data from each column in a separate NumPy array

import numpy as np
arr1 = np.genfromtxt(r'SalaryGender.csv',delimiter=',')

# print(arr1)
# print(type(arr1))
# print(arr1.shape)

salary = arr1[1:,0]
gender = arr1[1:,1]
age    = arr1[1:,2]
phd    = arr1[1:,3]

# 2
# Find: 1. The number of men with a PhD 2. The number of women with a PhD

print()

#count=0

a = [1 for item in arr1 if (item[1]==1 and item[3]==1)]
a = np.array(a)
print('The number of men with a PhD is ',a.sum())

#
# for item in arr1:
#     if item[1] ==1 and item[3] == 1:
#         count+=1

#print(count)

b = [1 for item in arr1 if (item[1]==0 and item[3]==1)]
b=np.array(b)
print('The number of women with a PhD is ',b.sum())

# 3
# Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD

import pandas as pd

df1 = pd.Series(age,dtype=int)
print(df1)

df2 = pd.Series(phd,dtype=int)
print(df2)

df3 = pd.DataFrame({'Age':df1,'PhD':df2})
print(df3)

df3.drop(df3[df3['PhD']==0].index,inplace=True)
print(df3)

df4=pd.DataFrame()
df4=df4.append(df3,ignore_index=True)
print(df4)

# 4
# Calculate the total number of people who have a PhD degree.

print('Total number of people who have a PhD degree is ',len(df4))

# 5
# How do you Count The Number Of Times Each Value Appears In An Array Of Integers?
# [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
# Answer should be array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1]) which means 0 comes 4 times, 1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so on.

import numpy as np

ab = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
print(ab)
bc = sorted(ab,reverse=False)
print(bc)

count_items = [[i,bc.count(i)] for i in set(bc)]
print(count_items)

x = [(str(j[0])+' comes '+str(j[1])+' times') for j in count_items ]
print(x)

print(','.join(x))

# 6
# Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements greater than 5.

import numpy as np
fg = np.array([[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]])
print(fg[fg>5])

# 7
# Create a numpy array having NaN (Not a Number) and print it.
# array([ nan, 1., 2., nan, 3., 4., 5.])
# Print the same array omitting all elements which are nan

import numpy as np
jk = np.array(['NaN', 1., 2.,'NaN', 3., 4., 5.])
print(jk[jk!='NaN'])

# 8
# Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np
lp = np.empty([10,10],dtype=int)
print(lp.shape)
print(lp.max(),' is the maximum value and ',lp.min(),' is the minimum value.')

# 9
# Create a random vector of size 30 and find the mean value.

import numpy as np
op = np.empty(30,dtype=int)
print(op.shape)
print(op)
print(op.mean())

# 10
# Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9

import numpy as np
# nl = np.arange(0,11)
# print(nl[(nl<3)|(nl>9)])
print(np.arange(0,11)[(np.arange(0,11)<3)|(np.arange(0,11)>9)])

# 11
# Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column.

import numpy as np

arr = np.empty([3,3],dtype=int)
print(arr)

import pandas as pd
df1 = pd.DataFrame(arr)
print(df1)

print(df1.sort_values(0))
print(df1.sort_values(1))
print(df1.sort_values(2))

# 12
# Create a four dimensions array get sum over the last two axis at once.

import numpy as np

kl = np.empty([4,4],dtype=int)
print(kl)

print(kl[2]+kl[3])

# 13
# Create a random array and swap two rows of an array.
print('ínverse')
import numpy as np

yh=np.empty([2,4],dtype=int)
print(yh)

yh[[0,1]] = yh[[1,0]]
print(yh)

# 14
# Create a random matrix and Compute a matrix rank.

import numpy as np
ju = np.empty([3,5],dtype=int)

print(np.linalg.matrix_rank(ju))

# 15
#

#### Phase 1 - Data Collection
# Read the data in pandas data frame
import pandas as pd
data = pd.read_csv(r'middle_tn_schools.csv',delimiter=',')

print(data)

# Describe the data to find more details
print(data.describe())
print(data.info())
print(data.head())


#### Phase 2 - Group data by school ratings

grouped_data = data.groupby('school_rating')

print(grouped_data)

print(grouped_data.describe()['reduced_lunch'])
print(grouped_data.describe()['stu_teach_ratio'])

#### Phase 3 – Correlation analysis
print(data.corr())
print(data.corrwith(other=data['school_rating']))

print(data['reduced_lunch'].corr(data['school_rating']))

#### Phase 4 – Scatter Plot
data.plot(kind='scatter',x='reduced_lunch',y='school_rating',label='name',color='darkgreen')

#### Phase 5 – Correlation Matrix
import matplotlib.pyplot as plt
plt.interactive(False)
corr = data.corr()
import seaborn as sns
sns.heatmap(corr,xticklabels=corr.columns, yticklabels=corr.columns,annot=True,cmap='coolwarm')
