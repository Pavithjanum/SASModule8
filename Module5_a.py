# Module5 Data Visualization

#1 You are given a dataset, which is present in the LMS, containing the number of hurricanes occurring in the United States along the coast of the Atlantic. Load the data from the dataset into your program and plot a Bar Graph of the data, taking the Year as the x-axis and the number of hurricanes occurring as the Y-axis.

import pandas as pd
hurricanes_analysis = pd.read_csv(r'Hurricanes.csv')

hurricanes_analysis.info()

hurricanes_analysis.describe()
hurricanes_analysis.head()

import matplotlib.pyplot as plt

plt.bar(hurricanes_analysis['Year'],hurricanes_analysis['Hurricanes'])
plt.title('Hurricane analysis in united states')
plt.xlabel('Year')
plt.ylabel('Number of Hurricanes')

plt.show()

#2 The dataset given, records data of city temperatures over the years 2014 and 2015. Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.

import pandas as pd
import matplotlib.pyplot as plt

city_temp_analysis = pd.read_csv(r'539_m5_datasets_v1.1\CityTemps.csv')

city_temp_analysis.info()
city_temp_analysis.describe()
city_temp_analysis.head()
plt.hist(city_temp_analysis['San Francisco'],bins=50,label='San Francisco',alpha=0.5,color='G',ls='dotted',lw=2)
plt.hist(city_temp_analysis['Melbourne'],bins=50,label='Melbourne',alpha=0.5,color='B',ls='dashed',lw=2)
plt.legend()
plt.show()

#3 Plot a pie-chart of the number of models released by every manufacturer, recorded in the data provide. Also mention the name of the manufacture with the largest releases.

import pandas as pd
import matplotlib.pyplot as plt

cars2015_analysis =  pd.read_csv(r'Cars2015.csv')
cars2015_analysis.info()
cars2015_analysis.describe()
cars2015_analysis.tail()

grp = cars2015_analysis.groupby('Make')
lp = grp.describe() ['LowPrice']
lp.info()

dict_data = dict(lp['count'])
plt.figure(figsize=(30,30))
plt.pie(dict_data.values(),labels=dict_data.keys())
#plt.legend()
plt.axis('equal')
plt.tight_layout()
plt.show()

import operator
max_make = max(dict_data.items(), key=operator.itemgetter(1))[0]

print('The manufacture with the largest releases is ',max_make)

#4 Create csv file from the unstructured data and read in pandas data frame

import matplotlib.pyplot as plt
# Phase 1 -Reading Data
import pyperclip

## copy the contents before by using ctrl+a and ctrl+c
a = (pyperclip.paste())
type(a)
li = []
li = a.split('\n')

with open(r'Shopdetails.csv', 'w+') as csvfile:
    for j in li:
        csvfile.write(j)

import pandas as pd

csv_data = pd.read_csv(r'Shopdetails.csv')
csv_data.info()
csv_data.head()

# Phase 2 –Describe the data
csv_data.describe()['net_price']

# Phase 3 –filter the data
shop_details = pd.DataFrame()

shop_details['name'] = csv_data['name']
shop_details['net_price'] = csv_data['net_price']
shop_details['date'] = csv_data['date']

grp = shop_details.groupby('name')

hj = grp.describe()['net_price']

hj.info()

dict_data = dict(hj['count'])
plt.figure(figsize=(30,30))
plt.bar(dict_data.keys(), dict_data.values())
plt.grid(True)
plt.xticks(rotation=70)
plt.xlabel('Customer name')
plt.ylabel('Total Sales')
plt.show()

#5 Let the x axis data points and y axis data points are
##X = [1,2,3,4] y = [20, 21, 20.5, 20.8]
##5.1: Draw a Simple plot
##5.2: Configure the line and markers in simple plot
##5.3: configure the axes
##5.4: Give title of Graph & labels of x axis and y axis
##5.5: Give error bar if y_error = [0.12, 0.13, 0.2, 0.1]
##5.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100
##5.7: Give a font size of 14
##5.8: Draw a scatter graph of any 50 random values of x and y axis
##5.9: Create a dataframe from following data
##'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
##'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
##'female': [0, 1, 1, 0, 1],
##'age': [42, 52, 36, 24, 73],
##'preTestScore': [4, 24, 31, 2, 3],
##'postTestScore': [25, 94, 57, 62, 70]
##Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
##5.10: Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore with the size = 300 and the color determined by sex

import matplotlib.pyplot as plt
X = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

plt.plot(X,y)
#plt.show()

plt.plot(X,y,'--',marker='*')

plt.xlim(0.5,4.0)
plt.ylim(5,40)

plt.title('Simple Plot')
plt.xlabel('X data points')
plt.ylabel('Y data points')
plt.errorbar(X,y,yerr=[0.12, 0.13, 0.2, 0.1],marker='*',ls='--')


plt.figure(figsize=(4,5),dpi=100)
plt.rcParams.update({'font.size': 14})
plt.show()

import matplotlib.pyplot as plt
import numpy as np
n = np.random.randn(50)
m= np.random.randn(50)

plt.scatter(n,m)
plt.show()

fg = pd.DataFrame()
fg['first_name'] = ['Jason', 'Molly', 'Tina', 'Jake', 'Amy']
fg['last_name'] = ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze']
fg['female'] = [0, 1, 1, 0, 1]
fg['age'] = [42, 52, 36, 24, 73]
fg['preTestScore'] = [4, 24, 31, 2,3]
fg['postTestScore'] = [25, 94, 57, 62, 70]

print(fg)

plt.scatter(fg['preTestScore'],fg['postTestScore'],s=fg['age'])

plt.show()

plt.scatter(fg['preTestScore'],fg['postTestScore'],s=300,c=fg['female'])

plt.show()
