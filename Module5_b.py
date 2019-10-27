# Module 5: Data Visualisation

import pandas as pd
import matplotlib.pyplot as plt

bigmart_data = pd.read_csv(r'BigMartSalesData.csv')

bigmart_data.info()


# 1. Plot Total Sales Per Month for Year 2011. How the total sales have increased
# over months in Year 2011. Which month has lowest Sales?

bigmart_data = bigmart_data[bigmart_data['Year']== 2011]

grp = bigmart_data.groupby(['Month'])

temp = grp.describe() ['Quantity']


plt.figure(figsize=(10,10))
plt.xlim(0,13)

plt.plot(temp['count'])

plt.xlabel('Months in Year 2011')
plt.ylabel('Total Sales per month')
plt.title('BigMart Sales')
plt.legend()
plt.show()

# 2. Plot Total Sales Per Month for Year 2011 as Bar Chart. Is Bar Chart Better to
# visualize than Simple Plot?

bigmart_data = bigmart_data[bigmart_data['Year']== 2011]

grp = bigmart_data.groupby(['Month'])

temp = grp.describe() ['Quantity']

print(temp)

bigmart_dict = dict(temp['count'])

plt.figure(figsize=(10,10))
plt.xlim(0,13)

#plt.plot(bigmart_dict.keys(),bigmart_dict.values())

for i, key in enumerate(bigmart_dict,start=1):
    plt.bar(i,bigmart_dict[key],label='Month '+str(i))

plt.xlabel('Months in Year 2011')
plt.ylabel('Total Sales per month')
plt.title('BigMart Sales')
plt.legend()
plt.show()

# 3 Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest
#towards sales?
bigmart_dict = dict(temp['count'])
plt.pie(temp['count'],labels=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'])
plt.title('BigMart Sales')
plt.show()

# 4 Plot Scatter Plot for the invoice amounts and see the concentration of amount.
#In which range most of the invoice amounts are concentrated

plt.scatter(bigmart_data['Month'],bigmart_data['Amount'])
plt.show()

## Enhancements for code

# Change the bar chart to show the value of bar

for i, key in enumerate(bigmart_dict,start=1):
    plt.bar(i,bigmart_dict[key],label='Month '+str(i))
    
plt.xlabel('Months in Year 2011')
plt.ylabel('Total Sales per month')
plt.title('BigMart Sales')

plt.legend()
plt.show()

# In Pie Chart Play With Parameters shadow=True, startangle=90 and see how
# different the chart looks

bigmart_dict = dict(temp['count'])
plt.pie(temp['count'],labels=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'],shadow=True,startangle=90)
plt.title('BigMart Sales')
plt.show()

# In scatter plot change the color of Scatter Points

plt.scatter(bigmart_data['Month'],bigmart_data['Amount'],c=bigmart_data['Month'])
