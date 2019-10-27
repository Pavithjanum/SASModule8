# 1.
# Given a vector “First_Hundred”, which comprises of sequence of first hundred natural numbers:
# • Change all the odd numbers to the string “ODD”
# • Change all the even numbers to the string “EVEN”

rm(First_Hundred)

First_Hundred = c(1:100)

for (i in First_Hundred)
{
  if((i%%2) != 0)
  {
    First_Hundred[i] = 'ODD'
  }
  else
  {
    First_Hundred[i] = 'EVEN'
  }
}

   
#2.
# From the “iris” dataset, find the number of observations whose “Sepal.Length” 
#is greater than ‘6.5’ by using only loops and conditional statements

View(iris)

colnames(iris)

no_of_observe = 0

for (row in iris[,1])
{
  if((is.numeric(row)) & (row>6.5))
  {
    print(row)
    no_of_observe = no_of_observe + 1
  }
}

print(no_of_observe)

#3.
# “CO2” is a preloaded data-set in R. From the “CO2” data-set, find the mean 
# ‘uptake’ of only those observations where Type is “Mississippi” and Treatment 
# is ‘chilled’. You can use only loops and conditional statements.

View(CO2)

colnames(CO2)


data = data.frame(CO2)

r=data[,]

sum = 0
count=0

for (i in c(1:nrow(CO2)))
{
  print(r[i,])
  
  if (r[i,2]=='Mississippi' & r[i,3] =='chilled')
  {
    sum = sum + r[i,5]
    count = count +1
    
  }
}

print(sum)
print(i)

Average = sum/nrow(CO2)
print(Average)
Avg  = sum/count
print(Avg)

tapply(CO2$uptake,(CO2$Type=='Mississippi'& CO2$Treatment=='chilled'),sum)

tapply(CO2$uptake,(CO2$Type=='Mississippi'& CO2$Treatment=='chilled'),mean)

#4.
# On the "CO2" data-set, use 'tapply()' function to obtain mean, median, 
# minimum and maximum values of 'uptake' with respect to the 'Treatment' column

tapply(CO2$uptake,CO2$Treatment,mean)
tapply(CO2$uptake,CO2$Treatment,median)
tapply(CO2$uptake,CO2$Treatment,min)
tapply(CO2$uptake,CO2$Treatment,max)

#5.
# 'swiss' is a preloaded data-set in R. Using the 'invoke_map()' function, 
# find out the minimum 'Fertility' and maximum 'Infant.Mortality' from the 
# 'swiss' data-set.

View(swiss)

install.packages('purrr')

library(purrr)

invoke_map(list(Min_Fertility="min",Max_Infant.Mortality="max")
           ,list(swiss$Fertility,swiss$Infant.Mortality)) 

#6
# Create a custom function "dice()" which will give a random number 
# between 1-6 every time the function is invoked.

dice <- function(){
  print(sample(1:6, size=1))
}

dice()
  
