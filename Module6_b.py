# 1

import pandas as pd

data = pd.read_csv(r'539_m6_datasets_v1.0\Salaries.csv',delimiter=',')

grp = data.groupby('Year')

totalpay1 = sum(grp.get_group(2011)['TotalPayBenefits'])
totalpay2 = sum(grp.get_group(2014)['TotalPayBenefits'])

print('Total salary cost has increased by,',totalpay2-totalpay1 ,'from year 2011 to 2014')

# 2

grp1 = data[data.Year==2014].groupby(['JobTitle'])

means = grp1.mean()
h=dict(means['TotalPayBenefits'])

import operator

max(h.items(),key=operator.itemgetter(1))[0]
max(h.items(),key=operator.itemgetter(1))[1]

print('Title in Year 2014 having highest mean salary of',max(h.items(),key=operator.itemgetter(1))[1] ,'is',max(h.items(),key=operator.itemgetter(1))[0])

# 3

grp = data.groupby('Year')

grp.get_group(2014).sum()['OvertimePay']

print('Money that could have been saved in Year 2014 by stopping OverTimePay is',grp.get_group(2014).sum()['OvertimePay'])

# 4

grp1 = data[data.Year==2014].groupby(['JobTitle'])

means = grp1.mean()

data_sorted = means.sort_index(by='TotalPayBenefits',ascending=False)

top_5 = data_sorted.iloc[:5,6]

h = dict(top_5)

print('Top 5 common job in Year 2014 and how much do they cost SFO is as follows')
i=1
for key,value in h.items():
    print(i,'.',key,':',value)
    i+=1
    
# 5

grp = (data.groupby(['Year','JobTitle']))
means = grp.sum()
h=dict(means['TotalPayBenefits'])

import operator

max(h.items(),key=operator.itemgetter(1))[0]
max(h.items(),key=operator.itemgetter(1))[1]

print('Top earning employee across all years',max(h.items(),key=operator.itemgetter(1))[0][0],'is',max(h.items(),key=operator.itemgetter(1))[0][1],'and the total salary is',max(h.items(),key=operator.itemgetter(1))[1])

# Enhancements for code

# 1
grp1 = data[data.Year==2014].groupby(['JobTitle'])

means = grp1.mean()

data_sorted = means.sort_index(by='TotalPayBenefits',ascending=True)

bot_5 = data_sorted.iloc[:5,6]

h = dict(bot_5)

print('Last 5 common job in Year 2014 and how much do they cost SFO is as follows')
i=1
for key,value in h.items():
    print(i,'.',key,':',value)
    i+=1

# 2
grp = data.groupby('Year')

total_overtime = sum(grp.get_group(2011)['OvertimePay'])
total_pay = sum(grp.get_group(2011)['TotalPayBenefits'])

print('OverTimePay is',(total_overtime/total_pay)*100,'percentage of TotalPayBenefits')

# 3
grp1 = data[data.Year==2014].groupby(['JobTitle'])

means = grp1.mean()
h=dict(means['TotalPayBenefits'])

import operator

min(h.items(),key=operator.itemgetter(1))[0]
min(h.items(),key=operator.itemgetter(1))[1]

print('Title in Year 2014 having lowest mean salary of',min(h.items(),key=operator.itemgetter(1))[1] ,'is',min(h.items(),key=operator.itemgetter(1))[0])
    
