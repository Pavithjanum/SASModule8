#1
#Load the required libraries and the data

library(dplyr)

data <- read.csv('C:\\Users\\PAVI\\Desktop\\Edureka\\R Certification\\Module\\Module4\\housingdata_v2.0.csv')

data

# 2. 
# Understand the data structure and provide concise summary on the following – 
# • no of observations 
# • total number of variables 
# • number of continuous variables 
# • number of categorical variables

str(data)

# 3. 
# Select and Mutate : use the select() and mutate() functions in R to answer the following  
# • Select the columns Gender, Education, and Income and print the first five rows 
# • Select the columns from Gender to Loan Period and print the first five rows 
# • Be concise! - select columns by removing Record Column and Gender and print the first five rows 
# • Use mutate() function to add the new variables var1 which calculates the ratio of property value to total income
# and save the result as g1. Print the first five rows
# • Add the new variable var2 which returns the ratio of property value to loan period and save the result as g2
# Print the first five rows

data[1:5,]  %>% select(Gender,Education,Income)

data[1:5,]  %>% select(Gender:Loan_Period)

(data[-1:-2]) [1:5,]

g1 <- mutate(data,var1=PropertyValue/Income)

g1[1:5,]

g2 <- mutate(g1,var2=PropertyValue/Loan_Period) 

g2[1:5,]

# 4. 
# Filter and Arrange:  
# • Filter all the observations that have Property Value lower than 80000 or higher than 150000 
# and store it in df g3. Print the first five rows. How many observations are there. 
# • Filter all the observations that have Property Value > 1000000 and Income < 3185 and store it in df g4. 
# Print the first five rows. How many observations are there. 
# • Filter all observations where Income < 3185 and still Property was purchased. How many such records are 
# there in the data set. Print the first five rows. 
# • Use the arrange() function in dplyr to -: 
# • Create a data frame by the name ‘bought’ – which includes observations when the Property was purchased. 
# How many observations are there. 
# • Arrange the data frame bought by Income and print the first five rows. 
# • Arrange the data frame bought by Gender and print the first five rows. 
# • Arrange the data frame bought so that Gender and Education is grouped and print the first five rows. 
# • Create a data frame by the name ‘notbought’ – which includes observations when the Property was not purchased. 
# How many observations are there. 
# • Arrange the data frame notbought by Income and print the first five rows. 
# • Arrange the data frame notbought by Gender and print the first five rows. 
# • Arrange the data frame notbought so that Gender and Education is grouped and print the first five rows. 
# • Reverse the order of arranging - Arrange the housing data according to Gender and decreasing Income. 
# Print the first five rows.
# 

g3 <- filter(data,PropertyValue < 80000 | PropertyValue > 150000)

g3[1:5,]

no_of_observation_g3 = nrow(g3)

print(no_of_observation_g3)


g4 <- filter(data,PropertyValue > 1000000 & Income < 3185)

g4[1:5,]

no_of_observation_g4 = nrow(g4)

print(no_of_observation_g4)

g5 <- filter(data,Income < 3185 & Property_Purchased == 'Y')

no_of_observation_g5 = nrow(g5)

print(no_of_observation_g5)

g5[1:5,]

bought <- filter(data,Property_Purchased == 'Y')

print(nrow(bought))

class(bought)

print(arrange(bought,Income)[1:5,])

print(arrange(bought,Gender)[1:5,])

print(arrange(bought,Gender,Education)[1:5,])

notbought <- filter(data,Property_Purchased != 'Y')

print(nrow(notbought))

print(arrange(notbought,Income) [1:5,])

print(arrange(notbought,Gender) [1:5,])

print(arrange(notbought,Gender,Education) [1:5,]) 

print(arrange(data,Gender,desc(Income)) [1:5,])


# 5. 
# Summarise function:  
# • Print out a summary with variables min_income and max_income. 
# • Generate summary statistics about Income column of housing dataframe. The summary should print minimum, 
# maximum, average, standard deviation, and IQR of the variable. 
# • Generate summary about PropertyValue column of housing. The output should print minimum, maximum, 
# average, standard deviation, and IQR of the variable. 
# • Generate summary about Loan_Period column of housing. The output should print minimum, maximum, 
# average, standard deviation, and IQR of the variable.

summarise(data,min_income=min(Income),max_income=max(Income))

summarise(data,minimum_Income=min(Income),maximum_Income=max(Income),
          average_Income=mean(Income),Standard_deviation_Income=sd(Income),IQR_Income=IQR(Income))

summarise(data,minimum_Loan_Period=min(Loan_Period),maximum_Loan_Period=max(Loan_Period),
          average_Loan_Period=mean(Loan_Period),Standard_deviation_Loan_Period=sd(Loan_Period),
          IQR_Loan_Period=IQR(Loan_Period))


# 6. 
# the pipe operator of dplyr: reproduce the below steps using dplyr and pipe operator 
# • Start with the housing data set and then
# • Add the new variable var1 which calculates the ratio of property value to total income 
# • Pick all-of the rows whose var1 value exceeds 50, and then 
# • Summarize the data set with a value named avg. that is the mean value of var1. 
# • Finally report the output of the above steps.

data %>% mutate(var1=PropertyValue/Income) %>% filter(var1>50) %>% summarise(avg=mean(var1))

# 7. 
# using group_by function of dplyr: reproduce the below steps  
# • Start with the housing data set and then 
# • Use group_by() to group housing by Education. 
# • summarise() the grouped df with two summary variables: avg_income, the average of Income, and avg_Value, 
# the average value of purchased property.  
# • Finally, order the summary from low to high by these two summarized variables
# • Finally report the output of the above steps

data %>% group_by(Education) %>% summarise(avg_income=mean(Income), avg_Value=mean(PropertyValue)) %>% 
  arrange(avg_income,avg_Value)
